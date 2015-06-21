class Fuzzylogic: 

    fuzzyList = []
    def triangle(self, a, b, c, xValue):
        self.a = a
        self.b = b
        self.c = c
        self.xValue = xValue
        y = (1 - (float(abs(b - xValue)) / (b - a)))
        return max(y, 0)

    def verySmall(self, val):
        return self.triangle(0, 20, 40, val), self.centroid(0, 20, 40)
    def Small(self, val):
        return self.triangle(30 , 50, 70, val), self.centroid(30 , 50, 70)
    def Medium(self, val):
        return self.triangle(60, 80, 100, val), self.centroid(60, 80, 100)
    def Large(self, val):
        return self.triangle(90, 110, 130, val), self.centroid(90, 110, 130)
    def veryLarge(self, val):
        return self.triangle(120, 140, 160, val), self.centroid(120, 140, 160)

    def fuzzy(self, val):
        self.fuzzyList = []
        self.fuzzyList.append(self.verySmall(val))
        self.fuzzyList.append(self.Small(val))
        self.fuzzyList.append(self.Medium(val))
        self.fuzzyList.append(self.Large(val))
        self.fuzzyList.append(self.veryLarge(val))

        #print self.fuzzyList


    def centroid(self, l, m, r):
        width = abs(r - l)
        hieght = 1
        area = float(width) / 2
        moment = (float(1) / 6)*(r*(r + m) - l*(l + m))
        #print moment
        centroid = float(moment/area)

        return centroid

    def deFuzzy(self):
        j = 0
        total = 0
        for t,t1 in self.fuzzyList:
            total = total + t*t1

        if total == 0:
            return 0

        return total


fl = Fuzzylogic()
#fl.fuzzy(159)
#print fl.deFuzzy()

