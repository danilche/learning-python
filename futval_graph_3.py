# futval_graph_3.py
from graphics import *


def drawbar(window, year, height):
    bar = Rectangle(Point(year, 0), Point(year + 1, height))
    bar.setFill("purple")
    bar.setWidth(2)
    bar.draw(window)

def main():
    # Introduction
    print("This program plots the growth of a 10-year investment.")
    
    # Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))
    
    # Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("aquamarine")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' O.OK').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5k').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    # Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        drawbar(win, year, principal)
        
    input("Press <Enter> to quit.")
    win.close()
main()