@echo off
REM Remove Python cache files
for /d /r %%d in (__pycache__) do rd /s /q "%%d"
for /r %%f in (*.pyc) do del "%%f"
