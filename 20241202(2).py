#coding utf-8

#Dicionario nativo de python, ou outra estrutura
comp1 = {"marca":"Dell",
    "preço":7000
    }
comp2 = {"marca":"Pichau",
    "preço":8000
    }
#Juntando em uma lista os dois dicionarios
lista_comp = [comp1, comp2]
#Cria arquivo paa gravação
nome_arquivo = "Comp.json"
Arql = open(nome_arquivo, "w", encoding = 'utf-8')
json.dump(lista_comp, Arql) #Codifica no formato Json e grava no arquivo.
Arql.close()