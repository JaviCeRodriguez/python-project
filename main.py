from modules.module1 import Module1
from modules.module2 import Module2

# No existen los imports, es un ejemplo de como se importan las clases

def main():
    m1 = Module1()
    m2 = Module2()
    m1.print_module1()
    m2.print_module2()

if __name__ == '__main__':
    main()
