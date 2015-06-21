using System;
using System.Collections.Generic;
using System.Text;

namespace FuzzyLogic
{
    class Famm
    {
        Double w1, w2, w3, w4, w5, w6, w7, w8, w9;

        //Direction trapezoidal member functinos
        public Double angleSmall(Double theta) 
        {
            Trapezoid aSmall = new Trapezoid(-1, 0, 45, 60);

            return aSmall.GetOutput(theta);
        }
        
        public Double angleMedium(Double theta) 
        {
            Trapezoid aMedium = new Trapezoid(55, 85, 95, 105);

            return aMedium.GetOutput(theta);
        }

        public Double angleLarge(Double theta)
        {
            Trapezoid aLarge = new Trapezoid(75, 110, 115, 180);

            return aLarge.GetOutput(theta);
        }


        //Distance trapezoidal member functions
        public Double distSmall(Double distance) 
        {
            Trapezoid dSmall = new Trapezoid(-1, 12, 25, 40);

            return dSmall.GetOutput(distance);
        }

        public Double distMedium(Double distance)
        {
            Trapezoid dMedium = new Trapezoid(30, 55, 65, 75);

            return dMedium.GetOutput(distance);
        }

        public Double distLarge(Double distance)
        {
            Trapezoid dLarge = new Trapezoid(70, 90, 100, 150);

            return dLarge.GetOutput(distance);
        }

        public Double deffuzify()
        {
            Double temp;
            temp = (w1 * 90) + (w2 * 55) + (w3 * 35) + 
                    (w4 * 55) + (w5 * 35) + (w6 * 20) + 
                    (w7 * 35) + (w8 * 20) + (w9 * 5);

            if ((w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9) == 0)
            {
                return 0;
            }
            else
            {
                return temp / (w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9);
            }
        }


        public Famm(Double obsAngle, Double obsDistance)
        {
            obsAngle = Math.Abs(obsAngle);

            w1 = (angleSmall(obsAngle) * distSmall(obsDistance));
            w2 = (angleSmall(obsAngle) * distMedium(obsDistance));
            w3 = (angleSmall(obsAngle) * distLarge(obsDistance));
            w4 = (angleMedium(obsAngle) * distSmall(obsDistance));
            w5 = (angleMedium(obsAngle) * distMedium(obsDistance));
            w6 = (angleMedium(obsAngle) * distLarge(obsDistance));
            w7 = (angleLarge(obsAngle) * distSmall(obsDistance));
            w8 = (angleLarge(obsAngle) * distMedium(obsDistance));
            w9 = (angleLarge(obsAngle) * distLarge(obsDistance));
        
            //w1 = ((angleSmall(obsAngle) + distSmall(obsDistance)) - (angleSmall(obsAngle) * distSmall(obsDistance)));
            //w2 = ((angleSmall(obsAngle) + distMedium(obsDistance)) - (angleSmall(obsAngle) * distMedium(obsDistance)));
            //w3 = ((angleSmall(obsAngle) + distLarge(obsDistance)) - (angleSmall(obsAngle) * distLarge(obsDistance)));
            //w4 = ((angleMedium(obsAngle) + distSmall(obsDistance)) - (angleMedium(obsAngle) * distSmall(obsDistance)));
            //w5 = ((angleMedium(obsAngle) + distMedium(obsDistance)) - (angleMedium(obsAngle) * distMedium(obsDistance)));
            //w6 = ((angleMedium(obsAngle) + distLarge(obsDistance)) - (angleMedium(obsAngle) * distLarge(obsDistance)));
            //w7 = ((angleLarge(obsAngle) + distSmall(obsDistance)) - (angleLarge(obsAngle) * distSmall(obsDistance)));
            //w8 = ((angleLarge(obsAngle) + distMedium(obsDistance)) - (angleLarge(obsAngle) * distMedium(obsDistance)));
            //w9 = ((angleLarge(obsAngle) + distLarge(obsDistance)) - (angleLarge(obsAngle) * distLarge(obsDistance)));
            
        }
    }
}
