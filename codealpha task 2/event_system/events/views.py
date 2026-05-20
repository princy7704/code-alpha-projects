from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration
from django.contrib.auth.models import User


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    user = User.objects.first()

    Registration.objects.create(
        user=user,
        event=event
    )

    return redirect('event_list')

def my_registrations(request):
    user = User.objects.first()

    registrations = Registration.objects.filter(user=user)

    events = [reg.event for reg in registrations]

    return render(request, 'events/event_list.html', {
        'events': events
    })