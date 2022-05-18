l1=["Ramesh","Rakesh","Suresh",'Usha']
for items in l1:
    print(f"Good Morning ! {items}")

l2=["sandeep","sarojini","arti","binu","shweta"]
for items in l2:
    if items[0]=="s":
        print("Good Morning,",items)
    else:
        pass

l3=["Ramesh","Rakesh","Suresh",'Usha',"dhruva"]
for names in l3:
    if names.startswith("R"):
        print(f"Hello ! {names}")




