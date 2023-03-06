class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPhone: {self.phone}")


viktor = Person("vitya", 24, "88005553535")
viktor.display_info()
