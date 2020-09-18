from django import forms
    
class UploadFileForm(forms.Form):

    image = forms.FileField( widget=forms.FileInput(),required=False)   
