##Funciones
def greet(name):
  print ("Hello", name)

greet("Joel Sanmiguel")

##Funcion Promedio
def average(list_num):
  sum_num = 0
  for i in list_num:
    sum_num += i
  return sum_num / len(list_num)

average([100,200,150,100,200])

##Funcion para Imprimir Usuario
people = [
    {
      'name': 'Wilson',
      'age': '34',
      'profession': 'Ingeniero de Sistemas',
    }, {
      'name': 'Jesica Amortegui',
      'age': '24',
      'profession': 'Contadora',
    }, {
      'name': 'Yeferson Capacho',
      'age': '33',
      'profession': 'Ingeniero Industrial',
    }, {
      'name': 'Jobanna Gonzales',
      'age': '44',
      'profession': 'Abogada',
    }
]

def presentation(person):
  return 'Hola mi nombre es: {name}, tengo {age} años, y soy {profession}'.format(
      name=person["name"],
      profession=person['profession'],
      age=person['age'],
  )

def presentations(people):
  for person in people:
    print(presentation(person))

presentations(people)

##Clases
class Address():
  def __init__(self, street=None, town=None, city=None):
    self.street = street
    self.town = town
    self.city = city
  
  def get_full_address(self):
    return '{} {} {}'.format(self.street, self.town, self.city)

class Person():
  def __init__(self, first_name=None, last_name=None, age=None, id=None, address=None):  
    self.first_name = first_name  
    self.last_name = last_name  
    self.age = age  
    self.id = id  
    self.address = address

  def set_first_name(self, first_name):
    self.first_name = first_name  

  def set_last_name(self, last_name):
    self.last_name = last_name  

  def set_age(self, age):
    self.age = age  

  def set_id(self, id):
    self.id = id  

  def set_address(self, address):
    self.address = address 

  def get_full_name(self):
    return '{} {}'.format(self.first_name, self.last_name)

  def greet(self):
    return 'Hola mi nombre es: {full_name}, tengo {age} años, y mi numero id es: {id}'.format(
        full_name= self.get_full_name(),
        id=self.id,
        age=self.age,
    )

  def greet_address(self):
    return self.greet() + ' mi direccion es: {}'.format(self.address.get_full_address())

address = Address("CR 23 # 23 67", "Quinta Granada", "Floridablanca")
person = Person("Jesica","Lima",24,1098,address)
person.greet_address()

##Decoradores
def prevent_error(f):
    def wrapper(*args, **kwargs):
        try:
          f(*args, **kwargs)
        except ZeroDivisionError: 
          print('Error, division por cero')
        except ValueError:
          print('Error, ha ingresado valores no numericos')
        except IndexError:
          print("Esta tratando de acceder a un indice no existente")
        except KeyError:
          print("Esta tratando de acceder a un atributo no existente")
    return wrapper


@prevent_error
def dummy_code(nota_1, nota_2):
  prom = int(nota_1) + int(nota_2) / int(nota_2)
  print(prom)

dummy_code(100, "a")
dummy_code(40, 0)
dummy_code(50, 20)

user = { "name": "Wilson"}

@prevent_error
def get_user(user):
  print("Nombre: ",user['nme'])

get_user(user)

pares = [2,4,6,8,10]

@prevent_error
def get_item(pares,index):
  print("Item: ",pares[index])

get_item(pares,4)
get_item(pares,10)