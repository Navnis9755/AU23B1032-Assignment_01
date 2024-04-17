def get_name():
    name=input("enter your name:")
    return name

def get_tshirt(n):
    name=get_name()
    a=input("which brand do you want:")
    brand=['allen solly', 'puma', 'roadster', 'sassafaras', 'tokyo talkies']
    for i in brand:
      if i==a:
        print("Hi", name + ",", "the brand you are looking for is available in our store.")
        break
      else:
        print("Hi", name + ",", "the brand you are looking for is not available in our store.")
get_tshirt('roadster')
