'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million'''


def isprime(myNum):
    if(myNum < 2):
        return False
    #using 'is' instead of '=='
    elif(myNum is 2):
        return True
    #must define myNum as int, can't process float
    #Only need to process until .5 of myNum
    #range(start, finish, steps)
    for x in range(3, int(myNum*0.5)+1, 2): 
        if myNum % x == 0:
            return False
    return True
    
def main():
    mysum = 0
    for myNum in range(100):
        if(isprime(myNum) is True):
            mysum += myNum
        else:
            pass
    print(mysum) #ATTN: s not printing the correct numbers

if __name__ == "__main__":main()
