# f = open("./refer.txt",'r+')
# string = ""
# for line in f.readlines():
#     string += line[:line.rfind("-")].strip() + "\n"
# print(string)

# f.close()

# fw = open("./refer.txt",'w')
# fw.write(string)
# fw.close()

# Dependency

f1 = open("./refer.txt",'r')
f2 = open("./Dependency.txt",'r')
l = []
s = f2.read().split('\n')
t = f1.read().split('\n')
for line in t:
    if line in s:
        l.append(line)
    if len(l)==5:
        break
print(l)