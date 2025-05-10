L = [4, 5, 6, 7, 8, 9, 10]
print("The original list is :", L)
count = 0
for i in L:
    count += i
avg = count/len(L)
print("Sum =", count)
print("Average =", avg)
print("Smallest element =", L[0])
print("Largest element =", L[-1])