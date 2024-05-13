x = "global"

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)  # inner: nonlocal
    def change_global():
        x = "global: changed!"

    print("outer:", x)   # outer: local
    inner()
    print("outer:", x)   # outer: local
    change_global()


print(x)  # global
outer()   # outer: local
          # inner: nonlocal
          # outer: local
print(x)  # global


