import simpy
import random

class SimulacionRedComputadoras:
    def __init__(self):
        # Variables para seguimiento de estadísticas
        self.paquetes_perdidos = 0
        self.tiempo_total_espera = 0
        self.paquetes_procesados = 0
        self.env = None  # El entorno de simulación
        self.servidor = None  # El recurso del servidor

    def iniciar(self, semilla, capacidad_servidor, capacidad_cola, 
                tiempo_procesamiento_min, tiempo_procesamiento_max, 
                tiempo_llegadas, total_paquetes):
        """Inicia el proceso de simulación con los parámetros especificados."""
        self.semilla = semilla
        self.capacidad_servidor = capacidad_servidor
        self.capacidad_cola = capacidad_cola
        self.tiempo_procesamiento_min = tiempo_procesamiento_min
        self.tiempo_procesamiento_max = tiempo_procesamiento_max
        self.tiempo_llegadas = tiempo_llegadas
        self.total_paquetes = total_paquetes
        
        # Configuración de la simulación
        random.seed(self.semilla)  # Establece la semilla para reproducir resultados
        self.env = simpy.Environment()  # Crea el entorno de simulación
        self.servidor = simpy.Resource(self.env, self.capacidad_servidor)  # Crea el recurso del servidor

        # Inicia el proceso de llegada de paquetes
        self.env.process(self.llegada_paquetes())
        self.env.run()  # Ejecuta la simulación
        self.mostrar_resultados()

    def paquete(self, nombre):
        """Simula el proceso de un paquete."""
        llegada = self.env.now  # Momento de llegada del paquete al sistema
        print(f'{nombre} llega al servidor en el segundo {llegada:.2f}')

        with self.servidor.request() as req:
            # Si el servidor y la cola están llenos, el paquete se pierde
            if len(self.servidor.queue) >= self.capacidad_cola:
                self.paquetes_perdidos += 1
                print(f'{nombre} se pierde debido a cola llena en el segundo {self.env.now:.2f}')
                return

            # El paquete espera su turno en la cola si es necesario
            yield req
            espera = self.env.now - llegada
            self.tiempo_total_espera += espera
            print(f'{nombre} comienza a ser procesado después de esperar {espera:.2f} segundos en el segundo {self.env.now:.2f}')

            # Simula el tiempo de procesamiento del paquete
            tiempo_procesamiento = random.randint(self.tiempo_procesamiento_min,
                                                  self.tiempo_procesamiento_max)
            yield self.env.timeout(tiempo_procesamiento)
            print(f'{nombre} termina de ser procesado en el segundo {self.env.now:.2f}')
            self.paquetes_procesados += 1

    def llegada_paquetes(self):
        """Genera la llegada de paquetes al servidor."""
        for i in range(self.total_paquetes):
            yield self.env.timeout(random.expovariate(1.0 / self.tiempo_llegadas))  # Tiempo entre llegadas
            self.env.process(self.paquete(f'Paquete {i + 1}'))

    def mostrar_resultados(self):
        """Muestra los resultados de la simulación."""
        print('--- Fin de la simulación ---')
        print("\nResultados de la simulación:")
        print(f'Total de paquetes simulados: {self.total_paquetes}')
        print(f'Paquetes procesados: {self.paquetes_procesados}')
        print(f'Paquetes perdidos: {self.paquetes_perdidos}')
        print(f'Tasa de pérdida de paquetes: {100 * self.paquetes_perdidos / self.total_paquetes:.2f}%')
        print(f'Tiempo promedio de espera de los paquetes: {self.tiempo_total_espera / self.paquetes_procesados if self.paquetes_procesados > 0 else 0:.2f} segundos')
        print(f'Utilización del servidor: {100 * (self.paquetes_procesados * (self.tiempo_procesamiento_min + self.tiempo_procesamiento_max) / 2) / self.env.now:.2f}%')


