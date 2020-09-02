import json
import os
import pandas as pd

class Curso():
    def __init__(self,json_path):
        self.__disciplinas = self.load_disciplinas(json_path)
        self.nome = os.path.splitext(os.path.basename(json_path))[0]

    def get_disciplinas(self):
        return [d.get_dict() for d in self.__disciplinas]

    def load_disciplinas(self,json_path,name=None):
        if(name==None):
            name = os.path.splitext(os.path.basename(json_path))[0]
        with open(json_path,'r') as json_file:
            dicts = json.load(json_file)
            for i in dicts:
                i['curso'] = name
            disc = [Disciplina(i)for i in dicts]     
        return disc

    def calc_cr(self):
        pass


class Disciplina():
    def __init__(self,materia):
        '''
        "ano":2015,"codigo":"BCS0001-13","situacao":"Aprovado","categoria":"Obrigatória","creditos":3,"periodo":"2","disciplina":"Base Experimental das Ciências Naturais","conceito":"A"
        '''
        self.__curso = materia['curso']
        self.__ano = materia["ano"]
        self.__quadrimestre = materia["periodo"]
        self.__codigo = materia["codigo"]
        self.__situacao = materia["situacao"]
        self.__categoria = materia["categoria"]
        self.__creditos = materia["creditos"]
        self.__disciplina = materia["disciplina"]
        self.__conceito = materia["conceito"]
        self.__dict = materia

    def get_dict(self):
        return self.__dict

class Aluno():
    def __init__(self,json_path="./data/ufabc/eiar.json"):
        self.__curso = Curso(json_path)
        self.__materias = self.__curso.get_disciplinas()
    
    def resumo_csv(self,file=None):
        if(file==None):
            file = os.path.normpath(os.path.join(os.path.dirname(__file__),"../csv",self.__curso.nome+".csv"))
            if(not(os.path.isdir(os.path.dirname(file)))):
                os.makedirs(os.path.dirname(file))
        df = pd.DataFrame(self.__materias)
        df.to_csv(file)

class UFABC():
    def __init__(self):
        self.__cursos = ""
