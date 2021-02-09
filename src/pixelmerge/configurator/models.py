from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Pixel(models.Model):
    RGB = 'RGB'
    RGBW = 'RGBW'
    typeChoices = [(RGB, 'RGB'), (RGBW, 'RGBW')]
    pixelType = models.CharField(
        max_length=4, 
        choices=typeChoices, 
        default=RGB
        )
    inputUniverse = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(255)])
    inputAddress = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(512)])
    outputUniverse = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)])
    outputAddress = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(512)])
    fixtureNum = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    pixelNum = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])

class Universe(models.Model):
    control = 'ctrlIn'
    consInput = 'consoleIn'
    pixInput = 'pixelIn'
    pixOutput = 'pixelOut'
    typeChoices = [
        (control, "Control Input"),
        (consInput, "Console Input"),
        (pixInput, "Pixel Input"),
        (pixOutput, "Pixel Output")
    ]
    universeType = models.CharField(
        max_length=13, 
        choices=typeChoices, 
        default=pixInput
        )
    universeNumber = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(512)])
    pixelOutUni = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(512)], default=0)
    multicast = models.BooleanField(default=True)
    available = models.BooleanField(default=False)

class AppSettings(models.Model):
    unicastIP = models.CharField(max_length=15)
    maxUniverses = models.IntegerField()
    consoleEnableChannel = models.IntegerField()
