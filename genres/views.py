import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Genre


@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data.get('name'))
        new_genre.save()
        return JsonResponse(
            {"id": new_genre.id, "name": new_genre.name}, safe=False, status=201
        )

    elif request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(
            data, safe=False
        )
    

@csrf_exempt    
def genre_detail_view(request, pk):
    data = get_object_or_404(Genre, pk=pk)

    return JsonResponse(
            {"id": data.id, "name": data.name}, safe=False
        )