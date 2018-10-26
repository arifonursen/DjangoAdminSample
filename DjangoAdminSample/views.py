from django.shortcuts import render


def IndexView(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)


def ProductView(request, productTitle):
    template = 'Product.html'
    context = {
        'productTitle': productTitle
    }
    return render(request, template, context)