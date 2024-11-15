# linear time space complexity
# run in constant time
a = 4
sum = a + 10
print(sum)


str = "hello"
print(str[1]) #getting item at index 1 of a string array has constant time


stuff = {'a':1, 'b': 2, 'c': 3}
print('b' in stuff) #checking for b in stuff has a constant time lookup
print(stuff['b']) #printing the value of b

colors = ['red', 'blue', 'green', 'yellow', 'margenta']
print('green' in colors) #this is going to have a linear(0(n)) lookup time (lists and dictionaries are different )



list = [5, 9, 2, -6, 12, 20, 30, 24]
sum = 0
for item in list: #time complexity(0(n)) comes from this for loop as it iterates through a list of items
    sum += item 
print(sum)


sentence = "hello world, how are you?"
print(sentence.split(" ")); #this has a (0(n)) as it iterates and checks for a space and split that sentence into chunks


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for letter1 in letters:
    for letter2 in letters:
        print(letter1 + ' ' + letter2);

#here we have nested loop  n = letters length
#our code has iterate through letters with first loop, then the second loop
# it has a time complexity of time: 0(n * n) which is outer loop n(complexity) multiplied by inner loop n(complexity)
# that can be simplified to n * n = 0(n^2)


def function2(n):
    for i in range(0, int(n/2)):
        print(i)

function2(20)

# this iterates through 20 digits and divides them by 2 
# n
#Time: 0(n/2)
#but we can remove constant to make it 0(n)
# since the print(i) is not adding any complex calculation we have Space: 0(1)

def function3(n):
    nums = []
    for i in range(1, n):
        nums.append(i)
    return nums;

print(function3(10))

# Here we are also iterating through a range of numbers and appending them to nums list
# since append only add one item it has Time: 0(n)
#since we are also not using much space we have Space: 0(n)


def function4(n):
    nums = []
    for i in range(1, n):
        nums.insert(0, i)
    return nums

print(function4(10))
# here we are iterating through a range of numbers with for i in range(1, n):
# then we are inserting each number at the start (0) of the array
#our numbers will be in a decreasing order, from largest to smallest
# this will give us Time: 0(n * n) which is 0(n^2)
# why is this 0(n * n)? because we have to shift elemnts each time we insert a new one in front
# space complexity stays the same Space: 0(n)


def function5(s):
    for char1 in s:
        for char2 in s:
            print(char1 + ',' + char2)
    for char1 in s:
        print(char1)

function5('qrs')

# here we first going to have n = string length
# then we have nested loops which will give us time complexity of Time: 0(n * n) = 0(n^2)
# then we have a loop that is separate, not nested in the above loops which just iterates and prints items
# that gives us just 0(n)
# together we can write them as Time : 0(n^2 + n)
# but following the rule of droping constants, we should have only Time: 0(n^2)

# this is going to give us contsant space complexity Space: 0(1)

def function6(s):
    for char1 in s:
        print(char1)

    for char1 in s:
        print(char1)

    for char1 in s:
        print(char1)

    for char1 in s:
        print(char1)

function5('qrs')

# if we have loops like this, we have a time complexity of Time : 0(n + n + n + n)
# which is same as Time: 0(4n)
# following the rule to remove constants we should have Time : 0(n)


def function6(s):
    for char1 in s:
        print(char1)
        for char1 in s:
            print(char1)
            for char1 in s:
                print(char1)
                for char1 in s:
                    print(char1)

function5('qrs')

# however, if we have them nested like above, we are increasing the calculation time, increasing the complexity
# this means we have to multiply them Time: 0(n * n * n * n)
# which is same as Time: 0(n^4)
