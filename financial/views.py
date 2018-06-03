import logging

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .bank import ABCforEnterprise
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import HaoyiTransaction
from .serializers import *
from .util import DateTimeUtils

log = logging.getLogger('django')

# Create your views here.
def transaction_import(request):
    ABCforEnterprise.import_transaction_v1('E:/TrnxReport.xls', '26-157001040005554')
    return HttpResponse('ok')

class HaoyiTransactionList(mixins.ListModelMixin, 
                           mixins.CreateModelMixin, 
                           generics.GenericAPIView):
    model = HaoyiTransaction
    serializer_class = HaoyiTransactionSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        queryset = HaoyiTransaction.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BalanceDetail(APIView):
    # 获取账户余额信息
    permission_classes = (AllowAny, )
    def get_queryset(self):
        return HaoyiTransaction.objects.all()

    def get_object(self, ID):
        try:
            return HaoyiTransaction.objects.filter(account_id=ID).order_by('-transaction_date')[0]
        except Exception:
            return

    def get(self, request, ID, format=None):
        # :param ID account_id
        balance = self.get_object(ID)
        if not balance:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        serializer = HaoyiTransactionSerializer(balance)
        return Response(serializer.data)

class TransactionQueryset(generics.ListAPIView):
    serializer_class = HaoyiAccountSerializer

    def get_queryset(self):
        log.info(self.kwargs)
        log.info(self.request.query_params)
        account_id = self.kwargs
        
        pass
        

class Analysis(APIView):
    
    def get(self, request, *args, **kwargs):
        log.info(self.kwargs)
        log.info(self.request.query_params)
        data = {'name': 'jj', 'id': 1}
        return Response(data)

    def post(self, request, *args, **kwargs):
        log.info(self.kwargs)
        log.info(self.request.query_params)
        account_id = self.request.data.get('accountId')
        start = self.request.query_params.get('startDate')
        end = self.request.query_params.get('endDate')
        object_account_id = self.request.data.get('objectAccountId')
        object_account_name = self.request.data.get('objectAccountName')

        start_date = DateTimeUtils.str_to_dt(start)
        end_date = DateTimeUtils.str_to_dt(end)

        if object_account_id:
            transactions = HaoyiTransaction.objects.filter(account_id=account_id, 
                                                           transaction_date__range=(start_date, end_date),
                                                           object_account_id = object_account_id)
        elif object_account_name:
            transactions = HaoyiTransaction.objects.filter(account_id=account_id, 
                                                           transaction_date__range=(start_date, end_date),
                                                           object_account_name = object_account_name)
        elif object_account_id and object_account_name:
            transactions = HaoyiTransaction.objects.filter(account_id=account_id, 
                                                           transaction_date__range=(start_date, end_date),
                                                           object_account_id = object_account_id,
                                                           object_account_name = object_account_name)
        incomes = []
        expenditures = []
        for transaction in transactions:
            transaction_type = transaction.transaction_type
            amount = transaction.amount
            if transaction_type == 0:
                expenditures.append(amount)
            else:
                incomes.append(amount)

        income = sum(incomes)
        expenditure = sum(expenditures)
        data = dict(income=income, expenditure=expenditure, total=income-expenditure)
        return Response(data)
        

