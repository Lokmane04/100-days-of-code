from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Prenmom", ["Baslimane", "Lassakeur", "Haddadi", "Abadlia", "Lassakeur", "Baslimane"])
table.add_column("Nom", ["Lokmane", "Eimane", "Chakib", "Zied", "Habib", "Mohammed"])
table.align= "l"

print(table)
