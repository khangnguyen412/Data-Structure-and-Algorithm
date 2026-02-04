## Data Structure and Algorithm
- Descripttion: Learn data structure and algorithm.

## Language in project:
- Language: C++

## How to start and testing project
### Setup project
1. Install MSYS2 from https://www.msys2.org/
2. Setup launch.json in .vscode folder
```JSON
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Build & Run",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "C:/msys64/ucrt64/bin/gdb.exe",
            "preLaunchTask": "C/C++: gcc.exe build active file",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]
        }
    ]
}
```

3. Setup tasks.json in .vscode folder
```JSON
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "cppbuild",
            "label": "C/C++: gcc.exe build active file",
            "command": "C:/msys64/ucrt64/bin/g++.exe",
            "args": [
                "-fdiagnostics-color=always",
                "-g",
                "${file}",
                "-o",
                "${workspaceFolder}\\build\\${fileBasenameNoExtension}.exe"
            ],
            "options": {
                "cwd": "C:/msys64/ucrt64/bin"
            },
            "problemMatcher": ["$gcc"],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

## Project structure 
```
DSA/
 ┣ .vscode
 ┃ ┣ launch.json
 ┃ ┣ settings.json
 ┃ ┗ tasks.json
 ┣ build
 ┃ ┣ HelloWorld.exe
 ┃ ┗ Recursion.exe
 ┣ src
 ┃ ┣ HelloWorld.cpp
 ┃ ┗ Recursion.cpp
 ┣ README.md
 ┗ run.bat
```

The source was set up by KhangNguyen — do not copy