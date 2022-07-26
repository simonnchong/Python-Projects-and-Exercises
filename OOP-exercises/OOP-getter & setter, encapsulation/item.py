import csv

class Item:

    def __init__(self, name: str, price: float, quantity = 0): 
        # self is the created instance itself
        # "name: str" is to set the datatype of parameter to avoid int as the argument input mistake
        # "quantity = 0" is also to set the datatype and initialize the parameter value at the same time

        # in order to avoid unwanted data, e.g: a negative value being passed into parameter price and quantity, 
        # use "assert" to do a data validation before it get processed
        # the fstring is the error message will be show if unwanted data being passed into this class constructor
        
        assert price >= 0, f"Price {price} cannot be negative value"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative value"

        #* _ and __ is used for private attribute
        #! _name means can be accessed directly to this attribute from outside of the class, like this -> `print(item1._name)`, but cannot be edited, like this -> `item1._name = "new word"`  
        #! __name means cannot be accessed and edited at all from outside of the class although you try to `print(item1.__name)` 
        #* so double underscore is a fully private execution can't be read and wrote at all, single underscores is only avoid to be edited but can be accessed from outside of the class
        #* single underscore and double underscores mean they only can be accessed in this class, even its child class
        self.__name = name
        self.price = price
        self.quantity =  quantity


    #* encapsulation -> private attribute         
    # this method return the private attribute which is an attribute with an double underscores as the starting,
    # when call this method, require no "()", like this -> `item1.name` instead of `item1.name()`
    @property # @property # declare a "getter" for read only, data can't be edited, 
    def name(self):
        return f"The name of this object is {self.__name}"

    
    # this method is to set the new value to the private attribute, like this -> `item1.name = "new name"`
    # when call this method, require no "()", like this -> `item1.name` instead of `item1.name()`
    # attribute.setter, replace the "attribute" name as the attribute name you wanna to set its setter
    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            # raise Exception to allow you to write your own exception message in error message form, instead of only the ordinary printing form
            raise Exception("Your new name is too long, please set it not more than 10 characters") 
        else:
            self.__name = new_name

#? Why do we use private attribute, setter and getter?
#! by using getter and setter, the programmer can control how their important variables are accessed and updated in the proper manner, such as changing the value of a variable within a specified range.
#! you might want them to have a different behaviors instead of only saved and accessed after they have been constructed
#! to avoid any accidental modification from outside of the class, and control how the data being accessed and modified, for example:
#! just like line 32, set the format of the attribute being printed, and line 40-44, set the data validation before it has been modified


#? Why do we use @property/Pythonic way of setter and getter instead of the ordinary way?
#! imagine you had done a bunch of code or a completed program, but now you decided to change the attribute from public to private
#! example you have a class "Item()" and 1 attribute "name", you have a valid instance `item1 = Item("Simon")` 
#! so you change the attribute from "name" to "__name" as private
#! let say in your main code you accessed the attribute -> `item1.name`, and modifying the attribute -> `item1.name = "newName"`
#! now if you set the "name" attribute to private, and if you wanna use the ordinary getter -> `getName(): return __name` and setter -> `setName(newName): return __name = newName`
#! so, you have to edit all of your codes which lines that accessed and modified the attribute -> "name", like this:
#! accessed the attribute -> `item1.getName()`, modifying the attribute -> `item1.setName("Simoon") = "newName"`
#! it is a terrible job to modify all existing code that accessing and modifying the particular attribute
#! so here come with the @property setter and getter!!!!!!
#! you don't have to change anything of the codes in main mode like on line 60, just access and edit it exactly like as it is public previously, see line 57
#! REMINDER: by calling the @property method when you want to access and edit the private attribute, you don't have to call the parenthesis line this -> `name()`, just call as usual just -> `name`
#! it seems it accesses and edits the private "name" directly but it's actually not, it calls the `name()` method behind the scene instead of the "name" itself