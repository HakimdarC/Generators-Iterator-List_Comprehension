def sqfun(l):
    for i in l:
        yield (i*i)

lt = [1,2,3,4,5]
gen = sqfun(lt)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in sqfun(lt):
    print(i)

print([ x*x for x in lt]) 
