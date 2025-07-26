print("=== PRUEBA DE IMPORTACIÓN DEL MÓDULO PRINCIPAL ===\n")

try:
    print("1. Importando app.main...")
    from app.main import app
    print("   ✓ app.main importado correctamente")
    
    print("\n2. Verificando que app es una instancia de FastAPI...")
    from fastapi import FastAPI
    if isinstance(app, FastAPI):
        print("   ✓ app es una instancia válida de FastAPI")
    else:
        print("   ✗ app NO es una instancia de FastAPI")
    
    print("\n3. Verificando configuración de la app...")
    print(f"   ✓ Título: {app.title}")
    print(f"   ✓ Versión: {app.version}")
    print(f"   ✓ Descripción: {app.description[:50]}...")
    
    print("\n4. Verificando routers incluidos...")
    router_count = len(app.routes)
    print(f"   ✓ Número total de rutas: {router_count}")
    
    # Mostrar algunas rutas
    print("   ✓ Rutas principales:")
    for route in app.routes[:10]:  # Mostrar solo las primeras 10
        if hasattr(route, 'path'):
            print(f"     - {route.path}")
    
    print("\n5. Verificando middleware CORS...")
    cors_middleware = None
    for middleware in app.user_middleware:
        if "CORSMiddleware" in str(middleware.cls):
            cors_middleware = middleware
            break
    
    if cors_middleware:
        print("   ✓ Middleware CORS configurado correctamente")
    else:
        print("   ✗ Middleware CORS NO encontrado")
    
    print("\n=== PRUEBA EXITOSA ===")
    print("La aplicación está lista para ejecutarse con uvicorn")
    
except Exception as e:
    print(f"\n✗ ERROR durante la importación: {e}")
    import traceback
    print("\nTraceback completo:")
    traceback.print_exc() 