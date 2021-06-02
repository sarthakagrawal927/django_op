from django.http import JsonResponse

from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()
    data = {"prdoucts": list(products.values())}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "price": product.price,
            "photo": product.photo.url,
            "quantity": product.quantity,
            "shipping_cost": product.shipping_cost}}
        response = JsonResponse(data)

    except Product.DoesNotExist:
        response = JsonResponse({"error": {
            "code": 404, "message": "not found"
        }}, status=404)
    return response


def manufacturer_list(request):
    manufacturer = Manufacturer.objects.filter(active=True)
    data = {"manufacturer": list(manufacturer.values())}
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all()
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
            "products": list(manufacturer_products.values())}}
        response = JsonResponse(data)

    except Manufacturer.DoesNotExist:
        response = JsonResponse({"error": {
            "code": 404, "message": "not found"
        }}, status=404)
    return response

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"
