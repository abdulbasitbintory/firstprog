list1 = [["Harry","2"], ["Larry","4"],
         ["Marry","6"], ["Carry","350"]]
for item, lollypop in list1:
    print(item,"and lolly is ", lollypop)
                    # NEXT
items = ["HaERRY", 5, 3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item >= 6:
        print(item)