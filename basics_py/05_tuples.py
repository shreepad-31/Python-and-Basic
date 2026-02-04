# tuples can be nested

tea = ("Green", "Black", "Oolong")
# tea[0] = "Lemon" --> Not possible, tuples are immutable

tea_new = ("White", "Mint")
all_tea = tea_new + tea

tea_new = ("White", "Mint", "White")
print(tea_new.count("White"))

(e1, e2, e3) = tea