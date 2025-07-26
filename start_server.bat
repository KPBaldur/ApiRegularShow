@echo off
echo ========================================
echo    API Regular Show - Iniciando...
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    pause
    exit /b 1
)

REM Verificar si estamos en el directorio correcto
if not exist "app\main.py" (
    echo ERROR: No se encuentra app\main.py
    echo Asegúrate de estar en el directorio raíz del proyecto
    pause
    exit /b 1
)

REM Instalar dependencias si es necesario
echo Verificando dependencias...
pip install -r requirements.txt >nul 2>&1

echo.
echo Iniciando servidor...
echo URL: http://127.0.0.1:8000
echo Documentación: http://127.0.0.1:8000/docs
echo Para detener: Ctrl+C
echo.

REM Iniciar el servidor
python start_server.py

pause 