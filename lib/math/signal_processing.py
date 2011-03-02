
# Signal Processing module. This module includes routines, classes and methods used for 
# signal processing



def compute_ema( signal, time_periods=15.0):
    """ Exponential Moving Average
        Further references in: http://en.wikipedia.org/wiki/Moving_average """

    alpha = 2.0 / ( time_periods + 1.0 )

    n_samples = len( signal )
    
    ema = [0] * n_samples

    for i in xrange( n_samples ):
        ema[i] = (signal[i]*alpha + (1-alpha)*ema[i-1]) if i>0 else signal[0]

    return ema

