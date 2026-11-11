import openpyxl

class NewExcelReader:
    
    def read_excel_cell(self, row_no, col_no):
        book = openpyxl.load_workbook("C:\\Users\\user\\Downloads\\employeedata_latest.xlsx")
        sheet = book["emp_sheet1"]        
        return sheet.cell(row=row_no,column=col_no).value