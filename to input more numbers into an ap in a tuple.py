def sequence(tup,n):
    n=len(tup)
    a=tup[0]
    c_d=tup[1]-tup[0]
    t=()
    for i in range(3):
        t=(tup[n-1]+c_d,)
        tup=tup+t
        n+=1
    return tup
tuple=eval(input("Enter a tuple of numbers as Ap: "))
num=int(input("enter the number of terms to be added: "))
solution = sequence(tuple,num)
print("The extended sequence is:", solution)