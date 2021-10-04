from tabulate import tabulate
Head = ["Nodes"]
source_node = input("What is the name of the source node")
Table = [["",0]]
all_nodes = [source_node]
remaining_nodes = []
Head.append(source_node)
condition = input("Do you want to input other nodes?(y/n)")
while condition == "y":
    current_node = input("What is the name of the node?")
    Head.append(current_node)
    all_nodes.append(current_node)
    remaining_nodes.append(current_node)
    Table[0].append(10**12)
    condition = input("Do you want to input other nodes?(y/n)")
print(tabulate(Table, headers=Head, tablefmt="grid"))
for item0 in all_nodes:
    minimum = 10**12
    for item1 in Table[0]:
        if type(item1) == int:
            if item1 < minimum:
                minimum = item1
            else:
                pass
        else:
            pass
    for item3 in remaining_nodes:
        if item3 == Head[Table[0].index(minimum)]:
            remaining_nodes.remove(Head[Table[0].index(minimum)])
        else:
            pass
    for item2 in remaining_nodes:
        distance_condition = input("Is " + Head[Table[0].index(minimum)] + " connected to " + item2 + " ?(y/n)")
        if distance_condition == "y":
            distance = int(input("What is the distance between " + Head[Table[0].index(minimum)] + " and " + item2 + "?"))
            if minimum + distance <= Table[0][Head.index(item2)]:
                Table[0][Head.index(item2)] = minimum + distance
            else:
                pass
        else:
            pass
    Table[0][Table[0].index(minimum)] = ""
    print(tabulate(Table, headers=Head, tablefmt="grid"))
