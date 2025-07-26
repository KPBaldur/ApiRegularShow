import uvicorn
import sys
import os

print("=== PRUEBA DE UVICORN ===\n")

try:
    print("1. Verificando que uvicorn puede importar la aplicación...")
    from app.main import app
    print("   ✓ Aplicación importada correctamente")
    
    print("\n2. Verificando configuración de uvicorn...")
    print(f"   ✓ Uvicorn versión: {uvicorn.__version__}")
    
    print("\n3. Simulando el comando uvicorn app.main:app --reload...")
    print("   Esto debería iniciar el servidor en http://127.0.0.1:8000")
    print("   Presiona Ctrl+C para detener el servidor")
    
    # Configuración de uvicorn
    config = uvicorn.Config(
        app=app,
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )
    
    server = uvicorn.Server(config)
    
    print("\n4. Iniciando servidor...")
    print("   Si ves este mensaje, el servidor se está iniciando correctamente")
    print("   Abre http://127.0.0.1:8000/docs en tu navegador")
    
    # Iniciar el servidor
    server.run()
    
except KeyboardInterrupt:
    print("\n✓ Servidor detenido correctamente")
except Exception as e:
    print(f"\n✗ ERROR al iniciar uvicorn: {e}")
    import traceback
    print("\nTraceback completo:")
    traceback.print_exc() 