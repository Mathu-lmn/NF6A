from distutils.command.build_scripts import build_scripts


a = 14
b = 13.2
c = "Hello"
d = True

print(type(a),type(b),type(c),type(d))
#yes we can assign the value of a variable to another variable even if their type is different

b_int = int(b)
a_float = float(a)

print(b_int,a_float)

a_str = str(a)
b_str = str(b)

print(a_str,b_str)