from rest_framework import serializers
from .models import Booking,Contact,Review,Subscriber
from django.contrib.auth.models import User
from .forms import Customizedsercreationform

class Booking_serializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['id','name','email','phone','address','city','state','pin_code','description','date','author']
        extra_kwargs={'author':{'read_only':True}}
    



class Contact_serializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['name','email','phone','subject','message']



class Review_serializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['message','author']
        extra_kwargs={'author':{'read_only':True}}

class subscribe_serializer(serializers.ModelSerializer):
    class Meta:
        model=Subscriber
        fields=['email']



class Register_serializer(serializers.Serializer):
    username=serializers.CharField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    email=serializers.EmailField()
    password1=serializers.CharField(style={'input_type':'passeord'})
    password2=serializers.CharField(style={'input_type':'passeord'})

    def validate(self,data):
        form=Customizedsercreationform(data)
        if form.is_valid():
            user=form.save()
            data['user']=user
        else:
            raise serializers.ValidationError(form.errors)   
        return data 


    



class Login_serializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self,data):
        username=data.get('username')
        password=data.get('password')

        if username and password:
            user=User.objects.filter(username=username).first()

            if user and user.check_password(password):
                data['user']=user
            else:
                raise serializers.ValidationError('invalid username or password')    
        else:
           raise serializers.ValidationError('both username and password incoorect')
        return data     

    