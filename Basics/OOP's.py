#Simple concept of objects and classes in python.
class employee:
    def __init__(self, Jobname, salary) -> None:
        self.Jobname = Jobname
        self.salary = salary
        pass

sahas = employee("Django developer", "60000") #Arguements
print(sahas.Jobname)
print(sahas.salary)

luniva = employee("CTO", "45000")
print(luniva.Jobname)
print(luniva.salary)