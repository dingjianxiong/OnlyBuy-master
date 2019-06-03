from django.shortcuts import render
from apps.memberapp.models import *
# Create your views here.
def index_views(request):

    return render(request,'index.html')


#
# def footer_views(request):
#     return render(request,'footer.html')
# def header_views(request):
#     return render(request,'header.html')
#
# def product_details(request):
#     typeid=request.GET.get('typeid')
#     goodid = request.GET.get('goodid')
#     print('tyid:%s,goodid:%s'%(typeid,goodid))
#     prarms={
#         'typeid':typeid,
#         'goodid':goodid,
#     }
#     return render(request,'product_details.html',prarms)
