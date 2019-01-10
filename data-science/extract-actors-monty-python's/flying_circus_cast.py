#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

# TODO: criar uma lista dos atores que apareceram no programa de televisão
# Flying Circus do Monty Python.


def create_cast_list(filename):
    cast_list = []
    with open(filename, 'r') as f:
        for line in f:
            if 'Series Cast' not in line:
                name = line.split('\t')[0]
                cast_list.append(name)
    return cast_list

if __name__ == "__main__":
    cast_list = create_cast_list('source_data/flying_circus_cast.txt')
    for actor in cast_list:
        print(actor)
