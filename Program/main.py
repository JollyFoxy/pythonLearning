class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.phone = "null"

    @property
    def get_age(self):
        return self.age

    @get_age.setter
    def set_age(self, age):
        self.age = age

    @property
    def get_phone(self):
        return self.phone

    @get_phone.setter
    def set_phone(self, phone):
        self.phone = phone

    @property
    def get_name(self):
        return self.name
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPhone: {self.phone}")


viktor = Person("Vitya")
viktor.set_age()
viktor.set_phone(88005553535)
viktor.display_info()
