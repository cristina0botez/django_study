@echo off

if "%cd:~0,1%" neq "D" (
    D:
)
if "%1"=="cris" (
    cd "D:\Workspace\PythonStudy\Django\cris"
) else (
    cd "D:\Workspace\PythonStudy\Django\cris\apps\%1"
)

