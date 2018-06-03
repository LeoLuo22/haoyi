from django.test import TestCase

# Create your tests here.
from .bank import ABCforEnterprise

ABCforEnterprise.import_transaction('E:/TrnxReport.xls')