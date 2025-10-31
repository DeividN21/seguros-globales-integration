import csv
import hashlib
import time
import os
from datetime import datetime

def generar_checksum(archivo):
    sha256 = hashlib.sha256()
    with open(archivo, 'rb') as f:
        sha256.update(f.read())
    return sha256.hexdigest()

def simular_fase4():
    print("\n--- Fase 4: Componentes de Integración ---")
    
    # Seguros Globales: Generador CSV (RF1, RF2)
    print("a. Seguros Globales: Generando CSV de reclamos.")
    fecha = datetime.now().strftime("%Y%m%d")
    lote_id = "001"
    archivo_reclamos = f"simulacion_sftp/inbound/SG_RECLAMOS_{fecha}_L{lote_id}.csv"
    with open(archivo_reclamos, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['numero_poliza', 'monto_reclamo', 'fecha_siniestro', 'descripcion'])
        writer.writerow(['POL123', '5000', '2023-10-01', 'Accidente vehicular'])
    checksum = generar_checksum(archivo_reclamos)
    with open(f"{archivo_reclamos}.sha256", 'w') as f:
        f.write(checksum)
    print(f"Archivo generado: {archivo_reclamos} con checksum.")
    time.sleep(1)
    
    # Constructora: Monitor SFTP (simulado con chequeo de directorio)
    print("b. Consultora: Monitoreando SFTP y descargando (RF2).")
    time.sleep(2)  # Simula polling
    print("Archivo detectado y 'descargado' (copiado localmente).")
    
    # Constructora: Procesador Legacy (RF4)
    print("c. Consultora: Procesando siniestros.")
    archivo_respuesta = f"simulacion_sftp/outbound/CONS_RESP_{fecha}_L{lote_id}.csv"
    with open(archivo_respuesta, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['siniestro', 'estado'])
        writer.writerow(['POL123', 'aprobado'])
    checksum = generar_checksum(archivo_respuesta)
    with open(f"{archivo_respuesta}.sha256", 'w') as f:
        f.write(checksum)
    print(f"Respuesta generada: {archivo_respuesta}.")
    time.sleep(1)

    # Seguros Globales: Ingestor Respuestas (RF5)
    print("d. Seguros Globales: Descargando y procesando respuesta.")
    time.sleep(1)
    with open('simulacion_sftp/logs/ingestion.log', 'a') as f:
        f.write("Respuesta procesada exitosamente.\n")
    print("Fase 4 completada.")