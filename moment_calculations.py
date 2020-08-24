'''1st order to 4th order i.e. population mean to population kurtosis calculation'''

class moment:

    def __init__(self):
        ar = input("Enter array: ")
        print(self.mean(ar))

    # Population mean
    def mean(self,ar):
        
        value = 0
        
        for i in ar:
            value+=i
        
        value /= len(ar)

        return value

moment = moment()
    

