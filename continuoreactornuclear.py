import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class ReactorNuclear:
    def __init__(self, Q_gen, k, T_cool, C, T0):
        self.Q_gen = Q_gen  # Tasa de generación de calor en vatios (W)
        self.k = k  # Coeficiente de enfriamiento en W/°C
        self.T_cool = T_cool  # Temperatura del sistema de enfriamiento en grados Celsius (°C)
        self.C = C  # Capacidad térmica del reactor (J/°C)
        self.T0 = T0  # Temperatura inicial del reactor (°C)
        self.tiempo = np.linspace(0, 200, 1000)  # Tiempo de simulación (0 a 200 minutos)
        self.solucion = None

    def modelo(self, T, t):
        """Ecuación diferencial para la variación de la temperatura."""
        dT_dt = (self.Q_gen / self.C) - self.k * (T - self.T_cool)
        return dT_dt

    def resolver(self):
        """Resuelve la ecuación diferencial."""
        self.solucion = odeint(self.modelo, self.T0, self.tiempo)

    def graficar(self):
        """Grafica los resultados de la temperatura del reactor a lo largo del tiempo."""
        if self.solucion is None:
            raise ValueError("La solución no ha sido calculada. Llama al método 'resolver()' primero.")
        
        plt.figure(figsize=(10, 5))
        plt.plot(self.tiempo, self.solucion, label='Temperatura del Reactor')
        plt.axhline(self.T_cool, color='red', linestyle='--', label='Temperatura del Sistema de Enfriamiento')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Temperatura (°C)')
        plt.title('Enfriamiento del Reactor Nuclear')
        plt.grid(True)
        plt.legend()
        plt.show()


