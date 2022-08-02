class Car:
    def __init__(self, *args, **kwargs) -> None:
        self.price = args
        self.make = kwargs['what']
        self.appearance = kwargs.get('how') # return "None" if the key is not found in dictionary
        
    def display(self):
        print(self.price)
        print(self.make)
        print(self.appearance)
        
        
my_car = Car(399, 999, what = "deluxe car")
my_car.display()
# (399, 999)
# deluxe car
# None


def test(arg, kwarg, *args, **kwargs):
    print("-------- Test 1")
    print(arg)
    print(kwarg)
    print(args)
    print(kwargs)
    
test(1, kwarg = 2)
# -------- Test 1
# 1
# 2
# ()
# {}



def test2(arg, *args, kwarg, **kwargs):
    print("-------- Test 2")
    print(arg)
    print(kwarg)
    print(args)
    print(kwargs)
    
test2(1, 2, 3, 4, kwarg = 5)
# -------- Test 2
# 1
# 5
# (2, 3, 4)
# {}


def test3(a, *args, **kw): 
    print("-------- Test 3")
    print(a)
    print(args)
    print(kw)

test3(4, 7, 3, 0, x=10, y=64)
# -------- Test 3
# 4
# (7, 3, 0)
# {'x': 10, 'y': 64}


# # cant put required argument as last parameter
def test4(arg, *args, **kwargs, kwarg):
    print(arg)
    print(kwarg)
    print(args)
    print(kwargs)
    
test2(1, 2, 3, 4, kwarg = 5)