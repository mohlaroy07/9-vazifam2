from django.shortcuts import render, get_object_or_404
from .models import Category, Ad


from django.shortcuts import render
from .models import Category, Ad

def home(request):
    categories = Category.objects.all()
    ads = Ad.objects.all()

    context = {
        'categories': categories,
        'ads': ads,
    }

    return render(request, 'home.html', context)

def ad_detail(request, id):
    ad = get_object_or_404(Ad, id=id)
    context = {
        'ad': ad,
    }
    return render(request, 'ad_detail.html', context)


def select_by_category(request, category_id):

    categories = Category.objects.all()
    ads = Ad.objects.filter(category_id=category_id)

    context = {
        'categories': categories,
        'ads': ads,
    }
    return render(request, 'home.html', context)