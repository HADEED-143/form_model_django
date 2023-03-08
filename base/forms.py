from django import forms

from . models import PostCv

class Postform(forms.ModelForm):
    class Meta:
        model = PostCv
        fields = "__all__"