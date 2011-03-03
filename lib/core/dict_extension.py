

def sort_dict_values_by_key( dictionary ):

    # Get the keys
    keys = dictionary.keys() 
    keys.sort()

    values = []

    for key in keys:
        values.append( dictionary[key] )

    return values

