import pymongo
import pymongo.errors
def consultar_todos_dados():
 try:        
    client = pymongo.MongoClient("mongodb+srv://guilhermo4t2l:Gui123@cluster.ue6fo.mongodb.net/")
    banco= client["Jogos"]
    collection = banco ["JogosparaVenda"]
    
    resultados = collection.find()

    resultado_lista = list(resultados)

    print("O resultado é: ",resultado_lista)

   
     
     
 except pymongo.errors as e:
    print('Vixe acabou dando erro aí em', e)

   
   





 