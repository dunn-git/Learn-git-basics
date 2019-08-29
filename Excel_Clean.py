import pandas as pd

Excel_File = 'pan.xls'
Sheet = pd.read_excel(Excel_File, sheet_name = 'Orders')
#print(Sheet.head(10))

Customer_Both_Names = Sheet["Customer Name"]
#print(Customer_Both_Names)

names = Customer_Both_Names.str.split(" ", n = 1, expand = True)
Sheet["First Name"] = names[0]
Sheet["Last Name"] = names[1]
#del Sheet['Customer Name']
Sheet.drop('Customer Name',axis=1)
print(Sheet)

#Sheet.to_excel('output.xlsx')







