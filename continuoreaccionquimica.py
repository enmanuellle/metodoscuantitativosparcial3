import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class ReaccionPrimeraOrden:
    def __init__(self, k, A0):
        self.k = k  # Constante de velocidad de la reacción (1/min)
        self.A0 = A0  # Concentración inicial de A (mol/L)
        self.tiempo = np.linspace(0, 50, 1000)  # Tiempo de simulación (0 a 50 minutos, con 1000 puntos)
        self.solucion = None

    def modelo(self, A, t):
        """Ecuación diferencial para la concentración de A."""
        dA_dt = -self.k * A
        return dA_dt

    def resolver(self):
        """Resuelve la ecuación diferencial."""
        self.solucion = odeint(self.modelo, self.A0, self.tiempo)

    def graficar(self):
        """Grafica los resultados de la concentración de A a lo largo del tiempo."""
        if self.solucion is None:
            raise ValueError("La solución no ha sido calculada. Llama al método 'resolver()' primero.")
        
        plt.figure(figsize=(10, 5))
        plt.plot(self.tiempo, self.solucion, label='Concentración de [A]')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Concentración (mol/L)')
        plt.title('Descomposición de un Reactivo de Primer Orden')
        plt.grid(True)
        plt.legend()
        plt.show()

