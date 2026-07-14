@echo off
setlocal enabledelayedexpansion

echo === SmrtDesk Image Upload (Retry Loop) ===

set MAX_TRIES=20
set TRY=1

:retry
echo.
echo --- Attempt !TRY!/%MAX_TRIES% ---
echo Starting scp at %TIME%...

scp -o StrictHostKeyChecking=no -o ConnectTimeout=15 -o ConnectionAttempts=1 -r "D:\openclaw\workspace\smrtdesk\product_images" root@2.25.171.203:/var/www/smrtdesk/

if !ERRORLEVEL! EQU 0 (
    echo SUCCESS!
    goto :done
)

echo Failed (exit code: !ERRORLEVEL!)
set /a TRY+=1
if !TRY! LEQ %MAX_TRIES% (
    echo Waiting 10 seconds...
    ping -n 10 127.0.0.1 >nul
    goto :retry
)

echo Max retries reached.
:done
echo.
echo Finished at %TIME%
