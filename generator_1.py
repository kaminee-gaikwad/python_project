users=[
    {
        'name' : 'john***',
        'age' : 17,
        'favourite_sport' : 'football'
    },
    {
        'name' : 'ram***',
        'age' : 18,
        'favourite_sport' : 'basketball'
    },

    {
        'name' : 'mona**',
        'age' : 19,
        'favourite_sport' : 'cricket'
    }
]
print('user :' , users[2]['name'])
print(users)

number_1 = ['one', 'two', 'three','four']
number_2 = [1, 2, 3, 4]
dictionary_1 = dict(zip(number_1,number_2))
print(dictionary_1)
dictionary = {}
for i in range(len(number_1)):
    dictionary[number_1[i]]= number_2[i]
print(dictionary)







'''person = {
    'name':'sia',
    'age': 6,
    'class': 'rose',
    'city': 'pune',
    'id': 123
}
person_1 = {
    'name': 14,
    'age': 66,
    'class': 2,
    'city': 23,
    'id': 45
}
for value in sorted(person_1.values()):
    print(value)
for value in sorted(person.keys()):
    print(value)

person['region'] = 'Maharashtra'
del person['class']

person['grade'] = 'KG'
print(person)
print(person.keys())
print(type(person['age']))
max_num=int(input("Enter the maximum number:  "))

def even_num(max):
    for i in range(max):
        if i%2 ==0:
            yield i

even = even_num(max_num)
for number in even:
    print(number)'''
