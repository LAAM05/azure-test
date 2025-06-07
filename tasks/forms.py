from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="El número debe tener el formato: '+999999999'. Hasta 15 dígitos."
)

class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['username'].widget.attrs.update({
           'class':"form-control",
           'id':"reg-name",
           'name':"name",
           'required':'',
           #'type':"text",
        
      })
      self.fields['email'].widget.attrs.update({
          'type':"email",
          'id':"reg-email",
          'name':"email",
          'class':"form-control", 
          'required':""
      })
      
      self.fields['phone_number'].widget.attrs.update({
          'type':"tel",
          'id':"reg-phone",
          'name':"phone",
          'class':"form-control",
          'required':""
      })
      
      self.fields['password1'].widget.attrs.update({
          'type':"password",
          'id':"reg-password",
          'name':"password",
          'class':"form-control",
          'required':""
      })
      
      self.fields['password2'].widget.attrs.update({
          'type':"password",
          'id':"reg-password",
          'name':"password",
          'class':"form-control",
          'required':""
      })
   
    username = forms.CharField(max_length=50, required=True, help_text='Put your name here')
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True,max_length=20,validators=[phone_regex]
)
    #password1 = forms.CharField(required=True,min_length=8)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is taken, chose another.")
        return email
    
    class Meta:
        model = User
        fields = ('username','email','phone_number','password1','password2')
        

class LoginUserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'id': 'login-email', 'required': ''
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'id': 'login-password', 'required': ''
    }))