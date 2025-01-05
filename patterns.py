#Pattern programs

#Single star
print("*")
print("-----------------------------------")
n = 5
print("*"*n)

print("-----------------------------------")
#Square pattern
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=' ')
    print()

print("-----------------------------------")
#Left handed increasing pattern (left side triangle increasing)
n = 5

for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    print()

print("-----------------------------------")
#Left handed decreasing pattern (left side triangle increasing)
n = 5
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print()

print("-----------------------------------")
#Right sided triangle increasing

n = 5

for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

print("-----------------------------------")
#Right sided triangle decreasing

n = 5 

for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i,n):
        print('*', end=' ')
    print()

print("-----------------------------------")
#Hill pattern
n = 5

for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

print("-----------------------------------")
# Reverse Hill pattern

n = 5

for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()

print("-----------------------------------")
# Diamond pattern

n = 5

for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()

print("-----------------------------------")

##Pyramid

