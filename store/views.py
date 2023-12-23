from django.shortcuts import render

from django.http import JsonResponse, HttpRequest, HttpResponseNotFound
from .models import DATABASE
from django.http import HttpResponse
from logic.services import filtering_category
from logic.services import view_in_cart, add_to_cart, remove_from_cart

def products_view(request):
    if request.method == "GET":
        id = request.GET.get('id')
        print(id)
        if id:
            for product in DATABASE.values():
                if product["id"] == int(id):
                    return JsonResponse(product, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})
            return HttpResponseNotFound("Данного продукта нет в базе данных")
        # return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
        #                                                     'indent': 4})

        if category_key := request.GET.get('category'):  # Считали 'category'
            if ordering_key := request.GET.get('ordering'):  # Если в параметрах есть 'ordering'
                if str(request.GET.get("reverse")).lower() == 'true':  # Если в параметрах есть 'ordering' и 'reverse'=True
                    data = filtering_category(DATABASE, category_key, ordering_key, reverse=True)  # TODO Провести фильтрацию с параметрами
                else:
                    data = filtering_category(DATABASE, category_key, ordering_key)  # TODO Провести фильтрацию с параметрами
            else:
                data = filtering_category(DATABASE, category_key)  # TODO Провести фильтрацию с параметрами
        else:
            data = DATABASE
        # В этот раз добавляем параметр safe=False, для корректного отображения списка в JSON
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False,
                                                                 'indent': 4})



def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ


def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            for products in DATABASE.values():
                if products['html'] == page:  # Если значение переданного параметра совпадает именем html файла
                    with open(f'store/products/{page}.html', encoding="utf-8") as f:
                        products = f.read()
                    return HttpResponse(products)
        elif isinstance(page, int):
            products = DATABASE.get(str(page))  # Получаем какой странице соответствует данный id
            if products:  # Если по данному page было найдено значение
                with open(f'store/products/{products["html"]}.html', encoding="utf-8") as f:
                    products = f.read()
                return HttpResponse(products)



        # Если за всё время поиска не было совпадений, то значит по данному имени нет соответствующей
        # страницы товара и можно вернуть ответ с ошибкой HttpResponse(status=404)
    return HttpResponse(status=404)




def cart_view(request):
    if request.method == "GET":
        data = view_in_cart()     # TODO Вызвать ответственную за это действие функцию
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})


def cart_add_view(request, id_product):
    if request.method == "GET":
        result = add_to_cart(id_product)    # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def cart_del_view(request, id_product):
    if request.method == "GET":
        result = remove_from_cart(id_product) # TODO Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})