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

def read_file(name_file):
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