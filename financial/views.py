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

log = logging.getLogger('django')

# Create your views here.
def transaction_import(request):
    ABCforEnterprise.import_transaction('E:/TrnxReport.xls')
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
