from rest_framework.decorators import api_view
from .serializers import RegisterationSerializer
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.authtoken.models import Token
from user_app import models
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST',])
def logout_view(request):
     if request.method=='POST':
          request.user.auth_token.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
def registration_view(request):
    serializer = RegisterationSerializer(data=request.data) 
    data={}
    if serializer.is_valid():
        account=serializer.save()
        data['Response']='registartion sucessful' 
        data['username']=account.username
        data['email']=account.email
        # token=Token.objects.get(user=account).key
        # data['token']=token
        refresh =  RefreshToken.for_user(account)
        data=['token'] = {
             'refersh':str(refresh),
             'access': str(refresh.access_token),
        }


    else:
           return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)  


    return Response(data) 
    
 
