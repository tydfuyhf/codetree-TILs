class nl:
    def __init__(self, Id, level):
        self.Id=Id
        self.level=level
    def __str__(self):
        return "user {} lv {}".format(self.Id,self.level)
x,y=input().split()
ans=nl(x,y)
print("user codetree lv 10")
print(ans)