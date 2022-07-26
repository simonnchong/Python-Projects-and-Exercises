class A:
    def __init__(self) -> None:
        # print("A")
        pass

    def fun(self):
        print("A function")

class B(A):
    def __init__(self) -> None:
        super().__init__()
        # print("B")
        pass

    def fun(self):
        super().fun()
        print("B function")

a = A()
b = B()

b.fun()