from Relevance import Relevance

n = int( input() )
a = list(map( int, input().split() ))
if len(a) != n:
    raise RuntimeError(f"Количество элементов не равно заданному числу: {n}")


d = int( input() )
f = [ list(map( int, input().split() )) for i in range(d) ]
if any(len(sublist) != n for sublist in f):
    raise RuntimeError(f"Количество элементов не равно заданному числу: {n}")

objs = Relevance(a, f)


q = int( input() )
commands = [ list(map( int, input().split() )) for i in range(q) ]

for command in commands:
    match command[0]:

        # Display indexes after sorting by relevance
        case 1:
            k = command[1]
            print(objs.get_relevance_sort_indexes(k))

        # Changing characteristics (f)
        case 2:
            i = command[1]
            j = command[2]
            v = command[3]

            objs.update_digit_characteristics(i, j, v)

        # No other commands
        case _:
            raise RuntimeError("Ожидалось встретить команды (\"1\", \"2\")")