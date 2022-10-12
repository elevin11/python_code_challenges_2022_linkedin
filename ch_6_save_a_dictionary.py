import json
# write function to save dictionary object to file


# takes two inputs, dictionary to be saved and output file path


def save(dict, path):
    # opens file from given path for writing - will create file if none at given path
    out_file = open(path, 'w')
    json.dump(dict, out_file)  # dumps data from dictionary to json file
    out_file.close()
    return


# takes file path as input and returns dictionary object
def load(path):
    read_file = open(path, 'r')
    data = json.load(read_file)
    dict = {}
    for key in data:
        dict[key] = data[key]
    return dict


test_dict = {"a": 1, "b": 3}
save(test_dict, 'test_file.json')
load_test = load('test_file.json')
print(load_test)
