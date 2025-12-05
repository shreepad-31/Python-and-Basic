# lists can be nested

poke = ["pika", "bulba", "squarta", "chiko" ]
poke[1:1] = ["chari", "blezi"]

# poke.append("Oolong") -> add at end of list
# poke.pop() -> removes a entry at end of list
# poke.remove("Oolong") -> removes given entry in the list
# poke.insert(1, "Oolong") -> inserts given entry in the list

tea = ["Black", "Green", "Oolong", "Herbal"]
tea[3] = "White"

# tea_copy = tea.copy() -> with different referance

print(tea, poke)

# loop: for varible in object:
# for x in range(0,10) -> gives numbers from 0 to 9

squared_num = [x**2 for x in range(10)]