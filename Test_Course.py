# Used for the Python Course as a main file
# Now I added even mor text
print("This Data Gather and Visualizer Project")

import xlrd

excel_workbook = xlrd.open_workbook("Raw_Data_Corona_Virus.xlsx")
excel_sheet = excel_workbook.sheet_by_name("Raw_Data")
#test_num = excel_sheet.cell(3, 2).value
#print ("The number of columns: " + str(excel_cols))
#print ("The number of rows: " + str(excel_rows))
#print ("The test number: " + str(test_num))



# PART I: Gather the data from file

excel_rows = excel_sheet.nrows
excel_cols = excel_sheet.ncols
excel_table = list()
record = list()

for x in range(excel_rows):
    for y in range(excel_cols):
        record.append(excel_sheet.cell(x,y).value)
    excel_table.append(record)
    record = []
    x +=1
print(excel_table)

# PART II: Sort the raw data and calculate


# PART III: Visualize the data

