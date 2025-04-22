from watchlist_app.models import Watchlist,StreamPlatform,Review
from . serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated
from watchlist_app.api.permissions import AdminorReadonly,ReviewUserOrReadOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle


class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()
    def perform_create(self, serializer):
       pk=self.kwargs['pk']
       watchlist=Watchlist.objects.get(pk=pk)
       review_user=self.request.user
       review_queryset=Review.objects.filter(watchlist=watchlist,review_user=review_user)
       if review_queryset.exists():
           raise ValidationError("have revied already")
       if watchlist.number_rating ==0:
           watchlist.avg_rating = serializer.validated_data['rating']
       else:
           watchlist.avg_rating=(watchlist.avg_rating+serializer.validated_data['rating'])/2
       watchlist.number_rating+=1
       watchlist.save()
       serializer.save(watchlist=watchlist,review_user=review_user)


class ReviewList(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer  
    # permission_classes=[ReviewUserOrReadOnly]
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)



class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[ReviewUserOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]

# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
#     def get(self,request,*args,**kwargs):
#         return self.retrive(request,*args,**kwargs)

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
             







class StreamPlatformListAV(APIView):
    permission_classes=[AdminorReadonly]
    def get(self,request):
        platform =  StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True,context={'request':request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer =  StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchListAV(APIView):
    permission_classes=[AdminorReadonly]
    def get(self,request):
        movie=Watchlist.objects.all()
        serializer=WatchListSerializer(movie,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchDetailAV(APIView):
    permission_classes=[AdminorReadonly]
    def get(self,request,pk):
        try:
            movie=Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error':' not fOUND'},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=Watchlist.objects.get(pk=pk)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        movie=Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer =  MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method=='POST':
#         serializer =  MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,pk):
#     if request.method=='GET':
#         try:
#          movie=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':"not found"},status=status.HTTP_404_NOT_FOUND)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method=='PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
#     if request.method=='DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

