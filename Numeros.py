
#Función cálculo números pares
def pares(n):
   print ("Pimeros ",n," números pares:")
   for i in range(0,(n*2),2):
      print (i)

#Función cálculo números impares
def impares(n):
   print ("Primeros ",n,"números impares:")
   for i in range(1,(n*2),2):
      print (i)

#Función cálculo números primos
def primos(n):
   print ("Primeros ",n,"números primos:")
   contador=0
   primos=0
   while (primos < n):
      if (es_primo(contador)):
            print(contador)
            primos=primos+1
      contador=contador+1

#Función es primo
def es_primo(num):
   if num < 2:
      return False
   for i in range(2, num):
      if num % i == 0:
            return False
   return True

#Funcón principal
def main():
   print("La siguiente aplicación calcula los primeros n números pares, impares y primos. \nPor favor a continuación ingrese un número cualquiera.")
   n = int(input("Ingrese el número n: "))
   if (n > 0):
      pares(n)
      impares(n)
      primos(n)

if __name__ == "__main__":
   main()


