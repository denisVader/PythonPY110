from django.urls import path
from .views import wishlist_view, wishlist_del_html_view, wishlist_add_json, wishlist_json, wishlist_del_json

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist_view, name="wishlist_view"),     #  Зарегистрируйте обработчик
    path('api/add/<str:id_product>/', wishlist_add_json),
    path('api/del/<str:id_product>/', wishlist_del_json),
    path('api/', wishlist_json),
    path('del/<str:id_product>', wishlist_del_html_view, name="remove_now"),
]