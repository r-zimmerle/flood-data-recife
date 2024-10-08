import pandas as pd
from geopy.geocoders import GoogleV3
from time import sleep

# Carregar a chave da API a partir do arquivo geocoding-api.txt
with open('config/geocoding-api.txt', 'r') as file:
    google_api_key = file.read().strip()

# Inicializar o geocoder GoogleV3 com a chave da API
geolocator = GoogleV3(api_key=google_api_key)

# Carregar o arquivo CSV com os endereços
df = pd.read_csv('output/alagamentos_confirmados.csv')

# Função para buscar a latitude e longitude com base no endereço
def get_coordinates(address):
    try:
        full_address = f"{address}, Recife, Pernambuco, Brasil"
        location = geolocator.geocode(full_address)
        if location:
            return pd.Series([location.latitude, location.longitude])
        else:
            return pd.Series([None, None])
    except Exception as e:
        print(f"Erro ao buscar coordenadas para o endereço {address}: {e}")
        return pd.Series([None, None])

# Aplicar a função para cada endereço e criar duas novas colunas com latitude e longitude
df[['latitude', 'longitude']] = df['solicitacao_endereco'].apply(get_coordinates)

# Salvar o resultado em um novo CSV com as coordenadas
df.to_csv('output/alagamentos_com_coordenadas.csv', index=False)

print("Arquivo CSV com coordenadas foi criado com sucesso!")
