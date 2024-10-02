import json

with open("dados.json", "r") as json_file:
    dados_faturamento = json.load(json_file)

valores_faturamento = [item["valor"] for item in dados_faturamento if item["valor"] > 0]

menor_valor = min(valores_faturamento)
maior_valor = max(valores_faturamento)

media_mensal = sum(valores_faturamento) / len(valores_faturamento)

dias_acima_media = sum(1 for item in dados_faturamento if item["valor"] > media_mensal)

print(f"Menor valor de faturamento diário: {menor_valor:.2f}")
print(f"Maior valor de faturamento diário: {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
