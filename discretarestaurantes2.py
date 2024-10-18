import simpy
import random

class Restaurante:
    def __init__(self, num_mesas, tiempo_comer_min, tiempo_comer_max, tiempo_llegadas, total_clientes, semilla):
        self.num_mesas = num_mesas
        self.tiempo_comer_min = tiempo_comer_min
        self.tiempo_comer_max = tiempo_comer_max
        self.tiempo_llegadas = tiempo_llegadas
        self.total_clientes = total_clientes
        random.seed(semilla)  # Establece la semilla para reproducir resultados
        self.env = simpy.Environment()  # Crea el entorno de simulación
        self.recurso = simpy.Resource(self.env, self.num_mesas)  # Crea el recurso de mesas en el restaurante

    def cliente(self, nombre):
        """Simula el proceso de un cliente que llega, espera una mesa, come y luego se va."""
        print(f'{nombre} llega al restaurante en el minuto {self.env.now:.2f}')

        # El cliente solicita una mesa en el restaurante (espera si no hay mesas disponibles)
        with self.recurso.request() as mesa:
            yield mesa  # Espera a que una mesa esté disponible
            print(f'{nombre} toma una mesa en el minuto {self.env.now:.2f}')

            # Simula el tiempo que el cliente pasa comiendo
            tiempo_comer = random.randint(self.tiempo_comer_min, self.tiempo_comer_max)
            yield self.env.timeout(tiempo_comer)
            print(f'{nombre} termina de comer y deja la mesa en el minuto {self.env.now:.2f}')

    def llegada_clientes(self):
        """Genera la llegada de clientes al restaurante."""
        for i in range(self.total_clientes):
            # Cada cliente llega al restaurante
            yield self.env.timeout(random.expovariate(1.0 / self.tiempo_llegadas))  # Distribución exponencial para el tiempo entre llegadas
            self.env.process(self.cliente(f'Cliente {i + 1}'))

    def run(self):
        """Ejecuta la simulación."""
        print('--- Simulación del Restaurante ---')
        self.env.process(self.llegada_clientes())  # Inicia el proceso de llegada de clientes
        self.env.run()  # Ejecuta la simulación
        print('--- Fin de la simulación ---')


