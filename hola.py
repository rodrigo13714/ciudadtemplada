import pandas as pd
from geopy.distance import great_circle

# Cargar el archivo CSV
df = pd.read_csv('worldcities.csv')

# Función para obtener las coordenadas de una ciudad
def get_coordinates(city_name):
    city = df[df['city_ascii'] == city_name]
    if not city.empty:
        return city.iloc[0]['lat'], city.iloc[0]['lng']
    else:
        return None

# Función para calcular la distancia entre dos ciudades
def calculate_distance(city1, city2):
    coords_1 = get_coordinates(city1)
    coords_2 = get_coordinates(city2)
    
    if coords_1 and coords_2:
        distance = great_circle(coords_1, coords_2).kilometers
        return distance
    else:
        return None

# Ejemplo de uso
city1 = "New York"
city2 = "Los Angeles"
distance = calculate_distance(city1, city2)

if distance:
    print(f"La distancia entre {city1} y {city2} es de {distance:.2f} kilómetros.")
else:
    print("Una o ambas ciudades no se encontraron en el archivo CSV.")
