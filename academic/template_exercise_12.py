# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):

    """
    Função para contar tipos de usuário sem definir um tipo em específico.
    Argumentos:
        column_list: lista com os registros de user_types.
    Retorna:
        Duas listas:
            1. Lista com os tipos de usuário presente no dataset.
            2. Lista com a contagem respectiva dos tipos de usuário presentes no dataset.

    """

    item_types = []
    count_items = []

    for user_types in set(column_list):
        item_types.append(user_types)
        count_items.append(column_list.count(user_types))

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------