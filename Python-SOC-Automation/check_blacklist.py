# Verificador de IPs en Lista Negra
# Este script revisa si una IP especifica esta reportada como maliciosa

# 1. Nuestra lista de IPs bloqueadas (Blacklist)
blacklist = ["192.168.1.10", "10.0.0.5", "172.16.0.100"]

# 2. IP que queremos consultar
ip_a_revisar = "10.0.0.5"

print(f"--- Consultando base de datos para la IP: {ip_a_revisar} ---")

# 3. Verificamos si la IP esta en la lista
if ip_a_revisar in blacklist:
    print("[ALERTA] La IP se encuentra en la BLACKLIST.")
    print("ACCION: Bloquear trafico inmediatamente.")
else:
    print("[OK] La IP esta limpia.")
    print("ACCION: Permitir acceso.")
