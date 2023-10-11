# forms.py
from django import forms
from .models import Hotel


class HotelForm(forms.ModelForm):

	class Meta:
		model = Hotel
		fields = ['name', 'face_Main_Img','cartoon_Main_Img']
		
