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

# Función para calcular la distancia total entre tres ciudades
def calculate_total_distance(city1, city2, city3):
    distance1 = calculate_distance(city1, city2)
    distance2 = calculate_distance(city2, city3)
    
    if distance1 is not None and distance2 is not None:
        total_distance = distance1 + distance2
        return total_distance
    else:
        return None

# Ejemplo de uso
city1 = "New York"
city2 = "Chicago"
city3 = "Los Angeles"
total_distance = calculate_total_distance(city1, city2, city3)

if total_distance:
    print(f"La distancia total entre {city1}, {city2} y {city3} es de {total_distance:.2f} kilómetros.")
else:
    print("Una o más ciudades no se encontraron en el archivo CSV.")
