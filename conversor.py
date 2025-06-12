import requests

print("=== Conversor de Moedas ===")

moeda_origem = input("Moeda de origem (ex: USD): ").upper()
moeda_destino = input("Moeda de destino (ex: BRL): ").upper()
valor = float(input("Valor a ser convertido: "))

url = f"https://api.exchangerate.host/convert?from={moeda_origem}&to={moeda_destino}&amount={valor}"
resposta = requests.get(url)
dados = resposta.json()

resultado = dados["result"]

print(f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")
