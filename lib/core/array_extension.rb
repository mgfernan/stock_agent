
# This class methods extend the ones for the class Array
class Array
   
    # The method _sum_ adds all the elements of the Array
    def sum
        sum = 0.0
        (0...self.size).each { |index| sum = sum + self[index] }
        return sum
    end

    # The method _mean_ computes the mean value inside a Array
    def mean
        return self.sum / self.size
    end

    # The method _compute_sliding_window_ computes an averaged
    # sliding window of the array for a given set of options.
    # _n_samples_ (which is an optional parameter with the default value of 
    # 10 samples). 
    # _delay_ parameter (also optional parameter) indicates if the sliding
    # window has to be computed at the *middle* of the interval, 
    # at the *front* or at the *back*
    # _missing_nil_ indicates that if the number of samples is less than
    # _n_samples_ a nil is stored. Otherwise it will compute the mean with
    # the available number of samples
    def compute_sliding_window( opts={} )
    
        average = Array.new
       
        # Check the hash containing the options for the method
        options = { :n_samples   => 10,
                    :delay       => 'middle',
                    :missing_nil => 'true' }.merge( opts )

        n_samples  = options[ :n_samples ]

        # Run through the array to compute the middle point
        self.each_with_index do |value,index|

            # Computes the from and to indices
            if options[:delay] == 'middle' then
                from = index - n_samples/2
                to   = index + n_samples/2
                to   = to - 1 if n_samples.even?
            elsif options[:delay] == 'front'
                from = index - n_samples + 1
                to   = index 
            else
                from = index 
                to   = index + n_samples - 1
            end

            # Check array limits
            from = 0 if from < 0
            to   = self.size - 1 if to >= self.size - 1
      
            # Compute sample
            sample = self[from..to].mean
            sample = nil if options[:missing_nil] and (to-from+1 < n_samples)

            # Add averaged sampled to the array
            average << sample
        
        end
        
        return average
    
    end


end
