w = [3618169,1063503,3361573,1549665,352217,2660376,1076829,549933,2830684,2090407,1129519,2307073,468632,1236319,2370568,167256]
i = 0

sum = 0
for i in range(65536):
    binary_string = bin(i)[2:].zfill(16)
    bits = tuple(map(int, binary_string))
    k = 0
    sum = 0
    for i in bits:
        sum += i*w[k]
        k+=1
    if sum == 16945769:
        print("chat gtp kommer ta våra jobb")
        break
    print(bits)