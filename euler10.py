'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million'''
def isprime(myNum):
    if myNum < 2 :
        return False
    #using 'is' instead of '=='
    if myNum == 2 :
        return True
    #must define myNum as int, can't process float
    #Only need to process until .5 of myNum
    #range(start, finish, steps)
    myMax = myNum**0.5+1
    for x in range(3, int(myMax), 2):
        if myNum % x == 0:
            return False
    return True
    
def main():
    mysum = 2
    for myNum in range(3, 2000000, 2):
        if(isprime(myNum) is True):
            mysum += myNum

    print(mysum)

if __name__ == "__main__":main()