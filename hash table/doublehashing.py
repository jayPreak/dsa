class DoubleHashing:
    def __init__(self, TableSize = 1111111):
        self.ts = TableSize
        self.List = [None]*self.ts
        self.count = 0

    def nearestPrime(self):
        for l in range((self.ts-1), 1, -1):
            flag = True
            for i in range(2, int(l**0.5)+1):
                if l%i == 0:
                    flag = False
                    break
            
            if flag:
                return l

        return 3

    def Hx1(self, key):
        return key%self.ts

    def Hx2(self, key):
        return self.nearestPrime() - (key%self.nearestPrime())

    def dHashing(self, key):
        if self.count == self.ts:
            print("List full")
            return
        elif self.List[self.Hx1(key)] == None:
            self.List[self.Hx1(key)] = key
            self.count+=1
            print(f"Entered key {key} at index {self.Hx1(key)}")

        else:
            comp = False
            i = 1
            while not comp:
                index = (self.Hx1(key) + i*self.Hx2(key))%self.ts

                if self.List[index] == None:
                    self.List[index] = key
                    print(f"Entered key {key} at index {index}")
                    comp = True
                    self.count +=1
                else:
                    i+=1
        return self.List

    def PrintHashList(self):
        for i in range(0, len(self.List)):
            print(self.List[i])

def main():
 
    tableSize = 5 
    DHash = DoubleHashing(tableSize)
 
    InputElements = [4,11, 29, 1, 5]
 
    for i in InputElements:
        DHash.dHashing(i)
 
 
    print('\n')
    print("The Hash List After Entering Elements")
    DHash.PrintHashList()
 
 
 
 
if __name__ =="__main__":
    main()
  

