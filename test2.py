from test import CreateNums

def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    name = 'tetdssdd'
    print('name:',name,'age:',age,'other:',kw)


name = 'tetd'
person(name, 24, city='Beijing', addr='Chaoyang', zipcode=123456)
print(name)