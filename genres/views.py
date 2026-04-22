import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Genre


@csrf_exempt
def genre_view(request):
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