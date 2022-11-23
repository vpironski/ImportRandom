lines = int(input("Input the number of lines: "))

with open("search_engine/file.txt", "w", encoding="UTF-8") as f:
    line = 1
    while line <= lines:
        f.write(str(line)+"\n")
        line += 1