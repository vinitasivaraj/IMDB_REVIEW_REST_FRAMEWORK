from rest_framework import serializers
from watchlist_app.models import Watchlist,StreamPlatform,Review

class ReviewSerializer(serializers.ModelSerializer):
    review_serializer=serializers.StringRelatedField()
    class Meta:
        model=Review
        # exclude=('watchlist',)
        fields="__all__"





class WatchListSerializer(serializers.ModelSerializer):
    # len_name=serializers.SerializerMethodField()
    reviews=ReviewSerializer(many=True,read_only=True)


    class Meta:
        model=Watchlist
        # fields = ['id', 'name','description']
        fields = "__all__"
        # exclude = ['name']

    # def get_len_name(self,objects):
    #     length =  len(objects.name)
    #     return length
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("name is too short")
    #     else:
    #         return value
        
    # def validate(self, attrs):
    #     if attrs['name']== attrs['description']:
    #         raise serializers.ValidationError("title and description should not be same")
    #     else:
    #         return attrs
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchListSerializer(many=True,read_only=True)
    class Meta:
        model=StreamPlatform
        fields="__all__"







# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description =serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     def validate_name(self,value):
#         if len(value) < 2:
#             raise serializers.ValidationError("name is too short")
#         else:
#             return value
        
#     def validate(self, attrs):
#         if attrs['name']== attrs['description']:
#             raise serializers.ValidationError("title and description should not be same")
#         else:
#             return attrs