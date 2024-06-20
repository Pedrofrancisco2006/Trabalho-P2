idade = int(input('Qual a sua idade: '))
nasc = input("Qual a sua nascionalidade: ")
experiencia = float(input("Quantos aanos de experiencia? (Apenas numeros): "))
if idade <= 0:
    print("Coloque uma idade correta")
elif idade >= 18 and experiencia >=2:
    if nasc == 'brasileira' or 'BR' or 'br':
        print("Você está elegivel")    
else :
    print("Você não está elegivel")        