from django.shortcuts import render, redirect
from main.forms import ProductsForm
from main.models import Products
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products_entries = Products.objects.all()

    context = {
        'products_entries' : products_entries,
        'name': 'Indah Cahya Puspitahati',
        'npm' : '2306245453',
        'class': 'PBP A',
        'brand': 'HOODIE-YAY✨',  
    }
    return render(request, "main.html", context)

def create_products_entry(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products_entry.html", context)

def show_xml(request):
    data = Products.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Products.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Products.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Products.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
