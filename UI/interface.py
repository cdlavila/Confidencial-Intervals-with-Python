def heading():
    print('\nCONFIDENCE INTERVALS AND SIGNIFICANCE POINTS')


def menu():
    print('OPTIONS')
    print('\t1. Calculate the confidence interval with the normal distribution')
    print('\t2. Calculate the confidence interval for the population mean')
    answer = input('Which option do you choose (1/2)?: ')
    if answer == '1' or answer == '2':
        return answer
    else:
        print('\nWrong option, try again\n')
        return menu()


def readDataNormalDistribution():
    print('\nConsidering the normal distribution N(μ,σ): ')
    mean = float(input('\tInput the population mean μ: '))
    deviation = float(input('\tInput the standard deviation σ: '))
    confidence = float(input('\tInput the confidence level you want to calculate(%): '))
    return [mean, deviation, confidence]


def readDataPopulationMean():
    print('\nConsidering the normal distribution N(μ,σ)')
    deviation = float(input('\tInput the standard deviation σ: '))
    sample = float(input('\tInput the sample size N: '))
    sampleMean = float(input('\tInput the sample mean X-: '))
    confidence = float(input('\tInput the confidence level you want to calculate(%): '))
    return [deviation, sample, sampleMean, confidence]
