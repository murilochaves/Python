# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
total_trip_duration = 0.

trip_duration_list = list(map(int, trip_duration_list))

for trip_duration in trip_duration_list:
    if trip_duration < min_trip or min_trip == 0:
        min_trip = trip_duration
    elif trip_duration > max_trip:
        max_trip = trip_duration
    
    total_trip_duration += trip_duration

trip_duration_list_len = len(trip_duration_list)

mean_trip = round(total_trip_duration / trip_duration_list_len)

trip_duration_list.sort()

if trip_duration_list_len % 2 == 0:
    median_trip = (trip_duration_list[int((trip_duration_list_len / 2) - 1)] + trip_duration_list[int(trip_duration_list_len / 2)]) / 2
else:
    median_trip = trip_duration_list[int(trip_duration_list_len / 2)]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------