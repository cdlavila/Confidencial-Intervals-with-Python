from UI import interface
from Model import confidenceInterval as ci


interface.heading()
answer = interface.menu()

if answer == '1':
    mean, deviation, confidence = interface.readDataNormalDistribution()
    x1, x2, significancePoint = ci.confidenceIntervalForNormalDistribution(mean, deviation, confidence)
    print("\033[;36m" + f'THE RANDOM VARIABLE IS IN THE INTERVAL ({x1}, {x2})'
                        f' WITH A CONFIDENCE OF {confidence}%')
    ci.graphConfidenceInterval(mean, deviation, confidence, x1, x2, significancePoint * 100)

elif answer == '2':
    deviation, sample, sampleMean, confidence = interface.readDataPopulationMean()
    x1, x2, significancePoint = ci.confidenceIntervalForPopulationMean(deviation, sample, sampleMean, confidence)
    print("\033[;36m" + f'THE POPULATION AVERAGE μ IS IN THE INTERVAL ({x1}, {x2}) '
                        f'WITH A CONFIDENCE OF {confidence}%')
    ci.graphConfidenceInterval((x1+x2)/2, deviation, confidence, x1, x2, significancePoint * 100, False)
