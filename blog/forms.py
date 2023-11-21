from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = CollaborateRequest
        fields = ('name', 'email', 'message')