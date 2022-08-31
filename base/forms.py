from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        # CREATE AN INPUT FOR ALL FIELDS
        # (except updated and created)
        fields = '__all__'
        
