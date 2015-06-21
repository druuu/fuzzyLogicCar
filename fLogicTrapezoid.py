class Trapezoid:
    def getOutput(self, a, b, c, d, xValue):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.xValue = xValue

        nextY = (self.xValue - self.a) / (self.b - self.a)
        nowY = (self.d - self.xValue) / (self.d - self.c)

        y = min(nextY, min(1, nowY))
        
        return max(y, 0)
         

