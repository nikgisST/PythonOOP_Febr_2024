x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x              # свързва LOCAL SCOPE с ENCLOSING SCOPE
        x = "nonlocal"
        print("inner:", x)      # inner: nonlocal
    def change_global():
        global x                # свързва LOCAL SCOPE с GLOBAL SCOPE
        x = "global: changed!"

    print("outer:", x)   # outer: local
    inner()
    print("outer:", x)   # outer: nonlocal
    change_global()

# x = "global: changed!"  с global думата все едно тук съществува този ред

print(x)  # global
outer()   # outer: local
          # inner: nonlocal
          # outer: nonlocal
print(x)  # global: changed


