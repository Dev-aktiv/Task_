class demo:
    def test(a,b):
        c=a+b
        print(c)
    def test(a,b,c):
        c=a+b+c
        print(c)

demo1=demo
demo1.test(10,10,10)
#demo1.test(10,10)#TypeError and it says 1 required argument
# demo1.test(a=10,c=10,10)# Syntax error it says it follow keyword arguments
#demo1.test(10,c=10,10)#Syntax Error