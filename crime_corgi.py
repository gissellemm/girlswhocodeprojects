import matplotlib.pyplot as plt
import state_crime
import numpy as np
list_of_report = state_crime.get_all_crimes()

#TOTAL NUMBER OF RAPES IN THE UNITED STATES FROM 1960-2012
years = []
number = []

for i in range(len(list_of_report)):
    c = list_of_report
    if c[i]['State'] == "United States":
        # print(c[i]['State'], c[i]['Year'], c[i]['Data']['Totals']['Violent']['Rape'])
        year = c[i]['Year']
        years.append(year)
        total = c[i]['Data']['Totals']['Violent']['Rape']
        number.append(total)

#SCATTERPLOT
plt.plot(years, number, 'ro')
plt.xlabel('Year')
plt.ylabel('Total Number of Rapes')
plt.title('Number of Rapes in the United States from 1960-2012')
plt.axis([1960, 2012, 17000, 110000])
plt.show()

#BAR GRAPH
index = np.arange(len(years))
plt.bar(index, number)
plt.xlabel('Year')
plt.ylabel('Number of Rapes')
plt.xticks(index, year, fontsize=5, rotation=30)
plt.title('Market Share for Each Genre 1995-2017')
plt.show()
