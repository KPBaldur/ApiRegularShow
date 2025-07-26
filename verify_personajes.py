import json

# Cargar el archivo de personajes
with open('app/data/personajes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total de personajes: {len(data)}")

# Verificar tipos de personaje
tipos = set(p["tipo_personaje"] for p in data)
print(f"Tipos de personaje: {tipos}")

# Contar por tipo
for tipo in tipos:
    count = len([p for p in data if p["tipo_personaje"] == tipo])
    print(f"{tipo}: {count} personajes")

# Verificar estructura del primer personaje
if data:
    primer_personaje = data[0]
    print(f"\nEstructura del primer personaje:")
    for key, value in primer_personaje.items():
        print(f"  {key}: {value}")

# Verificar que no hay campos "estado"
personajes_con_estado = [p for p in data if "estado" in p]
if personajes_con_estado:
    print(f"\nERROR: {len(personajes_con_estado)} personajes aún tienen campo 'estado'")
else:
    print(f"\n✓ Todos los personajes tienen la estructura correcta (sin campo 'estado')")

# Verificar que todos tienen campo "tipo_personaje"
personajes_sin_tipo = [p for p in data if "tipo_personaje" not in p]
if personajes_sin_tipo:
    print(f"\nERROR: {len(personajes_sin_tipo)} personajes no tienen campo 'tipo_personaje'")
else:
    print(f"\n✓ Todos los personajes tienen campo 'tipo_personaje'") 