# context.driver = webdriver.Chrome(executable_path = r"C://Webdriver//chromedriver-win64 (1)//chromedriver-win64//chromedriver.exe" )
# context.driver.get( "http://5.180.27.81:8081/bems/login.do" )
path = r"C:\Users\Shalini\Documents\timesheet.xlsx"
import openpyxl

def getRowCount(file, sheetName) :
    workbook = openpyxl. load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheetName)
    return (sheet.max_row)
def getColumnCount(file, sheetName) :
    workbook = openpyxl.load_workbook(file)
    sheet = workbook.get_sheet_by_name(sheetName)
    return (sheet.max_column)
def readData(file, sheetName,rownum,columnno) :
    workbook = openpyxl.load_workbook (file)
    sheet = workbook.get_sheet_by_name (sheetName)
    return sheet. cell (row=rownum, column=columnno) . value
def writeData (file, sheetName,r,c,data) :
    workbook = openpyxl.load_workbook (file)
    sheet = workbook.get_sheet_by_name (sheetName)
    sheet.cell(row=r,column=c).value=data
    workbook.save(file)