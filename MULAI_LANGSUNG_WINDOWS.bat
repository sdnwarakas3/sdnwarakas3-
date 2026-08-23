@echo off
title SDN WARAKAS 3 - SERVER OTOMATIS
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (py server.py) else (
  where python >nul 2>nul
  if %errorlevel%==0 (python server.py) else (
    echo Python belum terpasang di komputer ini.
    echo Pasang Python 3, lalu klik file ini lagi.
    pause
  )
)
