# define the Vehicle class
class Vehicle:

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1=Vehicle()

car1.name="curul"
car1.color="cacat"
car1.kind="pansat"
car1.value=3000
# test code
print(car1.description())

