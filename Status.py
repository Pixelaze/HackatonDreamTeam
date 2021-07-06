import Enum

class StatusAnalyzer:
    def __init__(self):
        pass

    def analyzeStatus(self, co2, temp, noise):
        co2rank = (co2 - 1200) / 30
        if (co2rank < 0):
            co2rank = 0

        temprank = abs((temp - 24) / 2.5)
        humrank = abs((hum - 50) / 2)

        if (noise < 70):
            noiserank = 0
        if (noise >= 70):
            noiserank = (noise - 70) / 10

        rank = 100 - co2rank - noiserank - humrank - temprank

        if (rank >= 90):
            return Enum.STATUS.BEST, rank, self.getRecomendations(co2, temp, noise)
        elif (rank >= 70):
            return Enum.STATUS.GOOD, rank, self.getRecomendations(co2, temp, noise)
        elif (rank >= 50):
            return Enum.STATUS.MEDIUM, rank, self.getRecomendations(co2, temp, noise)
        elif (rank >= 20):
            return Enum.STATUS.BAD, rank, self.getRecomendations(co2, temp, noise)
        else:
            return Enum.STATUS.WORST, rank, self.getRecomendations(co2, temp, noise)
    
    def getRecomendations(self, co2, temp, noise):
        returning = ""
        if (temp < 16):
            returning += Enum.LOCALE['too_small_temperature'] + "\n"
        elif (temp > 33):
            returning += Enum.LOCALE['too_big_temperature'] + "\n"

        if (co2 > 2200):
            returning += Enum.LOCALE['big_co2_count'] + "\n"
        elif (co2 > 3500):
            returning += Enum.LOCALE['really_big_co2_count'] + "\n"

        if (noise >= 90 and noise < 110):
            returning += Enum.LOCALE['big_noise'] + "\n"
        elif (noise >= 110):
            returning += Enum.LOCALE['really_big_noise'] + "\n"
        
        return returning