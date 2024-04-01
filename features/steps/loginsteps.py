# from behave import *
# from selenium import webdriver
# from venv import XLUtils
# import time
#
#
# @Given("Open the chrome browser and start the application")
# def launchBrowser(context):
#     context.driver=webdriver.Chrome(executable_path =r"C://Webdriver//chromedriver-win64 (1)//chromedriver-win64//chromedriver.exe")
#     context.driver.get("http://5.180.27.81:8081/bems/login.do")
# @When("User enters username and password")
# def loginpage(context):
#     path = r"C:\Users\Shalini\Documents\timesheet.xlsx"
#     rows = XLUtils.getRowCount(path, 'Sheet1')
#     for r in range(2,rows+1):
#
#         username = XLUtils.readData(path,"Sheet1", r, 1)
#         password = XLUtils.readData(path,"Sheet1", r, 2)
#         context.driver.find_element_by_name("username").send_keys(username)
#         time.sleep(9)
#         context.driver.find_element_by_id("password").send_keys(password)
#         time.sleep(20)
# @Then("Click on Submit button")
# def Sumbit(context):
#     context.driver.find_element_by_id("loginBtnId").click()
#     time.sleep(10)
#     context.driver.find_element_by_xpath("//a[@title='Logout']").click()
    # if driver.title == "Total Hours Logged":
    #         print( "test is passed" )
    #         time.sleep(31)
    #         XLUtils.writeData(path,"Sheet2",r,3,"test passed" )
    #  else:
    #     print("test failed")
    #     time.sleep(31)
    #     XLUtils.writeData(path, "Sheet3", r, 3, "test failed" )
# #         context.driver.find_element_by_xpath("//a[@title='Logout']" ).click()
# # context.driver.find_element_by_name( "username" ).clear()
# # context.driver.find_element_by_id( "password" ).clear()
# # loginpage()
# # clicksumbit()
from behave import *
from selenium import webdriver
from venv import XLUtils
import time



@Given("Open the chrome browser and start the application")
def launchBrowser(context):


    context.driver=webdriver.Chrome(executable_path =r"C://Webdriver//chromedriver-win64 (1)//chromedriver-win64//chromedriver.exe")
    context.driver.get("http://5.180.27.81:8081/bems/login.do")

@When("User enters username and password")
def loginpage(context):
    path = r"C:\Users\Shalini\Documents\timesheet.xlsx"
    rows = XLUtils.getRowCount(path, 'Sheet1')
    Username = context.driver.find_element_by_name("username")
    Password = context.driver.find_element_by_id("password")

    for r in range(2,rows+1):


       username = XLUtils.readData(path,"Sheet1", r, 1)
       password = XLUtils.readData(path,"Sheet1", r, 2)

       time.sleep(3)
       Username.send_keys(username)
       time.sleep(3)

       Password.send_keys(password)
       context.driver.find_element_by_id("loginBtnId").click()
       time.sleep( 1 )
       try:
        Username.clear()
       except:
           print('error for',Username)
           pass
       try:
           Password.clear()
       except:
           print('error for ',password)
           pass
       time.sleep( 1 )

@Then("Click on Submit button")
def Sumbit(context):


    # context.driver.find_element_by_id("loginBtnId").click()
    #
    # time.sleep(10)

    context.driver.find_element_by_xpath("//a[@title='Logout']").click()
    time.sleep(20)
    # TimeSheet=context.driver.find_element_by_xpath("//div[@class='col-md-6']")
    # if driver.title == "Time Sheet":
    #         print( "test is passed" )
    #         time.sleep(10)
    #         XLUtils.writeData(path,"Sheet1",r,3,"test passed" )
    # else:
    #     print("test failed")
    #     time.sleep(31)
    #     XLUtils.writeData(path, "Sheet1", r, 3, "test failed" )
    # context.driver.find_element_by_xpath( "//a[@title='Logout']" ).click()
    # time.sleep(20)
