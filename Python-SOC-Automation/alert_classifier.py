# Herramienta de Automatizacion para SOC - Clasificador de Alertas
# Este script ayuda a priorizar incidentes de seguridad de forma rapida

print("=== Sistema de Triaje de Alertas SOC ===")

# 1. Entrada de datos por parte del usuario
evento = input("Tipo de evento (ddos, login, malware): ").lower()
ip_origen = input("Ingrese la direccion IP de origen: ")

# 2. Logica de decision simplificada
if evento == "ddos":
    prioridad = "ALTA"
    accion = "Ejecutar protocolo de mitigacion en Firewall."
elif evento == "malware":
    prioridad = "MEDIA"
    accion = "Aislar el host infectado para analisis."
elif evento == "login":
    intentos = int(input("Numero de intentos fallidos: "))
    if intentos > 5:
        prioridad = "MEDIA"
        accion = "Bloqueo temporal de cuenta."
    else:
        prioridad = "BAJA"
        accion = "Registrar en log de auditoria."
else:
    prioridad = "INFO"
    accion = "Revision manual por un Analista SOC."

# 3. Salida del reporte final
print("\n--- REPORTE DE INCIDENTE ---")
print(f"EVENTO: {evento.upper()} | IP: {ip_origen}")
print(f"PRIORIDAD: {prioridad} | ACCION: {accion}")
