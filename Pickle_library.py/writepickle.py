import pickle

l = [10, 20, 30, 40, 50]

file = open("writedata.txt", "wb")

pickle.dump(l, file)

file.close()

print("Data successfully saved!")

# import pickle
# import os

# l = [10, 20, 30, 40, 50]

# with open("writedata.txt", "wb") as file:
#     pickle.dump(l, file)

# print("Data saved successfully!")

# print("File location:", os.path.abspath("writedata.txt"))