
# Signal Processing module. This module includes routines, classes and methods used for 
# signal processing
module SignalProcessing



    #  Computes sliding window of an _array_ using _n_samples_ (which is an optional parameter with
    #  the default value of 10 samples). The _delay_ parameter (also optional parameter) indicates
    #  if the sliding window has to be computed at the *middle* of the interval, at the *front* or
    #  at the *back*
    def self.compute_sliding_window( array, opts={})
    
        average = Array.new
       
        # Check the hash containing the options for the method
        options = { :n_samples => 10,
                    :delay     => 'middle'}.merge( opts )

        # Run through the array to compute the middle point
        array.each_with_index do |value,index|

            # Computes the from and to indices
            if options[:delay] == 'middle' then
                from = index - n_samples/2
                to   = index + n_samples/2
            elsif options[:delay] == 'front'
                from = index + n_samples
                to   = index 
            else
                from = index - n_samples/2
                to   = index 
            end

        
            # Determine start and ending values
            from = index - ( nSamples - 1)
            from = from + midSample
            to   = from + ( nSamples - 1 )
        
            # Boundary check
            from = 0 if from < 0
            to   = array.size if to >= array.size
        
            average = ( to-from+1 < nSamples ? nil : array[from..to].mean )
        
            average << average
        
        end
        
        return average
    
    end

end
