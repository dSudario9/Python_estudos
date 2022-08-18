#nome  = input("Digite seu Nome   ")

#print(nome+ " " +"Seja bem vindo ")

# Verificação de valor 
#a=input("primeiro_valor") 
#b=input("segundo_valor") 

#if a > b :
 # print("primeiro_valor é maior")  
#else: 
    #print("segundo_valor é maior")

  ########################################

#Numeros Fatorias

#var =int(input("Valor"+" "))
#if var < 0:
 # print("Digite apenas numeros Positivos")
#fat = 1
#for i in 1, var:
 # fat= fat * var
 # print(fat)

# Soma de uma Lista 

#lista = [15,46,75,34,23]
#soma = (sum(lista))
#print(soma)

#2º Opção 
#Somando  valor da lista com valor anterior

#lista = [15,46,75,34,23]
#total = 0
#for lista in lista:
  #soma = total + lista
  #print(soma)
###################################################
  # Chute o numero 

#valor = input("valor aleatorio entre 1 e 10 ")

#chute = input("chute do usuario"+" ")

#if chute != valor:
  #print ("Chute invalido")
  

#elif chute > valor:
   
    #print("Chute é maior")
 
#elif chute < valor:
   
   
   #print("Chute é menor")


#elif chute == valor:
  
   
   #print("acertou o chute")



    #################################
#Outra forma  usando ELIF 
#var = input("Digite um numero entre 1 e 10"+ " ")
#chute = input("Chute um numero "+ " ")

#if chute == var:
   # print("acertou ")
#elif chute < var:
   # print(" Numero é menor")
#else:
    #print("É maior que numero Digitado")


# Usando if com for :

#ordens = ["2003455","30099445","4005666","3009456","4005643","200456"]
#for ordens in ordens:
 #if ordens[0] == "2":
   # print(f"A {ordens}  É Manutenção Corretiva")
 #elif ordens[0] == "3":
   # print(f"A {ordens}  É Manutenção Preditiva")
#else:
   # print(f"A {ordens}  É Manutenção  corretiva")

# Salrio mensal 
#salario= input("Salario mensal"+ " ")
#hrs = input("Horas trabalhadas"+ " ")
#valor = int(salario) / int(hrs)
#print(valor)

# if - elif - else
#x = 4
#if x > 8 :
 #print(" Maior que X")
#elif x == 4:
  #print(" Valor igual ")
#else:
 # print(" Valor invalido")

# Laço de repetição 

#Repetindo palavras e numeros
#for palavra in  range(1,4):
 #print("Carregando")

#for item in  range(100):
 #print(1)

#indice 
#for indice in range(1,21):
  #print(indice)

#for item in range(1,21,2):
   # print(item)

# Percorrendo listas em for 

#nomes = ("Dorian","Sudario","da Silva")
#for nome in nomes:
  #print(nome)

#INDICES

#precos = [23.50 , 40.00 , 55,00]
#print(precos[0])

#print(f"Indice",precos.index(23.50),f"valor",precos[0])


###################### VELOCIDADE 

velocidade =int(input("velocidade  "))
max= 80 

if velocidade <= max:
   print("Não levou multa")
elif velocidade > max and velocidade <= max + 10:
 print("Levou multa leve")
elif velocidade > max + 11 and velocidade <= max + 20:
  print("Levou Multa grave")
else:
  print("Levou Multa  Gravissima")

  #Final Curso de Logica de programação 



  



  




