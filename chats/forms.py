from django import forms
from .models import ChatRoom

class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name']
        
class AddParticipantForm(forms.Form):
    username = forms.CharField(max_length=150)
