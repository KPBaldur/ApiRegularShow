import json
import os

def migrate_capitulos_data():
    """
    Script para migrar los datos de capítulos del formato anterior al nuevo formato
    con títulos en inglés y español.
    """
    
    # Ruta al archivo de capítulos
    capitulos_path = "app/data/capitulos.json"
    backup_path = "app/data/capitulos_backup.json"
    
    # Crear backup del archivo original
    if os.path.exists(capitulos_path):
        with open(capitulos_path, 'r', encoding='utf-8') as f:
            original_data = json.load(f)
        
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(original_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Backup creado en: {backup_path}")
        
        # Migrar datos
        migrated_data = []
        
        for capitulo in original_data:
            # Crear nuevo objeto con la estructura actualizada
            new_capitulo = capitulo.copy()
            
            # Cambiar 'titulo' por 'titulo_eng'
            if 'titulo' in new_capitulo:
                new_capitulo['titulo_eng'] = new_capitulo.pop('titulo')
                # Agregar campo titulo_es vacío para que lo llenes manualmente
                new_capitulo['titulo_es'] = ""  # Aquí agregarás las traducciones
            
            migrated_data.append(new_capitulo)
        
        # Guardar datos migrados
        with open(capitulos_path, 'w', encoding='utf-8') as f:
            json.dump(migrated_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Datos migrados exitosamente")
        print(f"📝 Ahora necesitas llenar los campos 'titulo_es' con las traducciones al español")
        print(f"📁 Total de capítulos migrados: {len(migrated_data)}")
        
        # Mostrar algunos ejemplos para verificar
        print("\n🔍 Primeros 3 capítulos migrados:")
        for i, cap in enumerate(migrated_data[:3]):
            print(f"  {i+1}. ID: {cap.get('id', 'N/A')}")
            print(f"     Título EN: {cap.get('titulo_eng', 'N/A')}")
            print(f"     Título ES: {cap.get('titulo_es', 'PENDIENTE')}")
            print()
    
    else:
        print(f"❌ No se encontró el archivo: {capitulos_path}")

if __name__ == "__main__":
    migrate_capitulos_data()