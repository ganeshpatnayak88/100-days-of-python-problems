from abstration import vehical

class car(vehical):
    def start(self):
        print("car starts with key")
    def wheel(self,no_of_wheel):
        print("no_of_wheel",no_of_wheel)
class bike(vehical):
    def start(self):
        print("bike start with kick")
    def wheel(self,no_of_wheel):
        print("no_of_wheel",no_of_wheel)