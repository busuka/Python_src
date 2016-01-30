
class Bubble():
    def __init__(self,tbl):
        self.tbl = tbl

    def sort(self):
        for i in range(len(self.tbl) - 1):
            if self.tbl[i] < self.tbl[i + 1]:
                tmp  = self.tbl[i]
                self.tbl[i] = self.tbl[i+1]
                self.tbl[i+1] = tmp
        print(self.tbl)




tables = [2,5,1,3]

sort_table = Bubble(tables)

sort_table.sort()

