from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from django.http import JsonResponse
from store.models import DATABASE
from logic.services import view_in_wishlist, add_user_to_wishlist, add_to_wishlist, remove_from_wishlist


@login_required(login_url='login:login_view')
def wishlist_view(request):
    if request.method == "GET":
        current_user = get_user(request).username
        data = view_in_wishlist(request)[current_user]
        if request.GET.get('format') == 'JSON':
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})
        products = []
        for products_id in data['products']:
            products.append(DATABASE[products_id])

        return render(request, 'wishlist/wishlist.html', context={"products": products}) #  прописать отображение избранного. Путь до HTML - wishlist/wishlist.html


def wishlist_add_json(request, id_product: str):
    """
    Добавление продукта в избранное и возвращение информации об успехе или неудаче в JSON
    """
    if request.method == "GET":
        result = add_to_wishlist(request, id_product)  #  вызовите обработчик из services.py добавляющий продукт в избранное
        if result:
            return JsonResponse({"answer": f"Продукт id={id_product} успешно добавлен в избранное"},
                            json_dumps_params={'ensure_ascii': False})  #  верните JsonResponse с ключом "answer" и значением "Продукт успешно добавлен в избранное"

        return JsonResponse({"answer": "Неудачное добавление в избранное"},
                        status=404,
                        json_dumps_params={'ensure_ascii': False})  #  верните JsonResponse с ключом "answer" и значением "Неудачное добавление в избранное" и параметром status=404


def wishlist_del_json(request, id_product):
    if request.method == "GET":
        result = remove_from_wishlist(request,
                                  id_product)  # Вызвать ответственную за это действие функцию и передать необходимые параметры
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def wishlist_json(request):
    """
    Просмотр всех продуктов в избранном для пользователя и возвращение этого в JSON
    """
    if request.method == "GET":
        current_user = get_user(request).username  # from django.contrib.auth import get_user
        data = view_in_wishlist(request)[current_user]  # получите данные о списке товаров в избранном у пользователя
        if data:
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})  #  верните JsonResponse c data

        return JsonResponse({"answer": "Пользователь не авторизован"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})  #  верните JsonResponse с ключом "answer" и значением "Пользователь не авторизирован" и параметром status=404


def wishlist_del_html_view(request, id_product):
    if request.method == "GET":
        result = remove_from_wishlist(request, id_product)  # Вызвать функцию удаления из корзины
        if result:
            return redirect("wishlist:wishlist_view")  #  Вернуть перенаправление на корзину

        return HttpResponseNotFound("Неудачное удаление из корзины")