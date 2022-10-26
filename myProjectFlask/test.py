ice = 0
room = 27
body = 32
boiling = 100

# and is not or 
# <, >, <=, >=, ==, !=

# # and operator
#         0             1          0

# if statement 
# match case statement
name = 'samuel'
if name == 'joseph':
    print(name)
# if elif else chain

name = 'samuel'
if name == 'joseph':
    print(name)
elif name == 'samuuel':
    print('you are not allowed')
else:
    print('please get out')

if name == 'joseph':
    print(name)
if name == 'samuel':
    print('you are not allowed')
# if name != 'joseph' and name != 'samuel':
#     print('get out')

match (name == 'joseph'):
    case True:
        print(name)
    case False:
        print('get out')
 
    
# for n in name:
#     print(n)

# for i in range(2, 10, 3):
#     print(i)

names = [['joseph', 'isaac', 'samuel', 'vincent', 'joshua'], ['sarah', 'claudia', 'angel', 'chioma']]


