from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from django import forms
from .models import *

class PixelForm(ModelForm):
    class Meta:
        model = Pixel 
        fields = [
            'pixelType',
            'inputUniverse',
            'inputAddress',
            'outputUniverse',
            'outputAddress',
            'fixtureNum',
            'pixelNum'
        ]
        labels = {
            'pixelType': 'Pixel Type',
            'inputUniverse': 'Input Universe',
            'inputAddress': 'Input Address',
            'outputUniverse': 'Output Universe',
            'outputAddress': 'Output Address',
            'fixtureNum': 'Fixture Number',
            'pixelNum': 'Pixel Number'
            }

class UniverseForm(ModelForm):
    class Meta:
        model = Universe 
        fields = [
            'universeType',
            'universeNumber',
            'pixelOutUni',
            'multicast'
        ]
        labels = {
            'universeType': 'Type',
            'universeNumber': 'Universe Number',
            'pixelOutUni': 'Corresponding Output',
            'multicast': 'Multicast'
        }

class SettingsForm(ModelForm):
    class Meta:
        model = AppSettings
        fields = '__all__'