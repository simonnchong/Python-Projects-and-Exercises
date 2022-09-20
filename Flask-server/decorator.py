import time

def delay_decorator(func):
    def wrapper_function():
        time.sleep(2)
        # do something before
        func()
        # do something after
    return wrapper_function()

# @ decorator wrap the function into it
@delay_decorator
def say_hello():
    print("hello")

@delay_decorator
def say_bye():
    print("bye")

@delay_decorator
def say_greeting():
    print("greeting")

# ------------------------------------------------------------ EXERCISE ------------------------------------------------------------ 

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i
        
@speed_calc_decorator
def slow_function():
    for i in range(90000000):
        i * i
        
fast_function()
slow_function()