import time

def simular_fase3():
    print("\n--- Fase 3: Seguridad ---")
    print("a. Creando cuentas y pares de claves SSH para SG y CONS (evitando contraseñas - RNF1, RNF3).")
    time.sleep(1)
    print("b. Configurando logs en simulacion_sftp/logs (para monitoreo de errores - RF3).")
    with open('simulacion_sftp/logs/security.log', 'w') as f:
        f.write("Log inicial: Accesos configurados.\n")
    time.sleep(1)
    print("c. Implementando validaciones en servidor (checksums - políticas).")
    time.sleep(1)
    print("Fase 3 completada.")