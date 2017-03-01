# Project:      Dice Program 
# Name:         Hans Christian
# Date:         03/07/14
# Description:  This program will allow the user to throw 5 dice, they will 
#               first enter a guess to their total of 5 dice (5-30) and the
#               program will give random dice roll

###########################################################################
#                               Dice Guessing                             #
###########################################################################
# NOTES: This program is not a perfect program, when you run it, please don't click
# anywhere outside the outline, else the program will stop working but you can click
# exit and no error message, However if you click on the entry straight away when the
# program is running and click on the assigned outline and in order from 1-5 the program
# will work fine and show the dice randomly.

# Import from the library
import random
from graphics import *

def makeDice(win):

    # Initialize
    DiceX = -0.1875
    FrameX = -0.5875
    DiceTotal = 0

    # For loop to draw the outline rectangle and dice text
    for i in range (5):
        FrameX = FrameX + 0.9375
        Frame = Rectangle(Point(FrameX,2.275),Point((FrameX+0.8),1.475))
        Frame.setOutline("Snow4")
        Frame.setWidth(4)
        Frame.draw(win)
        
        DiceX = DiceX + 0.9375
        DiceTotal = DiceTotal + 1
        DiceNumber = "Dice",DiceTotal
        DiceLabel = Text(Point(DiceX,1.875),DiceNumber)
        DiceLabel.setSize(16)
        DiceLabel.setFill("Snow4")
        DiceLabel.draw(win)

# Function 1 (FixedLayers):
def FixedLayers():

    # Window Setting(Color, size)
    win = GraphWin("5 Dice",600,300)
    win.setCoords(0.0,0.0,6.0,3.0)
    win.setBackground("LightBlue")

    makeDice(win)

    # Entry Text 
    EntryText = Text(Point(1.35,2.625),"Enter Your Guess (5-30)")
    EntryText.setSize(18)
    EntryText.setStyle("bold")
    EntryText.draw(win)

    # User Entry
    GuessUserEntry = Entry(Point(2.8,2.625),8)
    GuessUserEntry.setFill("White")
    GuessUserEntry.draw(win)

    # User Entry Frame
    UserInputFrame = Rectangle(Point(2.49,2.77),Point(3.11,2.5))
    UserInputFrame.setWidth(5)
    UserInputFrame.setOutline("Snow4")
    UserInputFrame.draw(win)

    # User Guess Text
    UserGuessText = Text(Point(0.80,1.3),"Your Guess")
    UserGuessText.setSize(18)
    UserGuessText.setFill("Snow4")
    UserGuessText.draw(win)

    # Random Dice total text
    DiceTotalText = Text(Point(1.85,1.3),"Dice Total")
    DiceTotalText.setSize(18)
    DiceTotalText.setFill("Snow4")
    DiceTotalText.draw(win)

    # Exit Rectangle frame
    ExitRect = Rectangle(Point(5.0,0.8),Point(5.7,0.55))
    ExitRect.setFill("Red")
    ExitRect.setOutline("Snow4")
    ExitRect.setWidth(4)
    ExitRect.draw(win)
    # Exit text 
    ExitRectLabel = Text(Point(5.35,0.675),"Exit")
    ExitRectLabel.setStyle("bold")
    ExitRectLabel.setFill("Seashell")
    ExitRectLabel.draw(win)

    # Returning to the main function
    return win, GuessUserEntry

