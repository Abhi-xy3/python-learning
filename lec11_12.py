lorignal=[4,5,6,7]
new=lorignal[:]
lorignal.remove(2)






''''''
l1 =[1,2,3,4,5]
l2=[4,5,6,7,8]
for e in l1:
    if e in l2:
        l1.remove(e)

print(l1)
'''1235'''

l1 =[1,2,3,4,5]
l1_copy=l1[:]
l2=[4,5,6,7,8]
for e in l1_copy:
    if e in l2:
        l1.remove(e)

print(l1)
'''123'''



def make_(a):
    def g(b):
        return a*b
    return g

val = make_(2)(3)
print(val)


'''exception assertions'''
'''like-index.type,syntax ,name....error'''


try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

assert x < 0, "x must be negative"









def sum_digiits(s):
    total =0
    for char in s:
        try:
            val=int(char)
            total +=val
        except:
            print("cannot convert",char)
        return total