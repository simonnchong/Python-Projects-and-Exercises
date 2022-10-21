with open("./hello.txt", encoding='utf8') as f: # use encoding for read language other than ASCII language such as Chinese, Japanese, 
    file = f.readlines()

for line in file:
    print(line.strip())