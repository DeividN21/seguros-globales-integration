# Simulación de Solución para Caso de Estudio: Seguros Globales

Esta es una simulación en Python de la integración de sistemas entre Seguros Globales y la Consultora de Siniestros, usando un SFTP simulado con directorios locales. Se basa en los requisitos, diagramas y plan de implementación del informe. La simulación ejecuta las 6 fases secuencialmente mediante prints en consola y operaciones de archivos.

## Estructura del Proyecto (Carpetas y Archivos)
```
simulacion-seguros-globales/
├── README.md                  # Instrucciones para clonar y ejecutar
├── .gitignore                 # Ignora archivos temporales
├── requirements.txt           # Dependencias (opcional, Python estándar)
├── scripts/                   # Scripts para simular fases
│   ├── fase1_preparacion.py   # Simula Fase 1: Preparación
│   ├── fase2_infraestructura.py # Simula Fase 2: Infraestructura
│   ├── fase3_seguridad.py     # Simula Fase 3: Seguridad
│   ├── fase4_integracion.py   # Simula Fase 4: Componentes de integración
│   ├── fase5_pruebas.py       # Simula Fase 5: Validación y pruebas
│   └── fase6_operacion.py     # Simula Fase 6: Operación
├── simulacion_sftp/           # Simulación del servidor SFTP
│   ├── inbound/               # Archivos de reclamos (SG a CONS)
│   ├── outbound/              # Archivos de respuestas (CONS a SG)
│   └── logs/                  # Logs simulados
├── datos_ejemplo/             # Datos sintéticos para pruebas
│   ├── reclamos_ejemplo.csv   # Ejemplo de CSV de reclamos
│   └── respuestas_ejemplo.csv # Ejemplo de CSV de respuestas
└── main.py                    # Script principal que ejecuta las fases
```

## Cómo Clonar y Ejecutar

1. **Requisitos:**
   - Python 3.x instalado (no se necesitan paquetes externos, se usa librerías estándar como `csv`, `hashlib`, `os`, `time`, `datetime`).

2. **Clonar el Repositorio:**
   - Abrir una terminal y ejecutar:
     ```
      git clone https://github.com/DeividN21/seguros-globales-integration.git
     ```
3. **Entrar al Directorio:**
   ```
   cd seguros-globales-integration
   ```
4. **Ejecutar la Simulación:**
- Ejecutar el script principal:
  ```
   python main.py
  ```
- Esto simulará todas las fases, generando archivos en `simulacion_sftp/` y logs.
- Puede observar los prints en consola para ver el flujo paso a paso.

5. **Notas:**
- Los archivos generados siguen las convenciones (p.ej., SG_RECLAMOS_YYYYMMDD_L001.csv con .sha256).
- Para reiniciar: Se debe borrar los directorios `simulacion_sftp/` manualmente.
- Esta es una simulación; no es para producción real.

Si se tiene problemas, puede revisar los logs en `simulacion_sftp/logs/`.

