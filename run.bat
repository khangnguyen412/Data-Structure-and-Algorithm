@echo off
setlocal

if "%1"=="" (
    echo Usage: run.bat HelloWorld
    exit /b 1
)

if not exist build (
    mkdir build
)

g++ src\%1.cpp -o build\%1.exe

if errorlevel 1 (
    echo Build failed
    exit /b 1
)

echo Build success
build\%1.exe