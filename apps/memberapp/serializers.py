from .models import *
from rest_framework import serializers
#继承serializers中的Serializer
#可以通过post方式保存数据到数据库中
class GoodsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=GoodsType
        #指定所有model字段，并映射到数据库
        fields='__all__'
class GoodsSerializer(serializers.ModelSerializer):
    #变量名type必须是关联外键的字段名
    type=GoodsTypeSerializer()
	#类似于django中的model设计
    class Meta:
        model = Goods
        # 指定所有model字段，并映射到数据库
        fields = '__all__'