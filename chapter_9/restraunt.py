# page 162  9-1
class Restraunt :
    def __init__(self,name,cuisine_type):
      self.name = name
      self.cuisine_type = cuisine_type
      
    def describe_restraunt(self):
        print(f"My favorite restraunt name is {self.name} and it`s type is {self.cuisine_type} .")
    
    def open_restraunt(self):
        print(f"The {self.name}`s restraunt is open seven days a week ! .")
        
my_restraunt = Restraunt("Attawich" , "Fast Food");  
my_restraunt.describe_restraunt();
my_restraunt.open_restraunt();


# my_restraunt = Restraunt("Atawich", "Fast food");
# print(f"My restraunt name is {my_restraunt.name} and it`s type is {my_restraunt.cuisine_type}")

