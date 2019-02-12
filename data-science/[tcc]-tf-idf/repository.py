import os


class Repository:
    """
    Esta classe possui o objetivo de abstrarir o diretório, que será
    um objeto à ser acessado posteriormente.
    """

    # construtor padrão da classe
    def __init__(self, path):
        """
        Construtor padrão da classe Repository.
        Arg:
            path = diretório absoluto do sitio de documentos.
        Out:
            Não há.
        """
        # diretório do path do repositório
        self.path = path
        # nome de todos os arquivos presentes no repositório
        self.listdir = os.listdir(path)

    # GETTERS
    def get_directory_path(self):
        """
        GET: Retorna uma STRING com o caminho do diretório do objeto.
        """
        return self.path

    def get_listdir(self):
        """
        GET: Retorna uma LISTA de STRINGS com o nome de todos os arquivos
             presentes no diretório do objeto.
        """
        return self.listdir

    # SETTERS
    def set_path(self, path):
        """
        SET: Setar uma STRING com o caminho do diretório do objeto.
        """
        self.path = path

    def set_listdir(self, path):
        """
        SET: Setar a LISTA de STRINGS com o nome de todos os arquivos
             presentes no diretório do objeto.
        """
        self.listdir = os.listdir(path)

    # METHODS
    def clear_repository(self):
        """
        Esta função possui como objetivo limpar todos os arquivos que
        não são respectivamente um arquivo .txt.
        Out:
            Não há.
        """

        # definindo as variáveis de escopo
        # referente ao nome dos arquivos que serão removidos do diretório
        list_for_delete = []

        # laço de repetição para verificar se todos os arquivos são um .txt
        for element in self.get_listdir():
            if '.txt' not in str(element):
                list_for_delete.append(element)

        # removendo tudo que não seja um .txt
        for element in list_for_delete:
            os.remove(str(self.path + '/' + element))
            print('File {0} Removed!'.format())

if __name__ == "__main__":
    meiobit = Repository('/Users/murilochaves/Documents/GitHub/Python/data-science/[tcc]-tf-idf/source_data/Meio Bit')

    print(len(meiobit.get_listdir()))
    print(type(meiobit.get_listdir()))

    #print(meiobit.get_listdir())

    meiobit.clear_repository()

    for element in meiobit.get_listdir():
        if '.txt' not in str(element):
            print(element)
