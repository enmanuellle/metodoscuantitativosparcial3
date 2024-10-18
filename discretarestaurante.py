import os
import sys
import random
import simpy

class SimulacionRestaurante:
    def __init__(self, num_counters=3, customer_range_norm=(5, 10), sim_time=960):
        self.num_counters = num_counters  # Número de mostradores
        self.customer_range_norm = customer_range_norm  # Rango de tiempo de llegada de clientes
        self.sim_time = sim_time  # Tiempo total de simulación en minutos
        self.avg_service_time = 0  # Tiempo promedio de servicio
        self.service_per_minute = 0  # Servicio por minuto
        self.calculations = [0] * 500  # Almacena los tiempos de servicio para cada cliente
        self.customer_count = 0  # Número de clientes atendidos
        self.env = simpy.Environment()  # Crea el entorno de simulación
        self.waiting_lane = FilaEspera(self.env)  # Crea la fila de espera
        self.counters = [Mostrador(self.env) for _ in range(num_counters)]  # Crea los mostradores

    def run(self):
        print("¡Inicia la simulación!")
        self.env.process(self.setup())  # Inicia el proceso de configuración
        self.env.run(until=self.sim_time)  # Ejecuta la simulación hasta el tiempo final

        # Calcula el tiempo promedio de servicio y la tasa de servicio
        self.avg_service_time = sum(self.calculations) / self.customer_count if self.customer_count > 0 else 0
        self.service_per_minute = 1.0 / (self.avg_service_time * 60) if self.avg_service_time > 0 else 0

        self.report()

    def report(self):
        """Reporta los resultados después de la simulación."""
        print("¡Fin de la simulación!")
        print(f"[i] Modelo: {self.num_counters} mostradores")
        print(f"[i] Tiempo promedio:       {self.avg_service_time:.4f}")
        print(f"[i] Servicio por minuto: {self.service_per_minute:.2f}")

    def setup(self):
        """Crea clientes durante la simulación."""
        while True:
            yield self.env.timeout(random.randint(*self.customer_range_norm))
            self.customer_count += 1
            customer_name = f'Cust {self.customer_count}'
            self.env.process(self.customer_process(customer_name))

    def customer_process(self, name):
        """Simula el proceso de un cliente en el restaurante."""
        print(f"[w] ({self.toc(self.env.now)}) {name} llegó a la fila de espera")
        with self.waiting_lane.resource.request() as request:
            yield request
            yield self.env.process(self.waiting_lane.serve(name))

        # Inicia el proceso de servicio real en los mostradores
        for counter in self.counters:
            print(f"[v] ({self.toc(self.env.now)}) {name} está en el mostrador")
            with counter.resource.request() as request:
                yield request
                start_time = self.env.now
                yield self.env.process(counter.serve(name))
                self.calculations[self.customer_count - 1] = self.env.now - start_time
                print(f"[^] ({self.toc(self.env.now)}) {name} sale del mostrador")

    def toc(self, raw):
        """Convierte el tiempo crudo a un formato de hora legible."""
        return f'{raw // 60:02d}:{raw % 60:02d}'


class FilaEspera:
    def __init__(self, env):
        self.env = env
        self.resource = simpy.Resource(env, capacity=3)  # La fila de espera puede acomodar 3 clientes

    def serve(self, cust):
        """Simula la atención a un cliente en la fila de espera."""
        yield self.env.timeout(0)  # Simula el tiempo para entrar en la fila
        print(f"[w] ({SimulacionRestaurante.toc(self, self.env.now)}) {cust} está siendo atendido en la fila de espera")


class Mostrador:
    def __init__(self, env):
        self.env = env
        self.resource = simpy.Resource(env, capacity=1)  # Solo un empleado por mostrador

    def serve(self, cust):
        """Simula la atención a un cliente en este mostrador."""
        service_time = random.randint(1, 3)  # Tiempo de servicio simulado entre 1 y 3 minutos
        yield self.env.timeout(service_time)
        print(f"[$] ({SimulacionRestaurante.toc(self, self.env.now)}) {cust} terminó el servicio en {service_time} minutos")



