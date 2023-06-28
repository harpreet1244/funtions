##this funtion is created to get the even factors of a number##
def count_prime(nums):

    count = 0
    if nums < 2 :
        return 0
    
    prime = [2]

    x = 3
    while x <= nums:
        ##check if x is prime
        for y in prime :
            if x % y == 0:
                x += 2
                break

        else:
            prime.append (x)
            x += 2 

    print(prime)
    return len(prime)





print(count_prime(10))




### MAP FUNCTION: - ######

def divide(num):
    return num % 2

my_list = [2,5,9,11]

for i in map(divide,my_list):
    print(i)


#####filter function####

def check_even(num):
    return num % 2 == 0


my_list = [1,2,3,4,5,6,7,8,9]
for n in filter(check_even,my_list):
    print(n)



###lamda funtion###
my_list = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda num:  num % 2  , my_list)))


