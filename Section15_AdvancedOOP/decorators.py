## inner func
def outer_func():
    print("This is the first func")
    def inner_func():
        print("This is the inner")

    inner_func()
    print("This will also be printed")
    return inner_func

# outer_func()

## calling inner funcs
# output = outer_func()
# print(output)       # This will return a memory address


## returning inner func
# print(output())     # This will return the inner func

## decorators
def dec(inner_func):
    def wrapper_func():
        print("I am the wrapper")
        inner_func()

    return wrapper_func

def modified_func():
    print("This is modified func")

c = dec(modified_func)
# print(c)
# print(c())

## @ symbol
@dec
def modified_func():
    print("This is modified func")

x = modified_func()

## Reuse decorators
@dec
def new():
    print("This is new func")

k = new()