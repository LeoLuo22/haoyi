from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
'''
    path('comments', views.comments, name='comments'),
    path('scores', views.scores, name='scores'),
    path('relatedComments', views.related_comments, name='related_comments'),
    url(r'^boc/$', views.comment_list),
    #url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    #url(r'^comments/', views.CommentList.as_view())

    # API v1
    url(r'v1/(?P<app>\w+)/(?P<store>\w+)/comments/$', views.CommentListV1.as_view(), name='CommentListV1'),
    url(r'v1/opinions/$', views.MixinsOpinionList.as_view(), name='opinions'),
    url(r'^v1/opinions/(?P<ID>[0-9]+)/$', views.OpinionDetail.as_view()), 
    url(r'v1/opinions/categories/$', views.OpinionCategoryList.as_view()),
    url(r'v1/opinions/upload/$', views.upload), 
    url(r'v1/comments/import/(?P<store>\w+)/', views.comment_import)
'''
urlpatterns = [
    url(r'v1/transactions/import/', views.transaction_import), 
    url(r'v1/transactions/$', views.HaoyiTransactionList.as_view()),
    url(r'v1/balance/(?P<ID>\w+)/$', views.BalanceDetail.as_view()),
    # Need startDate, endDate
    url(r'v1/transactions/(?P<account_id>\w+)/$', views.TransactionQueryset.as_view()), 
    url(r'v1/transactions/analysis$', views.Analysis.as_view()), 
    # url(r'test/$', views.Analysis.as_view()),
    url(r'v1/accounts/(?P<account_id>\S+)/(?P<start_date>\d+)/(?P<end_date>\d+)/$', views.AccountsDetail.as_view()),
]