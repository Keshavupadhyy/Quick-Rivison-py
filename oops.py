# class employee:
#      Salary = 89
#      Salary2 = 88
#      def getSalary(self):
#          return self.Salary
#      def getSalary2(self):
#          return self.getSalary2()
#
# keshav = employee()
# print(keshav.Salary)
#
# subhanshu = employee()
# print(subhanshu.Salary2)

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    # def getName(self):
    #     print(self.name)
    # def getSalary(self):
    #     print(self.salary)

keshav = Employee("keshav" , 3355)
print(keshav.salary)
print(keshav.name)
# keshav.getSalary()
# keshav.getName()
subhanshu = Employee("subhanshu",3256987)
print(subhanshu.salary)
print(subhanshu.name)