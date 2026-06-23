#!/usr/bin/env python3
"""
Minimal SSH/SCP deploy using paramiko with specific algorithm configuration
matching what the VPS accepts.
"""
import paramiko
from paramiko.ed25519key import Ed25519Key
import socket, os, hashlib, time

HOST = '2.25.171.203'
PORT = 22
USER = 'root'
KEY_PATH = r'C:\Users\Administrator\.ssh\id_ed25519_vps'
ZIP_PATH = r'D:\openclaw\workspace\smrtdesk\smrtdesk-deploy.zip'
ZIP_NAME = 'smrtdesk-deploy.zip'

print(f'=== smrtdesk deploy v4 ===')
print(f'Target: {HOST}:{PORT}')
print(f'Zip: {ZIP_NAME} ({os.path.getsize(ZIP_PATH)/1024/1024:.1f} MB)')

# Load key
key = Ed25519Key.from_private_key_file(KEY_PATH)

# Create transport with specific settings
# Disable the problematic algorithms
disabled = {
    'kex': ['diffie-hellman-group-exchange-sha256', 'diffie-hellman-group-exchange-sha1'],
}

transport = paramiko.Transport((HOST, PORT))
transport.banner_timeout = 30

try:
    # Use specific kex algorithms that paramiko supports
    # Default paramiko kex list should work with modern OpenSSH
    print(f'Default kex: {transport.get_security_options().kex}')
    
    print('Starting SSH client...')
    transport.start_client()
    print(f'Transport active, authenticating...')
    
    transport.auth_publickey(USER, key)
    print('Authenticated!')
    
    # Open SFTP
    sftp = paramiko.SFTPClient.from_transport(transport)
    
    # Check target dir
    try:
        attrs = sftp.stat('/root/smrtdesk')
        print(f'/root/smrtdesk exists (size={attrs.st_size})')
    except:
        print('/root/smrtdesk not found, will create')
        stdin, stdout, stderr = transport.open_session().exec_command('mkdir -p /root/smrtdesk')
    
    # Upload
    print(f'\nUploading {ZIP_NAME} ({os.path.getsize(ZIP_PATH)/1024/1024:.1f} MB)...')
    t0 = time.time()
    sftp.put(ZIP_PATH, f'/root/smrtdesk/{ZIP_NAME}')
    elapsed = time.time() - t0
    print(f'Uploaded in {elapsed:.1f}s ({os.path.getsize(ZIP_PATH)/1024/1024/elapsed:.1f} MB/s)')
    sftp.close()
    
    # MD5 verify
    local_md5 = hashlib.md5(open(ZIP_PATH, 'rb').read()).hexdigest()
    chan = transport.open_session()
    chan.exec_command(f'md5sum /root/smrtdesk/{ZIP_NAME}')
    remote_line = chan.makefile('r').read().strip()
    remote_md5 = remote_line.split()[0] if remote_line else ''
    print(f'MD5 local:  {local_md5}')
    print(f'MD5 remote: {remote_md5}')
    match = local_md5 == remote_md5
    print(f'Match: {match}')
    
    if match:
        # Deploy
        print('\nDeploying...')
        chan = transport.open_session()
        chan.exec_command(
            f'cd /root/smrtdesk && '
            f'unzip -o {ZIP_NAME} -d /root/smrtdesk/extracted/ 2>&1 && '
            f'echo UNZIP_OK && '
            f'cp -r /root/smrtdesk/extracted/* /root/smrtdesk/ 2>&1 && '
            f'echo COPY_OK && '
            f'nginx -t 2>&1 && '
            f'nginx -s reload 2>&1 && '
            f'echo DEPLOY_DONE'
        )
        out = chan.makefile('r').read()
        err = chan.makefile_stderr('r').read()
        print(f'stdout:\n{out}')
        if err:
            print(f'stderr:\n{err}')
        
        if 'DEPLOY_DONE' in out:
            print('\n*** DEPLOYMENT SUCCESSFUL! ***')
        else:
            print('\n*** Deploy completed (check output) ***')
    
    transport.close()
    
except Exception as e:
    print(f'Error: {e}')
    import traceback
    traceback.print_exc()
    try:
        transport.close()
    except:
        pass
