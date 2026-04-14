# String can be treated as list.

alpha = "Iron man"
first_char = alpha[0]

print(first_char)

slice_alpha = alpha[0:4]
print(slice_alpha)

num = "0123456789"
print(num[::2])
# in [a:b:c] atarts from a ends before b and c is for hopping
# Bonus: we can write num[::-1] to reverse the string
a = "Shree"
# print(a.upper()) # -> str in Upper case
# str.lower() -> str in Lower case
# str.strip() -> extra spaces removed
print(a.replace("S", "tyui")) # -> It replace "this" by "that" in str
# str.count("rep") -> gives count of rep in str
# len(str) -> gives lenght of str 
# raw = r"hello\nworld" -> prints as it is

chai = "Lemon, Ginger, Masala, Mint"
l1 = chai.split(", ") #Converts into list with entries separated with ", "

chai_var = ["Lemon", "Masala", "Ginger"]
l2 = " ".join(chai_var) #Converts lists into string with " " between entries
print(l2)

chai = "lemon tea"
print(chai.find("tea")) #gives position from which "tea" starts, if output is -1 then it does not exist

quantity = 2
chai_type = "Green"

order = "I ordered {} cups of {} tea" #{} are place holders
print(order.format(quantity, chai_type))