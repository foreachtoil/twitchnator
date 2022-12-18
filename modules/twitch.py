import requests

from modules.aws import get_ssm_parameter

print("Buscando Client ID & Client Secret")
client_id = get_ssm_parameter('/twitch/client_id')
client_secret = get_ssm_parameter('/twitch/client_secret')
print("Client ID & Client Secret seteado")

# POST request al endpoint de Twitch con ciertos datos y headers para setear la configuración de lo que estamos mandando
def get_twitch_token():
    print("Función get_twitch_token")
    twitch_endpoint = 'https://id.twitch.tv/oauth2/token'

    payload=f'client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {client_secret}'
    }
    print("Solicitando Bearer Token a Twitch")
    response = requests.request('POST', twitch_endpoint, headers=headers, data=payload)
    print("Conseguí el Bearer Token de Twitch")
    return response.json()['access_token']

def get_twitch_user(user):
    if not user:
        return {}
    twitch_endpoint = f'https://api.twitch.tv/helix/users?login={user}'

    payload = {}

    headers = {
        'Client-Id': client_id,
        'Authorization': f'Bearer {get_twitch_token()}'
    }

    print("Pidiéndole a Twitch los datos de ForEachToil")
    response = requests.request('GET', twitch_endpoint, headers=headers, data=payload)
    print("Los datos de ForEachToil son:")
    return response.json()