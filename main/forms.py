from django.forms import ModelForm
from main.models import Products
from django.utils.html import strip_tags

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "price", "description", "stock", "image"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        return strip_tags(stock)
    
    def clean_image(self):
        image = self.cleaned_data["image"]
        return strip_tags(image)