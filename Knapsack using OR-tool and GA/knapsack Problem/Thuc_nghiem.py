

n = 0
c = 0
items = []
with open("s000.kp", "r") as f:
        f.readline()
        n = int(f.readline())
        print(n)
        c = int(f.readline())
        print(c)
        line = f.readline()
        for i in range(n): 
            line = f.readline()
            item = tuple(map(int, line.split()))
            items.append(item)

print(items)




