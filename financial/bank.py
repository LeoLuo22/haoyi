# 银行操作
import logging
import re
from .models import HaoyiTransaction
from .util import FileUtils
from .util import DateTimeUtils

log = logging.getLogger('django')

class ABC:
    pass

class ABCforEnterprise(ABC):
    # 农行企业网银简易版
    @staticmethod
    def import_transaction(filename, account_id):
        '''
        导入交易Excel到数据库
        @param filename 文件名
        :param account_id 账户
        '''
        workbook = FileUtils.get_excel_workbook(filename)
        sheet = workbook.sheet_by_index(0)
        print(sheet.nrows)
        for row in range(2, sheet.nrows-2):
            transaction = HaoyiTransaction()
            transaction_date = DateTimeUtils.str_to_dt(sheet.cell(row, 0).value)
            balance = float(sheet.cell(row, 3).value)
            # 记录是否已存在
            if HaoyiTransaction.objects.get(transaction_date=transaction_date, balance=balance):
                log.info('Transaction already exist. ' + str(transaction_date))
                continue
            transaction.account_id = account_id
            transaction.transaction_date = DateTimeUtils.str_to_dt(sheet.cell(row, 0).value)
            income = float(sheet.cell(row, 1).value)
            if income == 0.00:
                transaction.transaction_type = 0
                transaction.amount = float(sheet.cell(row, 2).value)
            else:
                transaction.transaction_type = 1
                transaction.amount = income
            transaction.balance = balance
            transaction.transaction_bank = sheet.cell(row, 4).value
            transaction.object_city = sheet.cell(row, 5).value
            transaction.object_account_id = sheet.cell(row, 6).value
            transaction.object_account_name = sheet.cell(row, 7).value
            transaction.transaction_usage = sheet.cell(row, 8).value
            transaction.save()

    # 农行企业网银详细版
    @staticmethod
    def import_transaction_v1(filename, account_id):
        '''
        导入交易Excel到数据库
        @param filename 文件名
        :param account_id 账户
        '''
        workbook = FileUtils.get_excel_workbook(filename)
        sheet = workbook.sheet_by_index(0)
        log.info(sheet.nrows)
        for row in range(2, sheet.nrows-2):
            transaction = HaoyiTransaction()
            transaction_date = DateTimeUtils.str_to_dt(sheet.cell(row, 0).value)
            balance = float(sheet.cell(row, 4).value)
            # 记录是否已存在
            try:
                HaoyiTransaction.objects.get(transaction_date=transaction_date, balance=balance)
                log.info('Transaction already exist. ' + str(transaction_date))
                continue
            except Exception:
                pass
            transaction.account_id = account_id
            transaction.transaction_date = DateTimeUtils.str_to_dt(sheet.cell(row, 0).value)
            timestamp = str(sheet.cell(row, 1))
            log.info(timestamp)
            transaction.transaction_timestamp = str(re.findall(r'\d+', timestamp)[0])
            income = float(sheet.cell(row, 2).value)
            if income == 0.00:
                transaction.transaction_type = 0
                transaction.amount = float(sheet.cell(row, 3).value)
            else:
                transaction.transaction_type = 1
                transaction.amount = income
            transaction.balance = balance
            transaction.procedure_fee = float(sheet.cell(row, 5).value)
            transaction.transaction_way = sheet.cell(row, 6).value
            transaction.transaction_bank = sheet.cell(row, 7).value
            transaction.transaction_categoty = sheet.cell(row, 8).value
            transaction.object_city = sheet.cell(row, 9).value
            transaction.object_account_id = sheet.cell(row, 10).value
            transaction.object_account_name = sheet.cell(row, 11).value
            transaction.transaction_explain = sheet.cell(row, 12).value
            transaction.transaction_summary = sheet.cell(row, 13).value
            transaction.transaction_usage = sheet.cell(row, 14).value
            transaction.save()