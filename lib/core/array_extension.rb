
# This class methods extend the ones for the class Array
class Array
   
    # The method _sum_ adds all the elements of the Array
    def sum
        sum = 0.0
        (1...self.size).each { |index| sum = sum + self[index] }
        return sum
    end

    # The method _mean_ computes the mean value inside a Array
    def mean
        return self.sum / self.size
    end

end
