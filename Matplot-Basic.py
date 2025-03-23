#----------------Exercise 1----------------

# import matplotlib.pyplot as plt

# X = range(1, 50)
# Y = [value * 3 for value in X]

# print("Values of X:")
# print(*range(1,50)) 
# print("Values of Y (thrice of X):")
# print(Y)

# plt.plot(X, Y)
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Draw a line.')
# plt.show()

#----------------Exercise 2----------------

# import matplotlib.pyplot as plt

# x = [1,2,3]
# y = [2,4,1]

# plt.plot(x, y)
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Sample graph!')
# plt.show()

#----------------Exercise 3----------------

# import matplotlib.pyplot as plt

# with open("test.txt") as f:
#     data = f.read()
# data = data.split('\n')
# x = [row.split(' ')[0] for row in data]
# y = [row.split(' ')[1] for row in data]
# plt.plot(x, y)

# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Sample graph!')
# plt.show()


#----------------Exercise 4----------------

# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
# df.plot()
# plt.show()

#----------------Exercise 5----------------

# import matplotlib.pyplot as plt

# x1 = [10,20,30]
# y1 = [20,40,10]
# plt.plot(x1, y1, label = "line 1")

# x2 = [10,20,30]
# y2 = [40,10,30]
# plt.plot(x2, y2, label = "line 2")

# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Two or more lines on same plot with suitable legends ')
# plt.legend()
# plt.show()

#----------------Exercise 6----------------

# import matplotlib.pyplot as plt

# x1 = [10,20,30]
# y1 = [20,40,10]

# x2 = [10,20,30]
# y2 = [40,10,30]

# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Two or more lines with different widths and colors with suitable legends ')

# plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-width-3')
# plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-width-5')

# plt.legend()
# plt.show()

#----------------Exercise 7----------------

# import matplotlib.pyplot as plt

# x1 = [10,20,30]
# y1 = [20,40,10]

# x2 = [10,20,30]
# y2 = [40,10,30]

# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Two or more lines with different widths and colors with suitable legends ')

# plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-dotted',linestyle='dotted')
# plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-dashed', linestyle='dashed')

# plt.legend()
# plt.show()

#----------------Exercise 8----------------

# import matplotlib.pyplot as plt

# x = [1,4,5,6,7]
# y = [2,6,3,6,3]

# plt.title('Display marker')
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.plot(x, y, color='red', linestyle='dashdot', linewidth = 3,
#          marker='o', markerfacecolor='blue', markersize=12)
# plt.ylim(1,8)
# plt.xlim(1,8)

# plt.show()


#----------------Exercise 9----------------

# import matplotlib.pyplot as plt

# X = range(1, 50)
# Y = [value * 3 for value in X]
# plt.plot(X, Y)
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Draw a line.')
# print(plt.axis()) 

# plt.axis([0, 100, 0, 200]) 

# plt.show()

#----------------Exercise 10----------------

# import pylab as pl

# x1 = [2, 3, 5, 6, 8]
# y1 = [1, 5, 10, 18, 20]

# x2 = [3, 4, 6, 7, 9]
# y2 = [2, 6, 11, 20, 22]

# pl.axis([0, 10, 0, 30]) 
# pl.plot(x1, y1,'b*', x2, y2, 'ro')
# pl.show()

#----------------Exercise 11----------------

# import matplotlib.pyplot as plt
# import numpy as np

# t = np.arange(0., 5., 0.2)
# print(t)

# plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
# plt.show()

#----------------Exercise 12----------------

# import datetime as DT
# from matplotlib import pyplot as plt
# from matplotlib.dates import date2num

# data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
#         (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
#         (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
#         (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
#         (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]
# x = [date2num(date) for (date, value) in data]
# y = [value for (date, value) in data]

# fig = plt.figure()
# graph = fig.add_subplot(111)

# graph.plot(x,y,'r-o')
# graph.set_xticks(x)

# graph.set_xticklabels(
#         [date.strftime("%Y-%m-%d") for (date, value) in data]
#         )
# plt.show()

#----------------Exercise 13----------------

# import datetime as DT
# from matplotlib import pyplot as plt
# from matplotlib.dates import date2num

# data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
#         (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
#         (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
#         (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
#         (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]
# x = [date2num(date) for (date, value) in data]
# y = [value for (date, value) in data]

# fig = plt.figure()
# graph = fig.add_subplot(111)

# graph.plot(x,y,'r-o')
# graph.set_xticks(x)

# graph.set_xticklabels(
#         [date.strftime("%Y-%m-%d") for (date, value) in data]
#         )

# plt.xlabel('Date')
# plt.ylabel('Closing Value')
# plt.title('Closing stock value of Alphabet Inc.') 
# plt.grid(linestyle='-', linewidth='0.5', color='blue')

# plt.show()

#----------------Exercise 14----------------

# import datetime as DT
# from matplotlib import pyplot as plt
# from matplotlib.dates import date2num

# data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
#         (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
#         (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
#         (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
#         (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]
# x = [date2num(date) for (date, value) in data]
# y = [value for (date, value) in data]

# fig = plt.figure()
# graph = fig.add_subplot(111)

# graph.plot(x,y,'r-o')
# graph.set_xticks(x)

# graph.set_xticklabels(
#         [date.strftime("%Y-%m-%d") for (date, value) in data]
#         )

# plt.xlabel('Date')
# plt.ylabel('Closing Value')
# plt.title('Closing stock value of Alphabet Inc.') 

# plt.minorticks_on()
# plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
# plt.tick_params(which='both', 
#                 top='off', 
#                 left='off', 
#                 right='off', 
#                 bottom='off')

# plt.show()

#----------------Exercise 15----------------

import matplotlib.pyplot as plt

fig = plt.figure()
fig.subplots_adjust(bottom=0.020, left=0.020, top = 0.900, right=0.800)

plt.subplot(2, 1, 1)
plt.xticks(()), plt.yticks(())

plt.subplot(2, 3, 4)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 5)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 6)
plt.xticks(())
plt.yticks(())

plt.show()