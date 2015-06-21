using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Windows.Threading;
using System.Threading;
using System.ServiceModel.Dispatcher;
using System.ComponentModel;


namespace FuzzyLogic
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>

    public partial class Window1 : System.Windows.Window
    {
        Sprite car;
        Boolean animationStart = false;

        public Window1()
        {
            InitializeComponent();
            car = new Sprite();
        }

        public delegate void CheckPosition();

        protected void btnAnimateClick(object sender, EventArgs e)
        {            
            car.Initialize(Canvas.GetRight(sprCar), Canvas.GetTop(sprCar), 10);
                        
            AnimateCar();

            if (!animationStart)
            {
                DoubleAnimation sprite1 = new DoubleAnimation(Canvas.GetTop(sprPerson5)+150, TimeSpan.FromSeconds(5));
                sprite1.AutoReverse = true;
                animationStart = true;
                sprite1.Completed += new EventHandler(Animation_Completed);

                sprPerson5.BeginAnimation(Canvas.TopProperty, sprite1);
            }
        }

        void Animation_Completed(object sender, EventArgs e)
        {
            DoubleAnimation sprite1 = new DoubleAnimation(Canvas.GetTop(sprPerson5) + 150, TimeSpan.FromSeconds(5));
            sprite1.AutoReverse = true;
            animationStart = true;
            sprite1.Completed += Animation_Completed;

            sprPerson5.BeginAnimation(Canvas.TopProperty, sprite1);

            DoubleAnimation sprite2 = new DoubleAnimation(Canvas.GetRight(sprPerson4) - 150, TimeSpan.FromSeconds(5));
            sprite2.AutoReverse = true;
            sprPerson4.BeginAnimation(Canvas.RightProperty, sprite2);                        
        }

        private void AnimateCar()
        {
            UpdateStatistics();
            Double temp = car.angle;

            car.PointTowardsDestination();

            CheckForCollision();

            SmoothCarHeading(temp);

            sprCar.RenderTransform = new RotateTransform(car.angle, sprCar.ActualWidth/2, sprCar.ActualHeight/2);
                        
            car.MoveInDirection(car.angle);
                      
            //Final Direction should be determined before this point
            DoubleAnimation sprCarX = new DoubleAnimation(car.xPos, TimeSpan.FromMilliseconds(car.xDuration));            
            DoubleAnimation sprCarY = new DoubleAnimation(car.yPos, TimeSpan.FromMilliseconds(car.yDuration));

            if (!DestinationReached())
            {                
                sprCarY.Completed += btnAnimateClick;
            }
            
            sprCar.BeginAnimation(Canvas.RightProperty, sprCarX);
            sprCar.BeginAnimation(Canvas.TopProperty, sprCarY);                                    
        }

        private void SmoothCarHeading(Double prevAngle)
        {
            Double newHeading = car.angle;

            if (newHeading - prevAngle > 4)
            {
                if (newHeading - prevAngle > 180) { car.angle = prevAngle - 5; } else { car.angle = prevAngle + 4; }
            }
            else if (car.angle - prevAngle < -4)
            {
                if (newHeading - prevAngle < -180) { car.angle = prevAngle + 5; } else { car.angle = prevAngle - 4; }
            }

            if (car.angle < 0) { car.angle += 360; }
            else if (car.angle > 360) { car.angle -= 360; }
        }

        private void adjustAngle(Double pAngle, Double obstacleDist)
        {
            lblStatus.Content = "Obstacle angle: " + pAngle.ToString() + "Dist: " + obstacleDist.ToString();
            
            Famm famm = new Famm(pAngle, obstacleDist);

            Double adjAngle = famm.deffuzify();

            //if (Math.Abs(adjAngle - pAngle) > 10) { adjAngle /= 2; }

            if (pAngle > 0) { adjAngle *= -1; }
                        
            if (car.angle + adjAngle > 360) { car.angle = (car.angle + adjAngle) - 360; }
            else if (car.angle + adjAngle < 0) { car.angle = car.angle + adjAngle + 360; }
            else { car.angle += adjAngle; }            
        }

        private void CheckForCollision()
        {
            Point carPosition = new Point();
            Double pAngle = 0, obstacleDist = 0;

            Double adjAngle = 360, adjDistance = 10000;
            
            carPosition.X = Canvas.GetRight(sprPerson1);// + 25;
            carPosition.Y = Canvas.GetTop(sprPerson1) + 10;

            if (car.CheckCollsions(ref obstacleDist, carPosition, ref pAngle))
            {
                if (obstacleDist < adjDistance)
                {
                    adjAngle = pAngle;
                    adjDistance = obstacleDist;
                }
                //adjustAngle(pAngle, obstacleDist);
            }

            carPosition.X = Canvas.GetRight(sprPerson2);// + 25;
            carPosition.Y = Canvas.GetTop(sprPerson2) + 10;

            if (car.CheckCollsions(ref obstacleDist, carPosition, ref pAngle))
            {
                if (obstacleDist < adjDistance)
                {
                    adjAngle = pAngle;
                    adjDistance = obstacleDist;
                }
                //adjustAngle(pAngle, obstacleDist);
            }

            carPosition.X = Canvas.GetRight(sprPerson3);// + 25;
            carPosition.Y = Canvas.GetTop(sprPerson3) + 10;

            if (car.CheckCollsions(ref obstacleDist, carPosition, ref pAngle))
            {
                if (obstacleDist < adjDistance)
                {
                    adjAngle = pAngle;
                    adjDistance = obstacleDist;
                }
                //adjustAngle(pAngle, obstacleDist);
            }

            carPosition.X = Canvas.GetRight(sprPerson4);// + 25;
            carPosition.Y = Canvas.GetTop(sprPerson4) + 10;

            if (car.CheckCollsions(ref obstacleDist, carPosition, ref pAngle))
            {
                if (obstacleDist < adjDistance)
                {
                    adjAngle = pAngle;
                    adjDistance = obstacleDist;
                }
                //adjustAngle(pAngle, obstacleDist);
            }

            carPosition.X = Canvas.GetRight(sprPerson5);// + 25;
            carPosition.Y = Canvas.GetTop(sprPerson5) + 10;

            if (car.CheckCollsions(ref obstacleDist, carPosition, ref pAngle))
            {
                if (obstacleDist < adjDistance)
                {
                    adjAngle = pAngle;
                    adjDistance = obstacleDist;
                }
                //adjustAngle(pAngle, obstacleDist);
            }

            if (adjDistance < 10000) { adjustAngle(adjAngle, adjDistance); }
        }

        private bool DestinationReached()
        {
            if (Math.Abs((car.xDestination - car.xPos)) < 5)
            {
                if (Math.Abs((car.yDestination - car.yPos)) < 5) { return true; }
            }
            return false;
        }

        protected void NewDestination(object sender, MouseButtonEventArgs e)
        {
            Point p = e.GetPosition(mainCanvas);
            p.X = this.ActualWidth - p.X;
            car.SetDestination(p.X - 50, p.Y - 10);

            sprTarget.Visibility = Visibility.Visible;
            Canvas.SetRight(sprTarget, p.X - (sprTarget.ActualWidth) + 5);
            Canvas.SetTop(sprTarget, p.Y - (sprTarget.ActualHeight/2));

            AnimateCar();
        }

        private void UpdateStatistics()
        {
            lblAngle.Content = car.angle.ToString();
            lblDestination.Content = "x: " + car.xDestination.ToString() + "  y:" + car.yDestination.ToString();            
        }
    }
}