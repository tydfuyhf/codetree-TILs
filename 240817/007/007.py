class smt:
    def __init__(self,code,point,time):
        self.code=code
        self.point=point
        self.time=time
    def __str__(self):
        return "secret code : {}\nmeeting point : {}\ntime : {}".format(self.code,self.point,self.time)
x,y,z=input().split()
ans=smt(x,y,z)
print(ans)