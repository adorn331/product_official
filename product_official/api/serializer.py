from .models import APP, Product
from rest_framework.serializers import ModelSerializer


# class PlatFormSerializer(ModelSerializer):
#     class Meta:
#         model = PlatForm
#         fields = '__all__'


class APPSerializer(ModelSerializer):
    # platform_type = PlatFormSerializer(many=True, read_only=True)

    class Meta:
        model = APP
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
