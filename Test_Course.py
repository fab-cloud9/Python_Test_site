# Used for the Python Course as a main file
# Now I added even mor text
import matplotlib

print("This Data Gather and Visualizer Project")

import xlrd
esp_pop = int(46940000/100000)
ind_pop = int(1353000000/100000)
nor_pop = int(5433000/100000)
swe_pop = int(10230000/100000)
usa_pop = int(328200000/100000)

excel_workbook = xlrd.open_workbook("Raw_Data_Corona_Virus.xlsx")
excel_sheet = excel_workbook.sheet_by_name("Raw_Data")
# test_num = excel_sheet.cell(3, 2).value
# print ("The number of columns: " + str(excel_cols))
# print ("The number of rows: " + str(excel_rows))
# print ("The test number: " + str(test_num))


# PART I: Gather the data from file
# Focus on the correct parameters

excel_rows = excel_sheet.nrows
excel_cols = excel_sheet.ncols
excel_table = list()
record = list()

for x in range(excel_rows):
    for y in range(excel_cols):
        record.append(excel_sheet.cell(x, y).value)
    excel_table.append(record)
    record = []
    x += 1
# print(excel_table)

# PART II: Sort the raw data and calculate
esp_tot = []
esp_100k = []
ind_tot = []
ind_100k = []
nor_tot = []
nor_100k = []
swe_tot = []
swe_100k = []
usa_tot = []
usa_100k = []

# To extract each countries total data into one list for each country
for i in range(excel_rows):
    if excel_table[i][1] == "Spain":
        esp_tot.append(excel_table[i][:])
        print(esp_tot)
        #Removing listsof list
        esp_tot = [item for sublist in esp_tot for item in sublist]
        #for item in range(esp_tot):
        #    esp_100k.append(esp_tot[2:])
        print(esp_100k)
        esp_100k = [k * 2 for k in esp_100k]
        print(esp_100k)
    elif excel_table[i][1] == "India":
        ind_tot.append(excel_table[i])
    elif excel_table[i][1] == "Norway":
        nor_tot.append(excel_table[i])
    elif excel_table[i][1] == "Sweden":
        swe_tot.append(excel_table[i])
    elif excel_table[i][1] == "USA":
        usa_tot.append(excel_table[i])
    i += 1
# The per 100k capita data
#print(esp_100k)
# The sorted trending data
esp_trend = []
ind_trend = []
nor_trend = []
swe_trend = []
usa_trend = []

for j in range(excel_rows):  # To extract each countries live data into one list for each country
    if excel_table[j][1] == "Spain_live":
        esp_trend.append(excel_table[j])
    elif excel_table[j][1] == "India_live":
        ind_trend.append(excel_table[j])
    elif excel_table[j][1] == "Norway_live":
        nor_trend.append(excel_table[j])
    elif excel_table[j][1] == "Sweden_live":
        swe_trend.append(excel_table[j])
    elif excel_table[j][1] == "USA_live":
        usa_trend.append(excel_table[j])
    j += 1

esp_trend_inf = [esp_trend[0][2], esp_trend[1][2]]
esp_inf_der = int(esp_trend_inf[1] - esp_trend_inf[0])
ind_trend_inf = [ind_trend[0][2], ind_trend[1][2]]
ind_inf_der = int(ind_trend_inf[1] - ind_trend_inf[0])
nor_trend_inf = [nor_trend[0][2], nor_trend[1][2]]
nor_inf_der = int(nor_trend_inf[1] - nor_trend_inf[0])
swe_trend_inf = [swe_trend[0][2], swe_trend[1][2]]
swe_inf_der = int(swe_trend_inf[1] - swe_trend_inf[0])
usa_trend_inf = [usa_trend[0][2], usa_trend[1][2]]
usa_inf_der = int(usa_trend_inf[1] - usa_trend_inf[0])

#--------- PART III: Visualize the data

import matplotlib.pyplot as plot
# Trending values
time = ["August 24th", "August 25th"]
plot.plot(time, esp_trend_inf)
plot.plot(time, ind_trend_inf)
plot.plot(time, nor_trend_inf)
plot.plot(time, swe_trend_inf)
plot.plot(time, usa_trend_inf)
plot.xlabel('Date')
plot.ylabel('# of cases')
plot.title('Trending number of Infected cases')
plot.legend(['Spain: ' + str(esp_inf_der), 'India: ' + str(ind_inf_der), 'Norway: ' + str(nor_inf_der), 'Sweden: ' +
             str(swe_inf_der), 'USA: ' + str(usa_inf_der)], loc='right')
plot.show()

# Total Numbers
# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]
# heights of bars = number of total cases
height = [esp_tot[2], ind_tot[0][2], nor_tot[0][2], swe_tot[0][2], usa_tot[0][2]]
# labels for bars
tick_label = ['Spain', 'India', 'Norway', 'Sweden', 'USA']
# plotting a bar chart
plot.bar(left, height, tick_label=tick_label,
         width=0.8, color=['yellow', 'green', 'red', 'blue', 'black'])
# naming the x-axis
plot.xlabel('Countries')
# naming the y-axis
plot.ylabel('# of Cases')
# plot title
plot.title('Total number of cases')
plot.axis([0, 6, 0, 100000000])
plot.show()
