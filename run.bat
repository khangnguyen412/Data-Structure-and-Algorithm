@echo off
setlocal

if "%1"=="" (
    echo Usage: .\run.bat [sub_folder]\[file_name]
    exit /b 1
)

if not exist build (
    mkdir build
)

:: Kiểm tra nếu file nguồn là Python
if exist src\%1.py (
    echo Running Python script: src\%1.py
    python src\%1.py
) else (
    echo File not found: src\%1.py
    exit /b 1
)

if errorlevel 1 (
    echo Execution failed
    exit /b 1
)

echo Execution success