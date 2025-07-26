#!/usr/bin/env python3
"""
Verificación final del proyecto API Regular Show
"""

import os
import json
import sys

def verificar_estructura():
    print("🔍 VERIFICACIÓN FINAL DEL PROYECTO")
    print("=" * 50)
    
    # Verificar archivos principales
    archivos_requeridos = [
        "app/main.py",
        "app/config.py", 
        "app/models.py",
        "app/errors.py",
        "app/data/data_manager.py",
        "app/data/personajes.json",
        "app/data/capitulos.json",
        "app/data/temporadas.json",
        "app/data/comics.json",
        "app/routers/personajes.py",
        "app/routers/capitulos.py",
        "app/routers/temporadas.py",
        "app/routers/comics.py",
        "requirements.txt",
        "start_server.py",
        "start_server.bat"
    ]
    
    print("\n📁 Verificando archivos principales:")
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            print(f"   ✅ {archivo}")
        else:
            print(f"   ❌ {archivo} - FALTANTE")
            return False
    
    return True

def verificar_datos():
    print("\n📊 Verificando datos JSON:")
    
    archivos_json = ["personajes", "capitulos", "temporadas", "comics"]
    for archivo in archivos_json:
        try:
            with open(f"app/data/{archivo}.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"   ✅ {archivo}.json: {len(data)} elementos")
        except Exception as e:
            print(f"   ❌ {archivo}.json: Error - {e}")
            return False
    
    return True

def verificar_personajes():
    print("\n👥 Verificando estructura de personajes:")
    
    try:
        with open("app/data/personajes.json", "r", encoding="utf-8") as f:
            personajes = json.load(f)
        
        # Verificar campos requeridos
        campos_requeridos = ["id", "nombre", "nombre_ingles", "nombre_latino", "raza", 
                           "profesion", "capitulo_aparicion", "comic_aparicion", 
                           "tipo_personaje", "imagen_url"]
        
        primer_personaje = personajes[0]
        for campo in campos_requeridos:
            if campo not in primer_personaje:
                print(f"   ❌ Campo faltante: {campo}")
                return False
        
        # Verificar que no hay campo "estado"
        personajes_con_estado = [p for p in personajes if "estado" in p]
        if personajes_con_estado:
            print(f"   ❌ {len(personajes_con_estado)} personajes aún tienen campo 'estado'")
            return False
        
        # Verificar tipos de personaje
        tipos = set(p["tipo_personaje"] for p in personajes)
        tipos_validos = {"Principal", "Secundario", "Antagonista"}
        if not tipos.issubset(tipos_validos):
            print(f"   ❌ Tipos de personaje inválidos: {tipos - tipos_validos}")
            return False
        
        print(f"   ✅ {len(personajes)} personajes con estructura correcta")
        print(f"   ✅ Tipos de personaje: {tipos}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error verificando personajes: {e}")
        return False

def verificar_importaciones():
    print("\n🔧 Verificando importaciones:")
    
    try:
        from app.main import app
        print("   ✅ app.main importado correctamente")
        
        from app.config import settings
        print(f"   ✅ app.config importado - {settings.app_name}")
        
        from app.models import Personaje, Capitulo, Temporada, Comic
        print("   ✅ app.models importado correctamente")
        
        from app.data.data_manager import DataManager
        print("   ✅ app.data.data_manager importado correctamente")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error en importaciones: {e}")
        return False

def verificar_uvicorn():
    print("\n🚀 Verificando uvicorn:")
    
    try:
        import uvicorn
        print(f"   ✅ Uvicorn {uvicorn.__version__} disponible")
        
        from app.main import app
        config = uvicorn.Config(app=app, host="127.0.0.1", port=8000)
        print("   ✅ Configuración de uvicorn válida")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error con uvicorn: {e}")
        return False

def main():
    print("🎯 VERIFICACIÓN FINAL - API REGULAR SHOW")
    print("=" * 60)
    
    checks = [
        ("Estructura de archivos", verificar_estructura),
        ("Datos JSON", verificar_datos),
        ("Estructura de personajes", verificar_personajes),
        ("Importaciones", verificar_importaciones),
        ("Uvicorn", verificar_uvicorn)
    ]
    
    resultados = []
    for nombre, funcion in checks:
        print(f"\n🔍 {nombre}...")
        resultado = funcion()
        resultados.append((nombre, resultado))
    
    print("\n" + "=" * 60)
    print("📋 RESUMEN DE VERIFICACIÓN:")
    
    exitos = 0
    for nombre, resultado in resultados:
        status = "✅ EXITOSO" if resultado else "❌ FALLIDO"
        print(f"   {nombre}: {status}")
        if resultado:
            exitos += 1
    
    print(f"\n🎯 Resultado: {exitos}/{len(resultados)} verificaciones exitosas")
    
    if exitos == len(resultados):
        print("\n🎉 ¡PROYECTO LISTO PARA EJECUTAR!")
        print("\n📝 Para iniciar el servidor:")
        print("   python start_server.py")
        print("   o")
        print("   start_server.bat")
        print("\n🌐 URL: http://127.0.0.1:8000")
        print("📚 Docs: http://127.0.0.1:8000/docs")
    else:
        print("\n⚠️  Hay problemas que necesitan ser corregidos antes de ejecutar")
        sys.exit(1)

if __name__ == "__main__":
    main() 