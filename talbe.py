print("구구단 출력")
print()
for i in range(1, 9):
    print(i, "단 출력")
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i * j))
