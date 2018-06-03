from django.test import TestCase
import requests, re

# Create your tests here.
# from .bank import ABCforEnterprise

# ABCforEnterprise.import_transaction('E:/TrnxReport.xls')
'''
a = "text:'20180524113723319481'"
print(re.findall(r'\d+', a))
'''
url = 'http://127.0.0.1:8000/financial/v1/transactions/analysis?startDate=20180524&endDate=20180610'
data = dict(accountId='26-157001040005554', objectAccountName='西京学院')
print(requests.post(url, data=data).text)
