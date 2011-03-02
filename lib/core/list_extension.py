

def convert_to_float_list( in_list ):
    out_list = []

    for element in in_list:
        try:
            value = float( element )
        except Exception: value = None

        out_list.append( value )

    return out_list
