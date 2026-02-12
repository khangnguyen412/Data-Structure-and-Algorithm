@echo off
setlocal

if "%1"=="" (
    echo Usage: .\run.bat [sub_folder]\[file_name]
    exit /b 1
)

if not exist build (
    mkdir build
)

g++ src\%1.cpp -o build\%~nx1.exe

if errorlevel 1 (
    echo Build failed
    exit /b 1
)

echo Build success: build\%~nx1.exe
build\%~nx1.exe
