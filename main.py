
def leer_poema(archivo):
  fichero = open(archivo, 'r')
  texto = fichero.readlines()
  fichero.close()
  poema = [t.replace('\n'," ") for t in texto]
  return "".join(poema)

def sustitucion(texto):
  dic = dict(zip('jJhHñÑkKuUwWyYxX','iIiInNlLvVvVzZrR'))
  poema = [t if t not in dic.keys() else dic[t] for t in texto]
  return ''.join(poema)

def eliminar_tildes(texto):
  tildes = dict(zip("áÁéÉíÍóÓúÚ","aAeEiIoOuU"))
  poema = [t if t not in tildes.keys() else tildes[t] for t in texto]
  return ''.join(poema)

def mayuscula(texto):
  return texto.upper()

def eliminar_signos(texto):
  signos =" .,;:¡!¿?()[]\"\'_/*¨"
  poema =  [ t for t in texto if t not in signos]
  return "".join(poema)

def frecuencias(texto):
  dic = dict.fromkeys('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ',0)
  for t in texto:
    if t in dic.keys():
      dic[t] += 1
  dic=sorted(dic.items(), key=lambda x: x[1], reverse=True)
  print(dic)

def metodo_Kasisky(texto):
  cadena =" "
  triada = [texto[s:s+4] for s  in range(len(texto)-3)]
  for index in range(len(triada) -1):
    valor = triada[index]
    if valor  in triada[index+4:]:
      cadena += f"({valor} : {triada[index+4:].index(valor)+3}) "
  return cadena

def unicode(texto):
 cadena = " ".join(f"{ord(c):x}" for c in texto)
 return str(cadena)

def procesar(texto):
  dic = dict(zip('ecf3','KLM8'))
  poema = [t if t not in dic.keys() else dic[t] for t in texto]
  return ''.join(poema)

def insert_mani(texto):
  cadenas = []
  i = 0
  while i < len(texto):
    cadenas.append(texto[i:i+20])
    i += 20
  cadenas=[i+"MANI" if len(i) == 20 else i for i in cadenas]
  poema = "".join(cadenas)

  if len(poema) % 4 != 0:
    for j in range(4 - (len(poema) % 4)):
      poema += "M"
  return poema

def main():
  poema = leer_poema('poema.txt')
  poema = sustitucion(poema)
  poema = eliminar_tildes(poema)
  poema = mayuscula(poema)
  poema = eliminar_signos(poema)
  P = metodo_Kasisky(poema)
  print(P)

  
if __name__ == "__main__":
  main()

def guardar(texto):
  archivo = open('POEMA_PRE.txt', 'w')
  archivo.write(texto)
  archivo.close()

def retornar_alfabeto(texto):
  dic = dict()
  for s in texto:
    if s in dic.keys():
      dic[s] += 1
    else:
      dic[s] = 0
  return (dic.keys() , sum(dic.values()))
  



  


