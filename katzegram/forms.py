from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Post, Comment, Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email address','style':'width:250px'}))
    first_name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'First name',
        'style':'width:250px'}))
    last_name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name','style':'width:250px'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


    def __init__(self, *args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['username'].widget.attrs['style'] = 'width:250px'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].widget.attrs['style'] = 'width:250px'

        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].widget.attrs['style'] = 'width:250px'

        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class ="form-text text-muted"><small>Enter the same password as before, for verification. </small><span>'

class PostForm(forms.ModelForm):
    content = forms.ImageField(label='Select your post')

    class Meta:
        model = Post
        exclude = ('user','likes',)



class CommentForm(forms.ModelForm):
    text = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': 'Add a comment',
                'style':'border:none; outline:none; height:30px;'
                
            }
            ),
            label = '',
        )

    class Meta:
        model = Comment
        fields = ('text',)

class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Picture')
    profile_bio = forms.CharField(label='description',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'description','style':'height:80px'}))


    class Meta:
        model = Profile
        fields = ('profile_image','profile_bio',)
