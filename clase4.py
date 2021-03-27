#Ejercicio de Condicionales
age = 15
gender = "M"
if (age >= 18 and gender == "F") or (gender=="M" and age >= 18):
  print("Acceso Concedido")
elif gender == "F" and age < 18:
  print("Acceso 2")
else:
  print("Acceso restringido")

print("\n\n")
#Ejercicio de Ciclo For
list_pares = [2,4,6,8,10]

for i in list_pares:
  print(i)

for i in range(len(list_pares)):
  print(i,": ",list_pares[i])

dictionary_user = {'id': 123456, 'name': 'Joel David Sanmiguel', 'phone': '3102001547', 'address': 'CLL 1N # 20- 04 P3'}

for key,value in dictionary_user.items():
  print(key,": ",value)

for key in dictionary_user.keys():
  print(key,": ",dictionary_user[key])

for value in dictionary_user.values():
  print(value)

print("\n\n")
#Ejercicio
#Definir un diccionario con la lista de precios de productos de una tienda y su respectivo valor, Ejemplo
#  lista_compra = {'huevos': 300, 'pan' : 200, 'queso': 500, ...}
#imagina que debes preparar una deliciosa comida y quiere saber cuanto te cuesta preparalo con el valor de los ingredientes.
#define una lista y calcula el valor total a pagar por esa comida.
products = {
    'leche': 2500,
    'arroz': 2500,
    'huevo': 250,
    'queso': 400,
    'carne': 7000,
    'pasta': 2500,
    'cebolla': 1200,
    'tomate': 800,
    'ajo': 500,
    'sal': 500,
    'pimienta': 1500,
    'recipiente_aluminio': 800
}
list_food = {'queso':3, 'carne': 1, 'pasta':1, 'cebolla': 1, 
             'tomate': 1, 'ajo': 1, 'sal': 1, 'pimienta': 1, 
             'recipiente_aluminio':2}
total = 0
for key,value in list_food.items():
  total += products[key] * value
print("El valor Total de la Comida es: ",total)