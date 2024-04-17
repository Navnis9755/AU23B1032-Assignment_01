def get_name():
    name=input("enter your name:-")
    return name

def get_tshirt(n):
    name=get_name()
    a=input("which brand do you want:-")
    b=input("in which size do you want:-")
    brand=['allen solly', 'puma', 'roadster', 'sassafaras', 'tokyo talkies']
    size=['xs', 's', 'm', 'l', 'xl', 'xxl']
    for i in brand and size:
      if i==a or i==b:
        print("Hi", name + ",", "the brand and size you are looking for is available in our store.")
        break
      else:
        print("Hi", name + ",", "the brand and size you are looking for is not available in our store.")
get_tshirt('roadster')
