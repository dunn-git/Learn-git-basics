import xlrd

Excelsheet = "Superstore.xls"

Book = xlrd.open_workbook(Excelsheet)

Sheet = Book.sheet_by_index(0)

print(Sheet.row_values(0))

Headings = Sheet.row_values(0)
Column1 = Headings[17]

print(Column1)

i =0
total =0

for row in range(Sheet.nrows):
    if str(Sheet.cell(row,7).value) == "Consumer":
        i = i +1
        total = total + (Sheet.cell(row,17).value)
    else:
        pass

print(i)
print(total)
print(total/i)
