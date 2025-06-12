import requests

def converter_moeda(origem, destino, valor):
    url = f"https://api.exchangerate.host/convert?from={origem}&to={destino}&amount={valor}"
    resposta = requests.get(url)
    dados = resposta.json()
    return dados["result"]

print("=== Conversor de Moedas ===")
moeda_origem = input("Digite a moeda de origem (ex: USD): ").upper()
moeda_destino = input("Digite a moeda de destino (ex: BRL): ").upper()
valor = float(input("Digite o valor a ser convertido: "))

resultado = converter_moeda(moeda_origem, moeda_destino, valor)
print(f"{valor} {moeda_origem} = {resultado:.2f} {moeda_destino}")