# Function 2 (Main):
def main():

    # Initialize
    blnLoopRun1 = True
    blnLoopRun2 = True
    FrameX = -0.5875
    RectDice1X = -0.5625
    OneDotX = -0.1875
    TwoDotX1 = 0
    TwoDotX2 = -0.375
    TwoDotX3 = -0.375
    TwoDotX4 = 0
    TwoDotX5 = -0.375
    TwoDotX6 = 0
    intDiceTotal = 0
    Counter = 0

    # Sending the code to the first function
    # and receice the value and objects
    win,Guess_UserEntry = FixedLayers()

    # Dice total Number, random number added value output
    DiceTotalNumber = Text(Point(1.85,1.1),intDiceTotal)
    DiceTotalNumber.setSize(18)
    DiceTotalNumber.setFill("Snow4")
    DiceTotalNumber.draw(win)

    # While Loop
    while blnLoopRun1 == True:
        # Formula to count the loop
        Counter = Counter + 1
        # Setting the frame difference 
        FrameX = FrameX + 0.9375

        #Clicked mouse (getx, gety)
        ClickedDice = win.getMouse()
        XDice = ClickedDice.getX()
        YDice = ClickedDice.getY()

        # Decision if the user click in the outline 
        if XDice >= FrameX and XDice <= FrameX+0.8 and YDice >= 1.475 and YDice <= 2.275 and Counter < 6:
            # Converting the user entry into an integer
            intGuessUserEntry = int(Guess_UserEntry.getText())

            # User Guess Entry number output 
            UserGuessNumber = Text(Point(0.85,1.1),intGuessUserEntry)
            UserGuessNumber.setSize(18)
            UserGuessNumber.setFill("Snow4")
            UserGuessNumber.draw(win)

            # Create the dice frame whenever the outline is click
            RectDice1X = RectDice1X + 0.9375
            RectDice = Rectangle(Point(RectDice1X,2.25),Point((RectDice1X + 0.75),1.5))
            RectDice.setFill("White")
            RectDice.draw(win)

            # Random from 1 to 6 
            RandomDice = random.randint(1,6)
            # Calculate the total dice randomly in the loop
            intDiceTotal += RandomDice

            # Decision if the loop has gone by 5
            if Counter == 5:
                # Finding the difference between the user entry and the
                # random dice value
                GuessDifference = intGuessUserEntry - intDiceTotal

                # Decision to determine the difference in guessing
                if GuessDifference == 0:
                    UserText = Text(Point(1.05,0.375),"Your Guess is Right")
                    UserText.setSize(18)
                    UserText.setFill("Snow4")
                    UserText.draw(win)
                elif GuessDifference in {1,2,-1,-2}:
                    UserText = Text(Point(1.05,0.375),"Your Guess is Close")
                    UserText.setSize(18)
                    UserText.setFill("Snow4")
                    UserText.draw(win)
                else:
                    UserText = Text(Point(1.05,0.375),"Your Guess is Far")
                    UserText.setSize(18)
                    UserText.setFill("Snow4")
                    UserText.draw(win)
            
            # Replacing the value of Dice total every time this program loop
            DiceTotalNumber.setText(intDiceTotal)

            # Dice Dot formula
            OneDotX = OneDotX + 0.9375
            TwoDotX1 = TwoDotX1 + 0.9375
            TwoDotX2 = TwoDotX2 + 0.9375
            TwoDotX3 = TwoDotX3 + 0.9375
            TwoDotX4 = TwoDotX4 + 0.9375
            TwoDotX5 = TwoDotX5 + 0.9375
            TwoDotX6 = TwoDotX6 + 0.9375

            # Decison to draw the dice number (1-6):
            if RandomDice == 1:
                OneDot = Circle(Point(OneDotX,1.875),0.08)
                OneDot.setFill("Black")
                OneDot.draw(win)

            elif RandomDice == 2:
                TwoDot1 = Circle(Point(TwoDotX1,2.0625),0.08)
                TwoDot2 = Circle(Point(TwoDotX2,1.6875),0.08)
                TwoDot1.setFill("Black")
                TwoDot2.setFill("Black")
                TwoDot1.draw(win)
                TwoDot2.draw(win)

            elif RandomDice == 3:
                OneDot = Circle(Point(OneDotX,1.875),0.08)
                TwoDot1 = Circle(Point(TwoDotX1,2.0625),0.08)
                TwoDot2 = Circle(Point(TwoDotX2,1.6875),0.08)
                OneDot.setFill("Black")
                TwoDot1.setFill("Black")
                TwoDot2.setFill("Black")
                OneDot.draw(win)
                TwoDot1.draw(win)
                TwoDot2.draw(win)
                
            elif RandomDice == 4:
                TwoDot1 = Circle(Point(TwoDotX1,2.0625),0.08)
                TwoDot2 = Circle(Point(TwoDotX2,1.6875),0.08)
                TwoDot3 = Circle(Point(TwoDotX3,2.0625),0.08)
                TwoDot4 = Circle(Point(TwoDotX4,1.6875),0.08)
                TwoDot1.setFill("Black")
                TwoDot2.setFill("Black")
                TwoDot3.setFill("Black")
                TwoDot4.setFill("Black")
                TwoDot1.draw(win)
                TwoDot2.draw(win)
                TwoDot3.draw(win)
                TwoDot4.draw(win)
                
            elif RandomDice == 5:
                OneDot = Circle(Point(OneDotX,1.875),0.08)
                TwoDot1 = Circle(Point(TwoDotX1,2.0625),0.08)
                TwoDot2 = Circle(Point(TwoDotX2,1.6875),0.08)
                TwoDot3 = Circle(Point(TwoDotX3,2.0625),0.08)
                TwoDot4 = Circle(Point(TwoDotX4,1.6875),0.08)
                OneDot.setFill("Black")
                TwoDot1.setFill("Black")
                TwoDot2.setFill("Black")
                TwoDot3.setFill("Black")
                TwoDot4.setFill("Black")
                OneDot.draw(win)
                TwoDot1.draw(win)
                TwoDot2.draw(win)
                TwoDot3.draw(win)
                TwoDot4.draw(win)
                
            else:
                TwoDot1 = Circle(Point(TwoDotX1,2.0625),0.08)
                TwoDot2 = Circle(Point(TwoDotX2,1.6875),0.08)
                TwoDot3 = Circle(Point(TwoDotX3,2.0625),0.08)
                TwoDot4 = Circle(Point(TwoDotX4,1.6875),0.08)
                TwoDot5 = Circle(Point(TwoDotX5,1.875),0.08)
                TwoDot6 = Circle(Point(TwoDotX6,1.875),0.08)
                TwoDot1.setFill("Black")
                TwoDot2.setFill("Black")
                TwoDot3.setFill("Black")
                TwoDot4.setFill("Black")
                TwoDot5.setFill("Black")
                TwoDot6.setFill("Black")
                TwoDot1.draw(win)
                TwoDot2.draw(win)
                TwoDot3.draw(win)
                TwoDot4.draw(win)
                TwoDot5.draw(win)
                TwoDot6.draw(win)

        # Decision if the user click on the set coordinates, which is the exit
        # button, the program will stop the loop and close the window
        if XDice > 4.9 and XDice < 5.8 and YDice < 0.9 and YDice > 0.54:
            win.close()
            blnLoopRun1 = False

# Calling the main fucntion           
main()
