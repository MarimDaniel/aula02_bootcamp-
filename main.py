try:
   temperatura_em_celsios = float(input("digite a temperatura Cº: "))
   celsios_conversao_fahrenheit = (temperatura_em_celsios * 1.8 + 32)
   print(f"{temperatura_em_celsios}°C é igual a {celsios_conversao_fahrenheit}°F")
except ValueError:
   print("O valor digitado não pode ser convertido")

