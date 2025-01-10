from django.shortcuts import render, redirect
from Korporeischen.models import Employee, Event
from Korporeischen.forms import Forms_Event, Swas_form

def glaw_stran(zapros):
    otwet = render(zapros, "Glaw_stran.html")
    return otwet

def stran_so_wsemi_rabami(zapros):
    rabotniki = Employee.objects.all()
    otwet = render(zapros, "stran_so_wsemi_rabami.html", {"rabotniki": rabotniki})
    return otwet

def stran_so_wsemi_eventomi(zapros):
    eventi = Event.objects.all()
    otwet = render(zapros, "stran_so_wsemi_eventomi.html", {"eventi": eventi})
    return otwet

def dan_eventa(zapros, id):
    try:
        event = Event.objects.get(id = id)
        otwet = render(zapros, "stran_so_wsemi_dannimi_eventa.html", {"event": event})
        return otwet
    except:
        otwet = render(zapros, "strann_404.html")
        return otwet

def lich_dan_rabotnika(zapros, id):
    rabotnik = Employee.objects.get(id = id)
    otwet = render(zapros, "stran_so_wsemi_dannimi_rabotnika.html", {"rabotnik": rabotnik})
    return otwet

def dobaw_event(zapros):
    if zapros.method == "GET":
        forma = Forms_Event()
        otwet = render(zapros, "Forms_Event.html", {"forma": forma})
        return otwet
    if zapros.method == "POST":
        forma = Forms_Event(zapros.POST)
        a = forma.is_valid()
        if a == True:
            forma.save()
            forma = Forms_Event()
        otwet = render(zapros, "Forms_Event.html", {"forma": forma})
        return otwet
    
def swas_team_event(request):
    if request.method == 'POST':
        form = Swas_form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            event = form.cleaned_data['event']
            team.event = event
            team.save()  # Сохранение изменений в базе данных
            return redirect('glawstran')  # Замените 'success' на вашу целевую страницу
    else:
        form = Swas_form()
    return render(request, 'Swas_team_event.html', {'form': form})