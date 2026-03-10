class employee:
    def work(self):
        print("employee works")

class intern(employee):
    def work(self):
        super().work()
        print("intern works")

i1 = intern()
i1.work()
    
