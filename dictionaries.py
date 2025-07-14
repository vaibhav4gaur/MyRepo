'''dictionary = {'a':'airplane','b':'bazball','c':'commomwealth-game'}
dictionary['e'] = 'apple'
print(dictionary.get('e', "'g' not found"))

# List
x = []
for i in range(11):
    if i%2 == 0:

      x.append(i ** 2)

print(x)'''

# type of collection
# unordered
# unique elements
# {}
'''
set1 = {1,2,3,4,5}
set1.remove(1)
print (set1)

set1 = {2,3,4,5}
set2 = {4,6,7,8,9}
print(set1.union(set2))

set1 = {4,5,6,7,8}
set2 = {1,2,0}
print(set2.issubset(set1))

b = 'vaibhav GaUr'
 print(b.upper())
print(b.lower())

 c = '10'
 print(c.isaplha())

 d = 'This is Great Buddy'
 print(d.startswith('Great'))
 print(d.endswith('Buddy'))
 print(d.replace('This','Shashank'))
 print(d.find('e'))  e --> finds index value and form multiple indexing signal
 print(d.splitlines())

s = 'Gaurav','Gangautri'
p = ','
print(p.join(s))



name = "King-kong"
number = len(name)*4
print("Hello {}, your lucky number is {}.".format(name,number))

price = 150
with_tax = 200 + 80
print(price,with_tax)


# tuple
tup0 = ('SadaShivya',122,988)
tup1 = ('Sarvashweya',45,91)
tup2 = ('Mrutunjuya',1.11)
print(tup0 + tup1 + tup2)
'''
