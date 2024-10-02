from django.forms import ModelForm
from main.models import Products

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "price", "description", "stock", "image"]