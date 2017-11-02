#coding: utf-8

from semestre import Semestre
from disciplina import
import datetime
## yyyy/mm/dd

def main():
    # SEMESTRE
    referencia = '2017/2'
    inicio_semestre_8 = datetime.date(2017, 7, 27)
    final_semestre_8 = datetime.date(2017, 12, 14)
    semestre_8 = Semestre('Oitavo Período', referencia, inicio_semestre_8, final_semestre_8)

    # MATERIAS

    
if __name__ == "__main__":
    main()