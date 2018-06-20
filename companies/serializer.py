from rest_framework import serializers
from companies.models import stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = stock
        # fields = ('ticker','volume')
        fields = '__all__'