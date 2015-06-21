using System;
using System.Collections.Generic;
using System.Text;

namespace FuzzyLogic
{
    class Trapezoid
    {
        Double a, b, c, d;

        public Trapezoid(Double pointA, Double pointB, Double pointC, Double pointD)
        {
            a = pointA;
            b = pointB;
            c = pointC;
            d = pointD;
        }

        public Double GetOutput(Double input)
        {
            Double temp, temp2;

            temp = (input - a) / (b - a);
            temp2 = (d - input) / (d - c);

            temp = Math.Min(temp, Math.Min(1, temp2));

            return (Math.Max(temp, 0));
        }
    }
}
