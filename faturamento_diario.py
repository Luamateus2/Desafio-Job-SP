import json

# Carregar o vetor do arquivo JSON
with open("dados.json", "r") as json_file:
    dados_faturamento = json.load(json_file)

# Calcular menor e maior valor de faturamento diário
menor_valor = min(item["valor"] for item in dados_faturamento)
maior_valor = max(item["valor"] for item in dados_faturamento)

# Calcular média mensal desconsiderando dias sem faturamento
valores_faturamento = [item["valor"] for item in dados_faturamento if item["valor"] > 0]
media_mensal = sum(valores_faturamento) / len(valores_faturamento)

# Calcular o número de dias em que o faturamento foi superior à média mensal
dias_acima_media = sum(1 for item in dados_faturamento if item["valor"] > media_mensal)

# Imprimir os resultados
print(f"Menor valor de faturamento diário: {menor_valor}")
print(f"Maior valor de faturamento diário: {maior_valor}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
