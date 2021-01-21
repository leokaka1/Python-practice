"""
多态
"""

class Dog(object):
    def work(self):
        print("指哪打哪")

class ArmDog(Dog):
    def work(self):
        print("追击敌人")

class DrugDog(Dog):
    def work(self):
        print("追查毒品")

class Person(object):
    def work_with_dog(self,dog):
        dog.work()

ad = ArmDog()
dd =DrugDog()

leon = Person()
leon.work_with_dog(ad)
leon.work_with_dog(dd)