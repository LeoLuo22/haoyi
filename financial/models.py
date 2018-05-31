from django.db import models

# Create your models here.
class HaoyiAccount(models.Model):
    # 账户表
    account_id = models.CharField(db_column='ACCOUNT_ID', max_length=50, primary_key=True)
    account_name = models.CharField(db_column='ACCOUNT_NAME', max_length=20)
    bank_name = models.CharField(db_column='BANK_NAME', max_length=50)
    crt_date = models.DateTimeField(db_column='CRT_DATE', auto_now=True)
    account_type = models.IntegerField(db_column='ACCOUNT_TYPE', help_text='0: Company 1: Person 2: Other')

    class Meta:
        managed = True
        db_table = 'HAOYI_ACCOUNT'

class HaoyiTransaction(models.Model):
    # 交易表
    accuont_id = models.CharField(db_column='ACCOUNT_ID', max_length=50)
    transaction_date = models.DateTimeField(db_column='TRANSACTION_DATE')
    '''
    income = models.FloatField(db_column='INCOME', default=0.0)
    expenditure = models.FloatField(db_column='EXPENDITURE', default=0.0)
    '''
    amount = models.FloatField(db_column='AMOUNT', blank=False, help_text='交易金额') 
    transaction_type = models.IntegerField(db_column='TRANSACTION_TYPE', blank=False, help_text='0: 支出 1: 收入 2: 借出 3:还款')
    balance = models.FloatField(db_column='BALANCE', help_text='余额')
    transaction_bank = models.CharField(db_column='TRANSACTION_BANK', max_length=50, help_text='交易行名')
    object_city = models.CharField(db_column='OBJECT_CITY', max_length=50, help_text='对方省市')
    object_account_id = models.CharField(db_column='OBJECT_ACCOUNT_ID', max_length=50, help_text='对方账号')
    object_account_name = models.CharField(db_column='OBJECT_ACCOUNT_NAME', max_length=50, help_text='对方户名')
    transaction_usage = models.CharField(db_column='TRANSACTION_UASGE', max_length=50, help_text='交易用途')
    remark = models.CharField(db_column='REMARK', max_length=50, help_text='备注')
    crt_date = models.DateTimeField(db_column='CRT_DATE', auto_now=True)

    class Meta:
        managed = True
        db_table = 'HAOYI_TRANSACTION'

class ObjectAccount(models.Model):
    # 交易账户表
    object_account_id = models.CharField(db_column='OBJECT_ACCOUNT_ID', max_length=50, primary_key=True)
    object_account_name = models.CharField(db_column='OBJECT_ACCOUNT_NAME', max_length=50)
    object_bank_name = models.CharField(db_column='OBJECT_BANK_NAME', max_length=50)
    crt_date = models.DateTimeField(db_column='CRT_DATE', auto_now=True)
    account_type = models.IntegerField(db_column='ACCOUNT_TYPE', help_text='0: Company 1: Person 2: Other')
    
    class Meta:
        managed = True
        db_table = 'OBJECT_ACCOUNT'
