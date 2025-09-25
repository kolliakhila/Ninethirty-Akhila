class Intlst:
    def __init__(self):
        self.data=[]
    def _validate_int(self,value):
        if not isinstance(value,int):
            raise TypeError("Only integers are allowed")
    def append(self,value):           #method for append
        self._validate_int(value)
        self.data.append(value)
    def remove(self,value):              # method for remove
        self._validate_int(value)
        if value not in self.data:
            raise ValueError(f"{value} not found in list")
        self.data.remove(value)
    def pop(self, index=-1):             # method for pop
        if not self.data:
            raise IndexError("pop from empty list")
        return self.data.pop(index)
    def __getitem__(self, index):           # method for slicing
        if isinstance(index, slice):
            new_list = Intlst()
            new_list.data = self.data[index]
            return new_list
        elif isinstance(index, int):
            return self.data[index]
        else:
            raise TypeError("Invalid index type")
    
    def __repr__(self):
        return repr(self.data)
lst=Intlst()
lst.append(5)
lst.append(7)
lst.append(12)
lst.append(0)

lst.remove(0)

lst.pop()

print(lst[0])
print(lst[1])

print(lst)