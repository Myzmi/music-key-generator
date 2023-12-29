from django.shortcuts import render, redirect
from django.urls import reverse
#from django.http import HttpResponseRedirect
from .models import KeyTable
import random

notes=['A','As','B','C','Cs','D','Ds','E','F','Fs','G','Gs']
scales=['maj', 'min']

# Create your views here.
def index(request):
    return render(request, "key/index.html")

def keyPage(request, note, type):
    if len(note)==2:
        note=f"{note[0]}#"
    if type=='maj':
        type='Major'
    elif type=='min':
        type='Minor'
    table = KeyTable.objects.get(rootNote=note, scale=type)
    #print(table)
    return render(request, "key/page.html", {
        "note": note,
        "type": type,
        "table": table
    })

def key(request):
    if request.method == "POST":
        note = request.POST["note"]
        type = request.POST["type"]
        indexUrl = reverse('index')
        targetUrl = f"{indexUrl}{note}/{type}"
        #print(targetUrl)
        return redirect(targetUrl)
    
def randomKey(request):
    note=random.choice(notes)
    type=random.choice(scales)
    indexUrl = reverse('index')
    targetUrl = f"{indexUrl}{note}/{type}"
    #print(targetUrl)
    return redirect(targetUrl)