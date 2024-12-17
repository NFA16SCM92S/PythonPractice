from Chef import Chef
#using inheritence to use 3 methods from the Chef class
class ChineseChef(Chef):

    def make_special_dish(self): #Override the method
        print("CHef makes broccoli with garlic sauce")

    def make_fried_rice(self):
        print("The chef makes fried rice")