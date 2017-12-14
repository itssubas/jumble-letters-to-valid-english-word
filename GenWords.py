from itertools import permutations

usr_input = input("word:")

permuted_list = [''.join(p) for p in permutations(str(usr_input))]
print (permuted_list)
count = 0
for elem in permuted_list:
    f = open("wordlist.txt")
    for line in f.readlines():
        if elem == line.strip("\n"):
            print (elem)
            count += 1

print (count)

