import rpg

aragon = rpg.Character("Aragon", "Human")
galadriel = rpg.Character("Galadriel", "Elf")
frodo = rpg.Character("Frodo", "Hobbit")

frodo.inv.set_currency(9, 47, 23)

chest = rpg.Chest(["Longsword", "Iron Helmet"], 10, 56, 99)

print(chest.__dict__)
# print(aragon.__dict__)
# print(galadriel.__dict__)
# print(frodo.__dict__)

print(frodo.inv.get_currency())