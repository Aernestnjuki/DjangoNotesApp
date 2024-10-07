from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializer import NoteSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
    routes = [
        '/notes/',
        '/notes/create',
        '/notes/id/update',
        '/notes/id/delete'
    ]

    return Response(routes)

# get all notes from the database

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

# get one note from the database

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

# create note
@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(body=data['body'])
    serializer = NoteSerializer(instance=note, many=False)
    return Response(serializer.data)

# update the notes route

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete note
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')