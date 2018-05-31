import xlrd
import datetime

class FileUtils:
    @staticmethod
    def get_excel_workbook(filename):
        '''
        获取Excel工作表对象
        @param filename 文件名
        @return workbook
        '''
        return xlrd.open_workbook(filename=filename)

class DateTimeUtils:
    @staticmethod
    def str_to_dt(string):
        '''
        将str转换为datetime类型
        @param str ('%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S')
        @return datetime
        '''
        if 'T' in string:
            return datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%SZ')
        elif '-' in string:
            return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
        return datetime.datetime.strptime(string, '%Y%m%d %H:%M:%S')