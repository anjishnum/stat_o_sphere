'''1st order to 4th order i.e. population mean to population kurtosis calculation'''

import numpy as np

class moment:

    def __init__(self):
        a = input("Enter array: ")
        a = a.split(',')
        ar = [float(x) for x in a]
        #print(ar) //for debugging if necessary
        print("Population mean: ",round(self.mean(ar),2))
        print("Population variance: ",round(self.variance(ar),2))
        print("Population skewness: ",round(self.skewness(ar),2))
        print("Population kurtosis: ",round(self.kurtosis(ar),2))

    # Population mean
    def mean(self,ar):
        
        value = 0
        
        for i in ar:
            value+=i
        
        value /= len(ar)

        return value

    # Population variance
    def variance(self,ar):
        
        value = 0

        for i in ar:
            value += (i-self.mean(ar))**2

        value /= len(ar)

        return value

    # Population skewness
    def skewness(self,ar):
        
        value = 0

        for i in ar:
            value += np.power((i-self.mean(ar)),3)

        value /= len(ar)*(np.power(self.variance(ar),3))

        return value

    # Population kurtosis
    def kurtosis(self,ar):

        value = 0

        for i in ar:
            value += np.power((i-self.mean(ar)),4)

        value /= len(ar)*(np.power(self.variance(ar),4))

        return value

moment = moment()
    

