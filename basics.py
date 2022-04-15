#!/usr/bin/python3

import sys, re

fruit = 'apple'
isCool = True

# IF STATEMENT
if fruit == 'banana' or fruit == 'orange':
    print('Yay!')
elif (fruit == 'kiwi') and not isCool:
    print('Yay2!')
else:
    print('Yay3!')

# FOR LOOP
testList = ['Hej<id>a1</id>då', 'Test<id>b2</id>123', 'Banana<id>c3</id>phone']
for test in testList:
    # REGEX
    id = re.search('<id>(.*)</id>', test)
    print(id.group())


# TODO WIP add more examples


print('WOHOO!')

