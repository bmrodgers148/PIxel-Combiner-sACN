from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import Pixel, Universe
from .forms import *
from .main import *


# Create your views here.
def home_view(request, *args, **kwargs):
    pixels = Pixel.objects.all()
    universes = Universe.objects.all()
    return render(request, "home.html", {"running": running, "pixels": pixels, "universes": universes})

def pixel_view(request, pk, *args, **kwargs):
    if pk == 'New':
        prevEntry = Pixel.objects.latest('id')
        initial_data = {
            'pixelType': prevEntry.pixelType,
            'inputUniverse': prevEntry.inputUniverse,
            'inputAddress': prevEntry.inputAddress,
            'outputUniverse': prevEntry.outputUniverse,
            'outputAddress': prevEntry.outputAddress,
            'fixtureNum': prevEntry.fixtureNum,
            'pixelNum': prevEntry.pixelNum,
        }
        initial_data['outputAddress'] += 3
        initial_data['pixelNum'] += 1
        if (512 - initial_data['outputAddress']) < 3 and initial_data['pixelType'] == 'RGB':
            initial_data['outputUniverse'] += 1
            initial_data['outputAddress'] = 1
        if (initial_data['outputAddress'] >= 512 and initial_data['pixelType'] == 'RGBW'):
            initial_data['outputUniverse'] += 1
            initial_data['outputAddress'] = 1
        form = PixelForm(request.POST or None, initial=initial_data)
    else:
        form = PixelForm(request.POST or None, instance=Pixel.objects.get(id=pk))
    
    
    if form.is_valid():
        form.save()
        return redirect('/pixel/New')
    pixels = Pixel.objects.all().order_by('-outputUniverse', '-outputAddress')
    context = {"running": running,"pixels": pixels,"form": form}
    return render(request, "pixel.html", context)

def delete_pixel_view(request, pk):
    if len(Pixel.objects.all()) > 1:
        pixel = Pixel.objects.get(id=pk)
        pixel.delete()
    return redirect('/pixel/New/')

def universe_view(request, pk, *args, **kwargs):
    if pk == 'New':
        prevEntry = Universe.objects.latest('id')
        initial_data = {
            'universeType': prevEntry.universeType,
            'universeNumber': (prevEntry.universeNumber + 1 ),
            'multicast': prevEntry.multicast
        }
        form = UniverseForm(request.POST or None, initial=initial_data)
    else:
        form = UniverseForm(request.POST or None, instance=Universe.objects.get(id=pk))
    if form.is_valid():
        form.save()
    universes = Universe.objects.all().order_by('-universeNumber')
    context = {"running": running,"universes": universes,"form": form}
    return render(request, "universe.html", context)

def delete_universe_view(request, pk):
    if len(Universe.objects.all()) > 1:
        universe = Universe.objects.get(id=pk)
        universe.delete()
    return redirect('/universe/New/')

def settings_view(request, *args, **kwargs):
    form = SettingsForm(request.POST or None, instance=AppSettings.objects.get(id=1))
    if form.is_valid():
        form.save()
    context = {"running": running,"form": form}
    return render(request, "settings.html", context)

def start_sACN_view(request, *args, **kwargs):
    global running, maxUniverses, unicastIP, consoleEnableChannel
    settings = AppSettings.objects.get(id=1)
    consoleEnableChannel = settings.consoleEnableChannel
    maxUniverses = settings.maxUniverses
    unicastIP = settings.unicastIP
    startsACN(Universe.objects.all(), Pixel.objects.all(), maxUniverses, consoleEnableChannel, unicastIP)
    running = True
    availableUnis = refreshUniverse()
    unis = Universe.objects.all()
    for u in unis:
        if u.universeNumber in availableUnis:
            u.available = True
        else:
            u.available = False
        u.save()
    return redirect('../')
    
def stop_sACN_view(request, *args, **kwargs):
    global running
    stopsACN()
    running = False
    unis = Universe.objects.all()
    for u in unis:
        u.available = False
        u.save()
    
    return redirect('../')

def refresh_universes(request, *args, **kwargs):
    availableUnis = refreshUniverse()
    unis = Universe.objects.all()
    for u in unis:
        if u.universeNumber in availableUnis:
            u.available = True
        else:
            u.available = False
        u.save()
    return redirect('../')