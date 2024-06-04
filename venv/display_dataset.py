import pandas as pd
import matplotlib.pyplot as plt

# Cargar el nuevo archivo CSV de las principales causales de quejas de acueducto 2020
datosQuejas = pd.read_csv('principalesQuejasAcueducto.csv')

# Crear la gráfica de barras
plt.figure(figsize=(10, 8))  # Ajustar el tamaño de la figura
plt.barh(datosQuejas['Causal'], datosQuejas['Cantidad de reclamos'], color='skyblue')
plt.xlabel('Cantidad de reclamos')
plt.ylabel('Causal')
plt.title('Reclamos por causal en 2020 - Acueducto')
plt.grid(axis='x')

# Aumentar el espacio entre las barras para dar más espacio al texto
plt.tight_layout()

# Mostrar la gráfica
plt.show()




# Leer el archivo CSV de las principales reclamaciones y recursos de acueducto 2020
datosReclamaciones = pd.read_csv('principalesReclamacionesAcueducto.csv')

# Crear la gráfica de barras
plt.figure(figsize=(10, 8))  # Ajustar el tamaño de la figura
plt.barh(datosReclamaciones['Causal'], datosReclamaciones['Cantidad de reclamos'], color='skyblue')
plt.xlabel('Cantidad de reclamos')
plt.ylabel('Causal')
plt.title('Reclamos por causal en 2020 - Reclamaciones Acueducto')
plt.grid(axis='x')

# Aumentar el espacio entre las barras para dar más espacio al texto
plt.tight_layout()

# Mostrar la gráfica
plt.show()




# Cargar el nuevo archivo CSV de los principales causales reclamaciones y recursos de alcantarillado 2020
datosReclamacionesAlcant = pd.read_csv('principalesReclamacionesAlcantarillado.csv')

# Crear la gráfica de barras
plt.figure(figsize=(10, 8))  # Ajustar el tamaño de la figura
plt.barh(datosReclamacionesAlcant['Causal'], datosReclamacionesAlcant['Cantidad de reclamos'], color='blue')
plt.xlabel('Cantidad de reclamos')
plt.ylabel('Causal')
plt.title('Reclamos por causal en 2020 - Alcantarillado')
plt.grid(axis='x')

# Aumentar el espacio entre las barras para dar más espacio al texto
plt.tight_layout()

# Mostrar la gráfica
plt.show()
