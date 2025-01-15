class A:
    def method_a(self):
        print("Method from class A")

class B:
    def method_b(self):
        print("Method from class B")

class C(A, B):
    def method_c(self):
        print("Method from class C")

c = C()
c.method_a()
c.method_b()
c.method_c()