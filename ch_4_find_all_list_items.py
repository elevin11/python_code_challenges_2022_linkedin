# input list and value to search for
# return list of lists of integers: each list of integers is an 'index' - the address of the given value within the list
# may return multiple indices

# base case: 1-dimensional list
#

def index_all(list, val):
    indices = []
    for idx in range(len(list)):
        # if item is integer instead of list, check if it matches given value
        if isinstance(list[idx], int):
            if list[idx] == val:
                indices.append([idx])
        else:
            # if item is list, generate new list of indices by searching this list
            sub_indices = index_all(list[idx], val)
            for sub_idx in sub_indices:  # indices of values found in smaller list are added to bigger list
                new_idx = sub_idx
                new_idx.insert(0, idx)
                indices.append(new_idx)
    return indices


while (True):
    test = int(input("Enter a value to search for: "))
    #example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    example = [1, 2, 3, 4, 1, 0]
    print(index_all(example, test))
