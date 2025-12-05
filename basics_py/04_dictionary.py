# dictionaries can be nested

name = {"First": "Shreepad", "Last" : "Deshmukh"}
name["Last"] = "Jagtap"
name["Middle"]= "Janardan"

# name_copy = name.copy() -> with diff ref

name["First"]
name.get("First")

for text in name:
    print(text, name[text])
for key, value in name.fromkeys():
    print(key, value)

# name.pop("Middle") -> removes given element
# name.popitem() -> removes last element 
# del name["Middle"] -> removes given element

cafe = {
    "tea": {"Green" : "$15", "Black": "$5"},
    "coffee": {"Normal": "$10", "Cold" : "$20"}
}

print(cafe["tea"])
print(cafe["tea"]["Green"])

squared_num = {x:x**2 for x in range(6)}
# squared_num.clear() -> removes all elements
print(squared_num)

# Generating Dictionary
key = ["Masala", "Ginger", "Green"]
default = "Good"

new_dict = dict.fromkeys(key, default)
print(new_dict)