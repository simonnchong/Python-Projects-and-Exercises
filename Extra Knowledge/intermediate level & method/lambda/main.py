
# --------------------------------------------- single variable ---------------------------------------------
from turtle import title


def double(x):
    return x*2

# same as

double = lambda x : x*2

print(double(9))


# --------------------------------------------- multiple variables ---------------------------------------------

def full_name(first_name, last_name):
    return f"{first_name.strip().title()} {last_name.strip().title()}"

# same as ...
# define the lambda function
full_name = lambda first_name, last_name : f"{first_name.strip().title()} {last_name.strip().title()}"

# call it
print(full_name("  SImon  ", " ChOnG"))