def store_csv( csv_data, header=False, field_separator=','):
    """ Store csv into a structure that is a Hash with arrays. The first line of the csv """

    dictionary  = {}
    names = []

    lines = csv_data.split( '\n' )

    first_line = True

    for line in lines:
        values = line.split( field_separator )
        n_values = len( values )

        # build header if necessary
        if first_line:
            for i in range(n_values):
                name = values[i] if header else i
                names.append( name )
                dictionary[ name ] = []
            first_line = False
            if header: continue
       
        # Add elements
        for i in range( n_values ):
            dictionary[ names[i] ].append( values[i] )

                
    return dictionary


