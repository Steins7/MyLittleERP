a = 10
b = 50

c = [a,b]

print(globals().keys())



l = [v for v in  globals().keys()]
print(l)

d = 'coucou'
print(d[0:2])

for v in l:
    if v[0:2] == '__':
        continue
        
    print(v + ' : ' + str(globals()[v])  )
    
    
    
