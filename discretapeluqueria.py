import random
import simpy
import math

class Peluqueria:
    def __init__(self, semilla, num_peluqueros, tiempo_corte_min, tiempo_corte_max, t_llegadas, tot_clientes):
        self.semilla = semilla
        self.num_peluqueros = num_peluqueros
        self.tiempo_corte_min = tiempo_corte_min
        self.tiempo_corte_max = tiempo_corte_max
        self.t_llegadas = t_llegadas
        self.tot_clientes = tot_clientes
        self.te = 0.0  # tiempo de espera total
        self.dt = 0.0  # duración del servicio
        self.fin = 0.0  # minuto en que finaliza
        self.env = simpy.Environment()  # creo el entorno de simulación
        self.personal = simpy.Resource(self.env, self.num_peluqueros)  # crea los recursos peluqueros

    def cortar(self, cliente):
        """Simula el corte de cabello del cliente."""
        R = random.random()
        tiempo = self.tiempo_corte_max - self.tiempo_corte_min
        tiempo_corte = self.tiempo_corte_min + (tiempo * R)  # distribución uniforme
        yield self.env.timeout(tiempo_corte)  # dejar correr el tiempo n minutos
        print("Corte listo a %s en %.2f minutos" % (cliente, tiempo_corte))
        self.dt += tiempo_corte  # acumular tiempo de uso de la instalación

    def cliente(self, name):
        """Simula la llegada y el proceso del cliente en la peluquería."""
        llega = self.env.now  # guarda el minuto de llegada del cliente
        print("--> %s llegó a la peluquería en el minuto %.2f" % (name, llega))
        with self.personal.request() as request:  # espera turno
            yield request  # obtener turno
            pasa = self.env.now
            espera = pasa - llega  # acumulo tiempo de espera
            self.te += espera  # acumulo tiempo de espera
            print("%s pasa y espera en la peluquería en el minuto %.2f habiendo esperado %.2f" % (name, pasa, espera))
            yield self.env.process(self.cortar(name))  # llamar al proceso cortar
            deja = self.env.now  # momento en que el cliente deja la peluquería
            print("<-- %s deja la peluquería en minuto %.2f" % (name, deja))
            self.fin = deja  # guardo el minuto en que termina

    def principal(self):
        """Simula la llegada de clientes a la peluquería."""
        for i in range(1, self.tot_clientes + 1):
            R = random.random()
            llegada = -self.t_llegadas * math.log(R)
            yield self.env.timeout(llegada)  # dejo transcurrir un tiempo entre un cliente y otro
            self.env.process(self.cliente('cliente %d' % i))

    def ejecutar(self):
        """Inicia la simulación."""
        print("--- Simulación Peluquería ---")
        random.seed(self.semilla)
        self.env.process(self.principal())
        self.env.run()
        self.mostrar_resultados()

    def mostrar_resultados(self):
        """Muestra los indicadores obtenidos de la simulación."""
        print("Indicadores obtenidos")
        print("")
        lpc = self.te / self.fin
        print("Longitud promedio de la cola: %.2f" % lpc)
        tep = self.te / self.tot_clientes
        print("Tiempo de espera promedio: %.2f" % tep)
        upi = (self.dt / self.fin) / self.num_peluqueros
        print("Uso promedio de la instalación: %.2f" % upi)

