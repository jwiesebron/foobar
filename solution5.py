def answer(n):
    res = 0
    while n != 1:
        if n % 2 != 0:
            if (n + 1) & n > (n - 1) & n:
                n += 1
            else:
                n -= 1
            res += 1
        n = int(n/2)
        res += 1
    return res


res = [0, 0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, 4, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 7, 6, 7, 6, 6, 5]
prev = 0
#for i in range(1, 1048577):
#    tmp = answer(i)
#    print(tmp)
#    if abs(tmp - prev) > 1:
#        print(i)
#    prev = tmp
#    #if res[i] != answer(i):
#    #    print(i)
#print(answer(11234))
print(answer(11))
#print(answer(112312341234129384721847213784129378461283794612387462387421341294873458973459873498573498573298572893475239847593842759384759374598729834759872398475982734985732984579832745983274598374958732985479234759324759823745035230457320457320495703924750239847509238745093274590324750324850372405974320587234))
