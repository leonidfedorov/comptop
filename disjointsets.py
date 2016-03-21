class DisjSets:
    class Singleton:
        def __init__(self, name_value):
            self.__name = name_value
            self.size = 1
            self.parent = self
        def getName(self):
            return self.__name
 
    __subsets = None
 
    def __init__(self):
        self.__subsets = {}
 
    def MakeSet(self, name):
        self.__subsets[name] = self.Singleton(name)
 
    def Join(self, nameA, nameB):
        a = self.__subsets[nameA]
        b = self.__subsets[nameB]
        pa = self.Find(a)
        pb = self.Find(b)
        if pa == pb: 
            return
        parent = pa
        child = pb
        if pa.size < pb.size:
            parent = pb
            child = pa
        child.parent = parent
        parent.size = max(parent.size, child.size + 1)
    
    def Find(self, x):
        if x == x.parent:
            return x
        x.parent = self.Find(x.parent)
        return x.parent
