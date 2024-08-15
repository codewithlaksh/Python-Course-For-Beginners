# key:value
# key --> immutable datatype
# value --> immutable/mutable datatype
d = {'name': 'Lakshyaraj', 'age': 18, 'marks': 99}
print(d)
print(d['name'])
print(d['age'])
print(d['marks'])

for i in d:
    print(f'Key: {i} & Value: {d[i]}')

d = dict([('name', 'Lakshyaraj')])
print(d)

d = dict.fromkeys('Lakshyaraj')
d = dict.fromkeys('Lakshyaraj', 11)
print(d)

d = {'name': 'Lakshyaraj', 'age': 18, 'marks': 99}
d['grade'] = 'A1'
print(d)

d.setdefault('age', 19)
d.setdefault('grade', 'A1')

for key, value in d.items():
    print(f'Key: {key} & Value: {value}')

res = d.pop('grade')
res = d.pop('marks')
res = d.popitem()
print(res)

val = d.get('grade')
print(val)

d1 = {'grade': 'A1', 'promoted': True}
d.update(d1)
d1.update(d)
print(d1)

keys = d.keys()
print(keys)
values = d.values()
print(values)


d1 = d
d2 = d.copy()



d1['grade'] = 'A1'
print(id(d1))
print(id(d))
print(d1)
print(d)



d2['grade'] = 'A1'
print(id(d2))
print(id(d))
print(d2)
print(d)



del d['name']
print(d)
del d
print(d)


d.clear()
print(d)

'''
Quiz 2: Take a list of different numbers and find out the mode of the numbers (ie number with maximum occurrence).
Warning: DO NOT USE 'statistics' module.
'''
