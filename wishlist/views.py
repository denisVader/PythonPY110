from django.shortcuts import render
from django.contrib.auth import get_user
from django.http import JsonResponse
from store.models import DATABASE
from logic.services import view_in_wishlist, add_user_to_wishlist,add_to_wishlist,remove_from_wishlist


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