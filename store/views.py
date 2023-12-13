from django.shortcuts import render

from django.http import JsonResponse, HttpRequest, HttpResponseNotFound
from .models import DATABASE
from django.http import HttpResponse


def products_view(request):
    if request.method == "GET":
        for data in DATABASE.values():
            if data[id] == DATABASE:
                return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})
    return HttpResponseNotFound



def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ


def products_page_view(request, page):
    pass
    # if request.method == "GET":
    #     for data in DATABASE.values():
    #       if data['html'] == page:      # Если значение переданного параметра совпадает именем html файла.
    #     # TODO 1. Откройте файл open(f'store/products/{page}.html', encoding="utf-8") (Не забываем про контекстный менеджер with)
    #     # TODO 2. Прочитайте его содержимое
    #     # TODO 3. Верните HttpResponse c содержимым html файла
    #
    #     # Если за всё время поиска не было совпадений, то значит по данному имени нет соответствующей
    #     # страницы товара и можно вернуть ответ с ошибкой HttpResponse(status=404)
    #    # return HttpResponse(status=404)