def get_order(n):
    i=1
    if i!= " ":
        for i in n:
            print('Preparing your order:')
            print('The Following Orders have been dispatched.')
        for i in n:   
            print(i)
            break
a=int(input("How many orders would you like to place:"))
order=[]
for i in range(a):
    if a>=i:
        b=input("enter items of your choice:")
        order.append(b)
    else:
        print("sorry, no order found")
get_order(order)
