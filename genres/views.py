import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer

  
class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    

@csrf_exempt    
def genre_detail_view(request, pk):
    data = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        return JsonResponse(
                {"id": data.id, "name": data.name}
            )
    elif request.method == 'PUT':
        body = json.loads(request.body.decode('utf-8'))
        data.name = body.get('name')
        data.save()
        return JsonResponse(
                {"id": data.id, "name": data.name}
            )
    elif request.method == 'DELETE':
        data.delete()
        return JsonResponse(
                {"message": "Genre deleted"}, status=204
            )