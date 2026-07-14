#!/bin/bash
# SmrtDesk GitHub 自动部署脚本
# 用法：在 VPS 上运行一次即可
# curl -sL https://raw.githubusercontent.com/hlsst2024-cyber/smrtdesk/main/deploy-github.sh | bash

set -e

echo "=== SmrtDesk GitHub Deploy ==="

# 如果已存在仓库就 pull，否则 clone
if [ -d "/root/smrtdesk/.git" ]; then
    echo "Existing repo found, pulling..."
    cd /root/smrtdesk
    git pull origin main
else
    echo "Fresh clone..."
    cd /root
    rm -rf /root/smrtdesk 2>/dev/null || true
    git clone https://github.com/hlsst2024-cyber/smrtdesk.git smrtdesk
    cd /root/smrtdesk
fi

# 设置文件权限
find . -type f -name "*.html" -exec chmod 644 {} \;
find . -type f -name "*.css" -exec chmod 644 {} \;
find . -type f -name "*.js" -exec chmod 644 {} \;
find . -type f -name "*.xml" -exec chmod 644 {} \;
find . -type f -name "*.txt" -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;

# Copy to nginx web root
echo "Copying files to web root..."
WEBROOT=""
if [ -d "/var/www/smrtdesk" ]; then WEBROOT="/var/www/smrtdesk"; fi
if [ -d "/usr/share/nginx/html" ] && [ -z "$WEBROOT" ]; then WEBROOT="/usr/share/nginx/html"; fi
if [ -n "$WEBROOT" ]; then
    cp -r ./* "$WEBROOT/"
    echo "Copied to $WEBROOT"
else
    echo "WARNING: Could not determine nginx web root"
fi

# Nginx reload
echo "Testing nginx config..."
nginx -t && nginx -s reload && echo "=== Deploy OK ===" || echo "=== Nginx Error ==="
