def hello(name, last_name):
     print(f"hello {name} {last_name}!")

hello("alex", "bobrovski")

def number(leaks, *args):
     print(f"hello {leaks} {args[0]} {args[1]} {args[2]} ")

number('alex', 'stela', 'mahmud', 'andrey')

def user_info(**kwargs):
    print(kwargs)

user_info(name='stiv', age=20, city="bishkek")

my_dick = {"key": "value", "key1": "value"}
phonebook = {"mom": "4850349253", "brother": "29498329755"}
 
phonebook["mom"] = "3842084938"

print(phonebook["mom"])

print(phonebook.keys())
print(phonebook.values())
print(phonebook.items())

def user_info(**kwargs):
     for key, value in kwargs.items():
          print(f"Ключ: {key}, Значение: {value}")

user_info(name="alex", age=14)

def user_num(*args, **kwargs):
     print(args)
     print(kwargs)

user_num(1, 2, 3, 4, 5, 6, a=2, b=2, c=213)

str1 = "affeuereuwaajf"
str2 = "affreuwajf"
str3 = "affeuewaajf"
str4 = "affeuereuajf"
str5 = "affeuereaajf"

def count_letters(string):
     g_let = "euioaEUIOA"
     res = 0
     for i in string:
          if i in g_let:
             res = res + 1
     
     return res

print(count_letters(str1))
 
