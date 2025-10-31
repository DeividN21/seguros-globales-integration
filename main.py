import time
from scripts.fase1_preparacion import simular_fase1
from scripts.fase2_infraestructura import simular_fase2
from scripts.fase3_seguridad import simular_fase3
from scripts.fase4_integracion import simular_fase4
from scripts.fase5_pruebas import simular_fase5
from scripts.fase6_operacion import simular_fase6

def main():
    print("Iniciando simulación de la solución para Seguros Globales...")
    time.sleep(1)
    
    simular_fase1()
    simular_fase2()
    simular_fase3()
    simular_fase4()
    simular_fase5()
    simular_fase6()
    
    print("Simulación completada exitosamente.")

if __name__ == "__main__":
    main()