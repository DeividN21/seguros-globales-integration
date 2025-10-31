import time
import os

def simular_fase5():
    print("\n--- Fase 5: Validación y Pruebas ---")
    print("a. Pruebas end-to-end con datos sintéticos (usando datos_ejemplo).")
    time.sleep(1)
    print("b. Validaciones de seguridad: Test de accesos en SFTP simulado (RNF1).")
    time.sleep(1)
    print("c. Prueba de restauración de backups (simulado: copiando archivos).")
    os.system('cp simulacion_sftp/inbound/* datos_ejemplo/')  # Simula backup
    time.sleep(1)
    print("d. Pruebas de fallo: Simulando archivo corrupto (checksum falla).")
    time.sleep(1)
    print("Fase 5 completada: Todas las pruebas pasaron.")