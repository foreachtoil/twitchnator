import boto3
import os

def get_ssm_parameter(name):
    print("Buscando el SSM Parameter")
    aws_profile_name = os.getenv('PERFIL_AWS') # os.getenv -->
    if not aws_profile_name:
        return "No encontré el perfil de AWS"
    else:
        print(f"Usando el perfil: {aws_profile_name}")

    session = boto3.Session(profile_name=aws_profile_name)
    client = session.client('ssm')
    print(f"Buscando el parámetro {name}")
    response = client.get_parameters(
        Names=[
            name
        ],
        WithDecryption=True
    )
    if len(response['Parameters']) == 1:
        secret_value = response['Parameters'][0]['Value']
    else:
        secret_value = f"Se encontraron {len(response['Parameters'])} cantidad de parámetros"
    print(f"Encontré el parámetro {name}")
    return secret_value