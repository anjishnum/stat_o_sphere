'''1st order to 4th order i.e. population mean to population kurtosis calculation'''

class moment:

    def __init__(self):
        a = input("Enter array: ")
        ar = []
        for i in a:
            try:
                type(int(i))
                ar.append(int(i))
            except:
                continue
        print(self.mean(ar))

    # Population mean
    def mean(self,ar):
        
        value = 0
        
        for i in ar:
            value+=i
        
        value /= len(ar)

        return value

moment = moment()
    

