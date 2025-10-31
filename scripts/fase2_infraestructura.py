import os
import time

def simular_fase2():
    print("\n--- Fase 2: Infraestructura ---")
    print("a. Provisionando servidor SFTP On-Premise (simulado con directorios locales - RNF5).")
    os.makedirs('simulacion_sftp/inbound', exist_ok=True)
    os.makedirs('simulacion_sftp/outbound', exist_ok=True)
    os.makedirs('simulacion_sftp/logs', exist_ok=True)
    time.sleep(1)
    print("b. Configurando sistema de ficheros con cuotas y ACLs (simulado: carpetas segregadas - RNF2).")
    time.sleep(1)
    print("c. Habilitando cifrado de disco y backup local (simulado: prints de encriptación).")
    time.sleep(1)
    print("d. Configurando firewall: Solo IPs autorizadas (simulado).")
    time.sleep(1)
    print("Fase 2 completada.")