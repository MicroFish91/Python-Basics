# same can be done with "import json"
# Pickle stores data in binary format
import pickle

data = {"first_name": "matt", "last_name": "fisher"}

# Read from File
with open("data.pickle", "rb") as fh:
    read_data = pickle.load(fh)
    print(data)

# Write to File
# with open("data.pickle", "wb") as fh:
#     pickle.dump(data, fh)
