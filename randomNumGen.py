from numpy.random import randint


class RandomNumber:
    '''The amount variable depicts how many random numbers will be returned
       the minRange variable depicts the starting range of the random number
       the maxRange variable depicts the maximum number that the random number could be
       '''
    def __init__(self, amount:int, minRange:int, maxRange:int):

        if isinstance(amount, int) and amount > 0:
            self.amount = amount
        else:
            raise Exception('amount must be an integer greater than 0')

        if isinstance(minRange, int) and minRange < maxRange:
            self.minRange = minRange
        else:
            raise Exception('minRange must be integer and less than maxRange')

        if isinstance(maxRange, int) and maxRange > minRange:
            self.maxRange = maxRange
        else:
            raise Exception('maxRange must be integer greater than minRange')


    def randomNumGenerator(self):
        numberlist = []
        minRange = self.minRange
        maxRange = self.maxRange
        for i in range(self.amount):
            randomNumber = randint(minRange,maxRange)
            numberlist.append(randomNumber)
        for number in numberlist:
            print(number)

if __name__ == "__main__":

    amount = int(input('how many random numbers will be returned?'))
    minRange = int(input('what is the starting range of the random number?'))
    maxRange = int(input('what is the maximum value of the random number?'))
    r1 = RandomNumber(amount,minRange,maxRange)
    r1.randomNumGenerator()
    print(f'Amount:{r1.amount}, minRange:{r1.minRange},maxRange:{r1.maxRange}')


