# Contador de Intentos de Acceso
# Este script simula el conteo de intentos fallidos de un usuario

intentos_fallidos = 0
limite_seguridad = 5

print("=== Monitoreando intentos de acceso ===")

# Simulamos 6 intentos
for i in range(1, 7):
    intentos_fallidos = i
    print(f"Intento numero {intentos_fallidos} registrado.")
    
    if intentos_fallidos >= limite_seguridad:
        print("[BLOQUEO] Se ha alcanzado el limite de seguridad.")
        break # Detiene el conteo al llegar al limite

print("\nProceso de monitoreo finalizado.")
