"""
    Made By: Marwan Alhindi
    Created On: 25 July 2022
    From: Python Crash Course
    This file is used to analyse the probability of the number that would occur when rolling one, two or multiple dices. By using Plotly, we will have an interactive plots for the user to represent each number occuarance probability. You learned how to use the function Bar and the function Layout from plotl (x,y titles and the graph title). The result of this file was that when a single D6 dice is being rolled E.g. 1000 times, the probability distribution of each side is equal. But when you roll two dice together, the most frequent number occur is 7.

    The Data Visualization project starts in Chapter 15, in which you'll learn to generate data and create a series of functional and beautiful visualizations of that data using Matplotlib and Plotly. Chapter 16 teaches you to access data from online sources and feed it into a visualization package to create plots of weather data and a map of global earthquake activity. Finally, Chapter 17 shows you how to write a program to automatically download and visualize data. Learning to make visualizations allows you to explore the field of data mining, which is a highly sought-after skill in the world today.
"""

import plotly as plt
from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die:
    """
        This class is used to roll a dice that has a specific side that the user can determined.
    """

    def __init__(self,num_sides= 6):
        """
            This class has only one attribute which is the number of sides of the dice.
        """

        self.num_sides = num_sides

    def roll(self):
        """
            This method uses the function randint to roll a dice.
        """

        result = randint(1,self.num_sides)

        return result

#6-sided dice
D6 = Die()


#rolling the dice 1000 times
roll_results = []
for roll in range(1000):
    roll_results.append(D6.roll())

#counting the frequency of each side
frequiences = []
for side in range(1,D6.num_sides+1):
    frequency = roll_results.count(side)
    frequiences.append(frequency)

print(sum(frequiences))
#using plotly to plot a bar chart
x_values = list(range(1,D6.num_sides+1))
y_values = [Bar(x= x_values,y= frequiences)]
x_title = {'title':'side'}
y_title = {'title':'frequency'}
my_layout = Layout(title='Rolling a dice 1000 times', xaxis=x_title,yaxis=y_title)
offline.plot({'data': y_values, 'layout': my_layout}, filename='d6.html')

#Rolling two 6-sided dice
D6_1 = Die()
D6_2 = Die()

#Rolling it 1000 times
each_roll = []
for roll in range(5000):
    result_1= D6_1.roll()
    result_2= D6_2.roll()
    result_both = result_1+result_2
    each_roll.append(result_both)

#getting each side frequency
frequiences= []
for side in range(2,13):
    frequency = each_roll.count(side)
    frequiences.append(frequency)

#plotting
x_values= list(range(2,13))
y_values= [Bar(x=x_values,y= frequiences)]
x_title= {'title':'side'}
y_title= {'title':'frequency'}
layout_2= Layout(title='Rolling 2 D6 for 1000 times',xaxis=x_title,yaxis=y_title)

offline.plot({'data':y_values,'layout':layout_2},filename='d66.html')