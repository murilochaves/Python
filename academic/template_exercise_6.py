# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):

    """
    Função para pegar o gênero mais popular
    Argumentos:
        data_list: lista com todos os dados do dataset.
    Retorna:
        Retorna o gênero mais popular como string.

    """

    male, female = count_gender(data_list)

    if male > female:
        answer = 'Male'
    elif female > male: 
        answer = 'Female'
    else:
        answer = 'Equal'

    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------