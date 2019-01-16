# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_tyes(data_list):

    """
    Função para contar os types
    Argumentos:
        data_list: lista com os registros de user_types.
    Retorna:
        Lista com a quantidade de Subscriber, Customer e Dependent.

    """

    subscriber = 0
    customer = 0
    dependent = 0
    
    for user_types in data_list:
        if 'Subscriber' in user_types:
            subscriber += 1
        elif 'Customer' in user_types:
            customer += 1
        elif 'Dependent' in user_types:
            dependent += 1
    
    return [subscriber, customer, dependent]

user_types_list = column_to_list(data_list, -3)
user_types_types = ['Subscriber', 'Customer', 'Dependent']
user_types_quantity = count_user_tyes(user_types_list)
user_types_y_pos = list(range(len(user_types_types)))
plt.bar(user_types_y_pos, user_types_quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de Usuários')
plt.xticks(user_types_y_pos, user_types_types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)