from django.views.generic.base import View
from apps.memberapp.models import Goods

import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse

class GoodsListViews(View):
    def get(self,request):
        goods=Goods.objects.all()
        json_data=serializers.serialize('json',goods)
        json_data=json.loads(json_data)
        return JsonResponse(json_data,safe=False)

