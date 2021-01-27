import numpy
import scipy.stats as st
from matplotlib import pyplot
import math


def confidenceIntervalForNormalDistribution(mean, deviation, confidence):
    confidence /= 100
    significancePoint = 1 - confidence
    z = st.norm.ppf(confidence + significancePoint/2)  # This function looking for in the Standard normal table
    z = round(z, 2)  # We round z to 2 decimals
    x1 = mean - z*deviation
    x1 = round(x1, 2)

    x2 = mean + z*deviation
    x2 = round(x2, 2)
    return [x1, x2, significancePoint]


def confidenceIntervalForPopulationMean(deviation, sample, sampleMean, confidence):
    confidence /= 100
    significancePoint = 1 - confidence
    z = st.norm.ppf(confidence + significancePoint/2)  # This function looking for in the Standard normal table
    z = round(z, 2)  # round function rounds a number to decimals what you want
    x1 = sampleMean - z*(deviation/math.sqrt(sample))
    x1 = round(x1, 2)

    x2 = sampleMean + z*(deviation/math.sqrt(sample))
    x2 = round(x2, 2)
    return [x1, x2, significancePoint]


def graphConfidenceInterval(mean, deviation, confidence, x1, x2, significancePoint, printMean=True):
    x = numpy.linspace(mean - 3 * deviation, mean + 3 * deviation, 300)
    function = (1 / (deviation * math.sqrt(2 * math.pi))) * math.e ** ((-1 / 2) * (((x - mean) / deviation) ** 2))

    pyplot.title('Intervalo De Confianza')
    pyplot.grid()
    pyplot.fill_between(x, function, 0,
                        where=(x > x1) & (x < x2),
                        color='c')
    pyplot.fill_between(x, function, 0,
                        where=(x >= mean - 3 * deviation) & (x <= x1),
                        color='y')
    pyplot.fill_between(x, function, 0,
                        where=(x >= x2) & (x <= mean + 3 * deviation),
                        color='y'
                        )
    pyplot.plot(x, function)
    meanInY = (1 / (deviation * math.sqrt(2 * math.pi))) * math.e ** ((-1 / 2) * (((mean - mean) / deviation) ** 2))
    if printMean:
        pyplot.plot(mean, meanInY, marker=".", color="r")
        pyplot.text(mean, meanInY, f"μ={mean}", fontsize=15)
    else:
        pyplot.text(mean, meanInY, "μ", fontsize=20)

    pyplot.text(mean - deviation / 3, meanInY / 2, f"{confidence}%", fontsize=25)
    pyplot.plot(x1, 0, marker=".", color="r")
    pyplot.text(x1, meanInY/25, f"X1={x1}")
    pyplot.plot(x2, 0, marker=".", color="r")
    pyplot.text(x2, 0, f"X2={x2}")
    a = (1 / (deviation * math.sqrt(2 * math.pi))) * math.e ** (
                (-1 / 2) * (((((mean - 3 * deviation) + x1) / 2 - mean) / deviation) ** 2))
    b = (1 / (deviation * math.sqrt(2 * math.pi))) * math.e ** (
                (-1 / 2) * (((((mean + 3 * deviation) + x2) / 2 - mean) / deviation) ** 2))
    pyplot.text(((mean - 4.05 * deviation) + x1) / 2, a, f"{round(significancePoint / 2, 1)}%", fontsize=15)
    pyplot.text(((mean + 3 * deviation) + x2) / 2, b, f"{round(significancePoint / 2, 1)}%", fontsize=15)
    pyplot.show()
