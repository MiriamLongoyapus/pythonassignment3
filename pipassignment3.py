# Write a Python program that takes a list of strings as input
#  and outputs the number of times each string appears in the list, 
# using a dictionary and conditional statements.
def count_text(str):
    count=dict()
    text=str.split()
    for text in text:
        if text in count:
            count[text] +=1
        else:
            count[text]= 1
    return count
print(count_text("hey,write a python a code code"))

# Write a Python program that takes a list of numbers as input and 
# outputs the median of the numbers 
def median_number(num):
    num=[10,20,30,40,50]
    num.sort()
    length=len(num)
    median=len(num)/2
    if length%2==0:
        return(num[median -1]+ num[median])/2
    else: 
        return num[median]
    print(median_number([10,20,30,40,50]))


# Write a Python program that takes a list of numbers as input and 
# outputs the second largest number in the list using conditional statements
#  and a for loop.
def second_largest(nums):
    largest_number=0
    second_largestnumber=0
    for i in range(len(nums)):
        if nums[i]>largest_number:
            second_largestnumber=largest_number
            largest_number=nums[i]
        elif nums[i] >second_largestnumber:
            second_largestnumber=nums[i]
    return second_largestnumber
print(second_largest([1,5,7,3,10]))





# Write a Python program that takes a year as input and determines if 
# it :
leap=(2004)
if leap%4==0:
    print("year is leap")
else:
    print("year is not leap")

# Write a Python program that takes a string as input and checks if it is 
# a palindrome (reads the same forwards and backwards), ignoring spaces and 
# punctuation.
def ispalindrome(string):
    return string==string[::-1]
sting="noon"
ans=ispalindrome("noon")
if ans:
    print("true")
else:
    print("false")