#  page 162 9-3

class Users :
    def __init__(self , name , last_name , age , city):
        self.name = name;
        self.last_name = last_name;
        self.age = age;
        self.city = city;
    def describe_user(self):
        print(f"{self.name.title()} {self.last_name.title()} is {self.age} years old and lives in {self.city} .")

user_info = Users("Barbara" , "Meinheim" , 38 , "Hamburg");
user_info.describe_user()