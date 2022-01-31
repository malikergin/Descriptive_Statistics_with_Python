class stat:
    def __init__(self, lst = []):
        self.lst = lst 

    def count(self):
        return len(self.lst)
    
    def summmation(self):
        s = 0
        for i in self.lst:
            s += i
        return s 
   
    def Min(self):
        return min(self.lst)
    
    def Max(self):
        return max(self.lst)
    
    def Range(self):
        return max(self.lst) - min(self.lst)
    
    def Mean(self):
        summation = 0 
        n = len(self.lst)
        for j in self.lst:
            summation += j 
        return summation // n
    
    def Median(self):
        lst_sorted = sorted(self.lst)
        lst_len = len(self.lst)
        if lst_len % 2 == 0:
            return (lst_sorted[(lst_len - 1) //2] + lst_sorted[(lst_len + 1) // 2]) // 2
        else:
            return lst_sorted[(lst_len - 1) // 2]

    def Mode(self):
        f = {}
        for k in self.lst:
            if k not in f:
                f[k] = 1
            else:
                f[k] += 1
        return [m for m, l in f.items() if l == max(f.values())]   

    def Variance(self):
        y = 0 
        lst_len = len(self.lst)
        for w in self.lst:
            y += w
            avg = y // lst_len
            var = sum((w - avg)**2 for w in self.lst) // lst_len
        return  var

    def StandartDeviation(self):
        y = 0 
        lst_len = len(self.lst)
        for w in self.lst:
            y += w
            avg = y // lst_len
            var = sum((w - avg)**2 for w in self.lst) // lst_len
            std = var ** 0.5
        return std

    def descriptives(self):  
       return f'Count: {self.count()}, Sum: {self.summmation()}, Max: {self.Max()}, Min: {self.Min()}, Range: {self.Range()}, Mean: {self.Mean()}, Median: {self.Median()}, Mode: {self.Mode()}, Variance: {self.Variance()}, Standart Deviation: {self.StandartDeviation()}'