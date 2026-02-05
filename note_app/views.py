from django.shortcuts import render
from .models import Note
# Create your views here.


def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'note_app/note_list.html', {'notes': notes})

