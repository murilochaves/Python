#coding: utf-8

from semestre import Semestre
#from disciplina import
import datetime
from dataPersonalizada import *
## yyyy/mm/dd

def main():
    
    # SEMESTRE
    referencia = '2017/2'
    inicio_semestre_8 = set_data(27, 7, 2017)
    final_semestre_8 = set_data(14, 12, 2017)
    semestre_8 = Semestre('Oitavo Período', referencia, inicio_semestre_8, final_semestre_8)

    # MATERIAS
    

    
if __name__ == "__main__":
    main()