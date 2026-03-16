import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from rich.pretty import pprint  # para mostrar con colorines

load_dotenv()

# Leer variables de entorno
OPEN_AI_ENDPOINT = os.getenv("OPEN_AI_ENDPOINT")
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

# Nombre del deployment que creaste en Azure
DEPLOYMENT = os.getenv("DEPLOYMENT")
API_VERSION = os.getenv("API_VERSION")


client = AzureOpenAI(
    api_key=OPEN_AI_API_KEY,
    azure_endpoint=OPEN_AI_ENDPOINT,
    api_version=API_VERSION
)

response = client.chat.completions.create(
    model=DEPLOYMENT,
    messages=[
        {"role": "user", "content": "Di hola en una frase corta"}
    ]
)

pprint(response)
# print(response.choices[0].message.content)
