# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0
max_trip = 0
mean_trip = 0
median_trip = 0

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")

itens = len(trip_duration_list)
total_tempo = 0

for v in range (0,itens):
     t = trip_duration_list[v]
     total_tempo = total_tempo+ int(t)
     if int(t) >= int(max_trip):
       max_trip = t
       if int(t) <= int(min_trip):
           min_trip = t

ordenada = trip_duration_list
ordenada.sort()

meio = int(itens/2)

median_trip = ordenada[meio]                        
mean_trip = round(total_tempo/itens)
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
