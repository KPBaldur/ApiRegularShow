#!/usr/bin/env python3
"""
Script de inicio para la API Regular Show
Uso: python start_server.py
"""

import uvicorn
import sys
import os

def main():
    print("🚀 Iniciando API Regular Show...")
    print("=" * 50)
    
    try:
        # Verificar que estamos en el directorio correcto
        if not os.path.exists("app/main.py"):
            print("❌ Error: No se encuentra app/main.py")
            print("   Asegúrate de estar en el directorio raíz del proyecto")
            sys.exit(1)
        
        # Importar la aplicación
        from app.main import app
        
        print("✅ Aplicación cargada correctamente")
        print(f"📋 Título: {app.title}")
        print(f"📦 Versión: {app.version}")
        print(f"🔗 Rutas disponibles: {len(app.routes)}")
        
        # Configuración del servidor
        config = uvicorn.Config(
            app=app,
            host="127.0.0.1",
            port=8000,
            reload=True,
            log_level="info",
            access_log=True
        )
        
        server = uvicorn.Server(config)
        
        print("\n🌐 Servidor iniciándose...")
        print("📍 URL: http://127.0.0.1:8000")
        print("📚 Documentación: http://127.0.0.1:8000/docs")
        print("🔴 Para detener: Ctrl+C")
        print("=" * 50)
        
        # Iniciar servidor
        server.run()
        
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido por el usuario")
    except Exception as e:
        print(f"\n❌ Error al iniciar el servidor: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 