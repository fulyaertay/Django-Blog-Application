from django import forms
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username=forms.CharField(max_length=150, label="Kullanıcı Adı:")
    password=forms.CharField(max_length=150,widget=forms.PasswordInput,label="Şifre:")

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adı veya parola yanlış")
        return super(LoginForm,self).clean()


class RegisterForm(forms.ModelForm):
    username=forms.CharField(max_length=150, label="Kullanıcı Adı:")
    password1=forms.CharField(max_length=150,widget=forms.PasswordInput,label="Şifre:")
    password2=forms.CharField(max_length=150,widget=forms.PasswordInput,label="Tekrar Şifre:")

    class Meta:
        model=User
        fields=["username","password1","password2"]

    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Parolalar Eşleşmiyor!")
        return password2