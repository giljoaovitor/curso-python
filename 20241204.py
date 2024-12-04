#coding utf-8

'''
def Info_computador():
    marca = input("Digite a marca do computador: ")
    memoria = input("Digite a quantidade de memória: ")
    placaV = input("Digite a placa de vídeo:")
    print("Seu computador é da marca: ", marca)
    print("Seu computador tem ", memoria ,"RAM de memória.")
    print("Seu computador tem a placa de vídeo",placaV)
Info_computador()
'''

'''
#função setter
def set_computador():
    marca = input("Digite a marca do computador: ")
    memoria = input("Digite a quantidade de memória: ")
    placaV = input("Digite a placa de vídeo: ")
    return marca, memoria, placaV

#função getter
def get_computador(marca, memoria, placaV):
    print("Seu computador é da marca: ", marca)
    print("Seu computador tem memória: ", memoria)
    print("Seu computador tem placa de video: ", placaV)

marca, memo, placaV = set_computador()
get_computador(marca, memo, placaV)
'''

'''
class computador():
    marca = ''
    preco = ''
    placaV = ''
    
Comp1 = computador()
Comp1.marca = "Daten"
Comp1.preco = "R$ 2000,00"
Comp1.placaV = "NVIDIA"

print("Detalhes do computador 1")
print(Comp1.marca)
print(Comp1.preco)
print(Comp1.placaV)
'''

# class Computador(object): #Informo ao dev que vou colocar métodos.
#     def __init__(self):
#         self.marca = ''
#         self.preco = ''
#         self.placaV = ''
#     def set_comp(self):
#         self.marca = input("Digite a marca do computador:")
#         self.preco = input("Digite o preço do computador:")
#         self.placaV = input("Digite a placa de video do computador:")
#         self.processador = input("Digite o processador:")
#     def get_comp(self):
#         print("Marca = ",self.marca)
#         print("Processador = ", self.processador)

# if __name__=="__main__":
#     Comp1 = Computador()
#     Comp1.set_comp()
#     Comp1.get_comp() NÃO FAZER ASSIM

