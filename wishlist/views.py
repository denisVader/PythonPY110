from django.shortcuts import render

# Create your views here.
def wishlist_view(request):
    if request.method == "GET":
        return render(request, 'wishlist/wishlist.html') # TODO прописать отображение избранного. Путь до HTML - wishlist/wishlist.html