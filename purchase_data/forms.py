from django import forms
from django.forms.models import inlineformset_factory
from .models import Item, PurchaseData, PurchaseDataDetail

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
    item = forms.ModelMultipleChoiceField(
        label = '購入商品',
        queryset=Item.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = PurchaseData
        fields = ('date', 'place', 'gender', 'age', 
        'item'
        )
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', "type": "datetime-local"}),
            'place': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
            'item': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
        }
    
    def clean_items(self):
        item = self.cleaned_data.get("item")
        items_list = item.split(",")
        return items_list

class PurchaseDataDetailForm(forms.ModelForm):
    item = forms.ModelMultipleChoiceField(
        label = '購入商品',
        queryset=Item.objects.all(),
    #    widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = PurchaseDataDetail
        fields = ('item','quantity',)

    #def __init__(self, *args, **kwargs):
    #    super(PurchaseDataDetailForm, self).__init__(*args, **kwargs)
#
    #    self.fields['item'].choices = lambda: [('', '-- 商品 --')] + [
    #        (item.id, '%s %s円' % (item.name.ljust(10, '　'), item.price)) for item in
    #        Item.objects]
#
    #    choices_number = [('', '-- 個数 --')] + [(str(i), str(i)) for i in range(1, 10)]
    #    self.fields['quantity'].widget = forms.widgets.Select(choices=choices_number)
    
    def clean_items(self):
        item = self.cleaned_data.get("item")
        items_list = item.split(",")
        return items_list

PurchaseDataDetailFormSet = inlineformset_factory(
    parent_model=PurchaseData,
    model=PurchaseDataDetail,
    form=PurchaseDataDetailForm,
    extra=1,
    min_num=1,
    validate_min=True,
)