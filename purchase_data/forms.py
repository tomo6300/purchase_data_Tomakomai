from django import forms
from .models import Item, PurchaseData

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'price', 'category')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

class PurchaseDataForm(forms.ModelForm):
    item = forms.CharField(label="購入商品", max_length=255)

    class Meta:
        model = PurchaseData
        fields = ('date', 'place', 'gender', 'age')
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_items(self):
        item = self.cleaned_data.get("item")
        items_list = item.split(",")
        return items_list