def inverter_string(original):
    invertida = ""
    for caractere in original:
        invertida = caractere + invertida
    return invertida

# String a ser invertida
string_informada = input("Informe uma string para ser invertida: ")

string_invertida = inverter_string(string_informada)

print(f"A string invertida é: {string_invertida}")