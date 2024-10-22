from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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
        'POST /api/token/',
        'POST /api/token/refresh/',
        'POST /api/register/',
        'GET /api/profile/',
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getName(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
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