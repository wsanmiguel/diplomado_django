from datetime import date, time, datetime

def get_integer(m):
  while True:
    try:
      num = int(input(m))
      return num
    except:
      print("Valor no válido, debe ingresar sólo números enteros")

def get_float(m):
  while True:
    try:
      num = float(input(m))
      return num
    except:
      print("Valor no válido, debe ingresar sólo números float")

def get_date(m):
  while True:
    try:
      day = get_integer("Día: ")
      month = get_integer("Mes: ")
      year = get_integer("Año: ")
      new_date = date(year, month, day)
      return new_date.strftime('%d/%m/%Y')
    except:
      print("!Valor no válido¡, por favor Intente de nuevo")

def get_today(m):
  return date.today().strftime('%d/%m/%Y')

def get_time(m):
  while True:
    try:
      hour = get_integer("Hora: ")
      minut = get_integer("Minuto: ")
      new_time = time(hour, minut, 0)
      return new_time.strftime('%H:%M')
    except:
      print("!Valor no válido¡, por favor Intente de nuevo")

def read_file(name_file):
  #print(name_file)
  file_ = open(name_file)
  content = file_.read()
  lines = content.splitlines()
  file_.close()
  return lines

def save_file(name_file, line):
  file_ = open(name_file, "a")
  file_.write(line)
  file_.close()
  print("Guardado Correctamente")

def save_lines(name_file, lines):
  file_ = open(name_file, "w")
  for line in lines:
    file_.write(line)
  file_.close()
  print("Guardado Correctamente")

##Funcion Promedio
def average(list_num):
  if len(list_num) > 0 :
    sum_num = 0
    for i in list_num:
      try:
        sum_num += float(i)
      except:
        print("Error en número: "+i)
    return round((sum_num / len(list_num)),2)
  else:
    return 0