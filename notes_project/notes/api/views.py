from rest_framework.decorators import api_view
from rest_framework.response import Response
from notes.models import Note
from .serializers import NoteSerializer
from rest_framework import status

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/notes',
        'GET /api/notes/id',
    ]
    return Response(routes)

@api_view(['GET'])
def getName(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def getNote(request, id, format = None):
    try:
        note = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    
    elif request.method == 'PUT':
        serializer = NoteSerializer(note, data= request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_403_FORBIDDEN)

    elif request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)