# This file contains helper functions for csv files


# Store csv into a structure that is a Hash with arrays. The first line of the csv
def store_csv( csv_data, opts={})

    options = { :header => false,
                :field_separator => ',' }.merge( opts )

    hash  = Hash.new
    names = Hash.new

    csv_data.each_with_index do |line, i_line|

        values   = line.strip.split( options[:field_separator] )
        n_values = values.size

        # Process header if first row is the header
        values.each_with_index do |value,i_value|

            # Build the names of the rows
            if( i_line == 0 ) then
                name = ( options[:header] ? value : i_value )
                names[ i_value ] = name
                hash[ name ] = Array.new
                next if options[ :header ]
            end

            name = names[ i_value ]
            hash[ name ] << value
        end

    end

    return hash

end

