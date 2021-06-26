# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # 1. Lambda Function

# %%
mul = lambda x,y : x/y
print(mul(1,2))

# %% [markdown]
# # 2. Function Args and Kwargs

# %%
def input1(*args):
    for i in args:
        print(i)
input1(1,2,3)


# %%
def input2(**k):
    lists = {}
    for key,value in zip(k.keys(), k.values()):
        lists[key] = value
    return lists


# %%
input2(x = "Tran", y = "Phat")


# %%
def input3(*z, y ,x = 1):
    print(x)
    print(y)
    print(z)


# %%
input3(1,2,3,4, y = 10, x = 5)

# %% [markdown]
# # 3. Iterator

# %%
mylist = [1,2,3, "phat", "deptrai"]


# %%
iterator = iter(mylist)
print(iterator)

# %% [markdown]
# Lazy Evaluation

# %%
print(iterator[1])


# %%
print(next(iterator))
print(next(iterator))
print(next(iterator))


# %%
print(next(iterator))
print(next(iterator))
print(next(iterator))

# %% [markdown]
# # 4. Generators and Yeild
# %% [markdown]
# ## normal function

# %%
def reverse_func(data):
    for i in range(len(data), 0, -1): # start: optional, stop: required, steps: optional
        print(i)                      # default: 0                       default: 1


# %%
mylist = [3,1,2,4]
reverlist = reverse_func(mylist)


# %%
def reverse_function(data):
    lists = []
    for i in range(len(data) - 1, -1, -1):
        lists.append(data[i])
    return lists


# %%
lists = list(range(10000000))


# %%
get_ipython().run_line_magic('time', 'reverse = reverse_function(lists)')


# %%
print(reverse)

# %% [markdown]
# ## generators

# %%
def reverse_gen(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]


# %%
mylist = [2,3,5,1]


# %%
get_ipython().run_line_magic('time', 'generator_list = reverse_gen(mylist)')


# %%
for i in generator_list:
    print(i)


# %%
next(reverse_gen(mylist))


# %%
print(generator_list)

# %% [markdown]
# # 5. Map
# %% [markdown]
# ## Traditional

# %%
def add_five(a):
    lists = []
    for ele in a:
        ele = ele + 5
        lists.append(ele)
    return lists


# %%
lists1 = [5,10,3]
add_five(lists1)


# %%
def add_5_map(a):
    return a + 5


# %%
out = map(add_5_map, lists)
next(out)

# %% [markdown]
# ## Advanced

# %%
output = map(lambda x : x + 5, lists1)


# %%
print(list(output))


# %%
powli = [2,2,2]


# %%
pow_list = map(pow, lists,powli)
# next(pow_list)
list(pow_list)


# %%
list(map(lambda x,y : x+y, lists, powli))

# %% [markdown]
# # 6. Filter Function
# %% [markdown]
# ## Traditional

# %%
def grades(grade):
    lists = []
    for i in grade:
        if i > 50:
            lists.append(i)
    return lists


# %%
lists = [10,50,60,70,75,80]


# %%
print(grades(lists))

# %% [markdown]
# ## Avanced Function

# %%
def gradeslist(grades):
    return grades > 50


# %%
print(list(filter(gradeslist, lists)))


# %%
print(list(filter(lambda grade: grade > 50, lists)))


# %%
print(list(map(lambda x: x >50, lists)))


