"""
Proyecto Python y Mysql:
-Abrir asistente
-Login o registro
-Si elegimos registro, creará un usuario en la base de datos
- Crear nota, mostrar notas, borrarlas
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -registro
    -login
""")
realiza = acciones.Acciones()
action = input("¿Que quieres hacer?: ")

if action == "registro":
    realiza.registro()
elif action == "login":
    realiza.login()
