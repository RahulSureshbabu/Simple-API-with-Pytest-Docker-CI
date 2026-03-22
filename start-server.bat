@echo off
REM Start the API server for tests
cd /d "%~dp0my-api"
if not exist node_modules\ (echo Installing dependencies... & npm install)
echo Starting server on http://localhost:3000 ...
node index.js
