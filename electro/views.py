from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import Booking_serializer,Contact_serializer,Review_serializer,subscribe_serializer,Register_serializer,Login_serializer
from .models import Booking, Review
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout


def userlogout(request):
    logout(request)
    return redirect('/')

class HomeView(APIView):
    serializer_class=Booking_serializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print('invalid')
        return Response(serializer.data)
    
class ContactView(APIView):
    serializer_class=Contact_serializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print('invalid')    
        return Response(serializer.data)
    
class ReviewView(APIView):
    serializer_class=Review_serializer
        
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

     

class SubscribeView(APIView):
    serializer_class=subscribe_serializer
        
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
# )))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
    
class  RegisterVIEW(APIView):
    
    serializer_class=Register_serializer
        
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
             user=serializer.validated_data['user']
             response_data={
                'user_id':user.id,
                'username':user.username,
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name

            }
             return Response(response_data)
            
        return Response(serializer.data)


class userLoginVIEW(APIView):
    
    serializer_class=Login_serializer
        
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.validated_data['user']
            token, created =Token.objects.get_or_create(user=user)

            response_data={
                'token':token.key,
                'user_id':user.id,
                'username':user.username,
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name

            }
            return Response(response_data)
        return Response(serializer.errors)
    
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    

class AppointmentVIEW(APIView):
    serializer_class=Booking_serializer
    query=Booking.objects.all()

    def get(self,request):
        data=self.query
        serializer=self.serializer_class(data,many=True)
        return Response(serializer.data)
    
class AllReviewView(APIView):
    serializer_class=Review_serializer
    query=Review.objects.all()

    def get(self,request):
        data=self.query
        serializer=self.serializer_class(data,many=True)
        return Response(serializer.data)
    
class View_AppointmentVIEW(APIView):
    serializer_class=Booking_serializer

    def get(self,request,id):
        data=Booking.objects.get(pk=id)
        serializer=self.serializer_class(data,many=False)
        return Response(serializer.data)
    
class Delete_AppointmentVIEW(APIView):
    serializer_class=Booking_serializer

    def delete(self,request,id):
        data=Booking.objects.get(pk=id)
        data.delete()
        serializer=self.serializer_class(data,many=False)
        return Response(serializer.data)