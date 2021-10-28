f = open("harry.txt", "w")
f.write("Harry bohat acha hai\n")
f.close()
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
f = open("harry2.txt", "a")
f.write("Harry bohat acha hai\n")
f.close()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
f = open("harry2.txt", "r+")
print(f.read())
f.write("thanks")