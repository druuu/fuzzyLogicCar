class Fuzzylogic: 

    fuzzyList = []
    def trapezoid(self, a, b, c, d, xValue):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.xValue = xValue
        nextY = float((self.xValue - self.a)) / (self.b - self.a)
        nowY = float((self.d - self.xValue)) / (self.d - self.c)
        y = min(nextY, min(1, nowY))
        return max(y, 0)

    def angleSmall(self, theta):
        return self.trapezoid(-1, 0, 45, 60, theta)
    def angleMedium(self, theta):
        return self.trapezoid(55, 85, 95, 105, theta)
    def angleLarge(self, theta):
        return self.trapezoid(75, 110, 115, 180, theta)

    def distSmall(self, dist):
        return self.trapezoid(-1, 12, 25, 40, dist)
    def distMedium(self, dist):
        return self.trapezoid(30, 55, 65, 75, dist)
    def distLarge(self, dist):
        return self.trapezoid(70, 90, 100, 150, dist)

    def fuzzy(self, objAngle, objDist):
        objAngle = abs(objAngle)
        self.fuzzyList.append((self.angleSmall(objAngle) * self.distSmall(objDist)))
        self.fuzzyList.append((self.angleSmall(objAngle) * self.distMedium(objDist)))
        self.fuzzyList.append((self.angleSmall(objAngle) * self.distLarge(objDist)))
        self.fuzzyList.append((self.angleMedium(objAngle) * self.distSmall(objDist)))
        self.fuzzyList.append((self.angleMedium(objAngle) * self.distMedium(objDist)))
        self.fuzzyList.append((self.angleMedium(objAngle) * self.distLarge(objDist)))
        self.fuzzyList.append((self.angleLarge(objAngle) * self.distSmall(objDist)))
        self.fuzzyList.append((self.angleLarge(objAngle) * self.distMedium(objDist)))
        self.fuzzyList.append((self.angleLarge(objAngle) * self.distLarge(objDist)))


    def deFuzzy(self):
        tempList = [90, 55, 35, 55, 35, 20, 35, 20, 5]
        j = 0
        val = 0
        massDist = 0
        for t in self.fuzzyList:
            val = val + t
        for i in tempList:
            massDist += self.fuzzyList[j] * i
            j += 1

        return float(massDist / val)


fl = Fuzzylogic()
fl.fuzzy(51 , 34)
print fl.deFuzzy()

