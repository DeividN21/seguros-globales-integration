import time

def simular_fase6():
    print("\n--- Fase 6: Operación ---")
    print("a. Rollout controlado: Iniciando en horas de baja actividad.")
    time.sleep(1)
    print("b. Monitorización 24-72h: Equipo de soporte activo (simulado con logs).")
    with open('simulacion_sftp/logs/operacion.log', 'w') as f:
        f.write("Sistema en operación normal.\n")
    time.sleep(1)
    print("c. Documentación: Runbooks, SLAs y contactos generados.")
    time.sleep(1)
    print("Fase 6 completada: Sistema 'en producción'.")