class Dad:
    basketball=1
class Son(Dad):
    dance=1
    def isdance(self):
        return f"Yes I dance {self.dance} number of times"
class Grandson (Son):
    dance = 6
    def isdance (self):
        return f"Yes this is perfect, {self.dance} is enough"
larry=Grandson()
print(larry.basketball)
print(larry.isdance())