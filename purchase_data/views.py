from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django import forms
from .forms import ItemForm, PurchaseDataForm
from .models import Item, PurchaseData
from . import draw_utils

class IndexView(TemplateView):
    template_name = 'index.html'

class ItemCreateView(CreateView):
    template_name = 'item/item_create.html'
    form_class = ItemForm
    success_url = reverse_lazy('purchase_data:item_create_complete')

class PurchaseDataCreateView(CreateView):

    model = PurchaseData
    template_name = 'purchase_data/purchase_data_create.html'
    form_class = PurchaseDataForm
    success_url = reverse_lazy('purchase_data:purchase_data_create_complete')

    #def get(self, request, *args, **kwargs):
    #    
    #    items   = Item.objects.all()
    #    data    = PurchaseData.objects.all()
    #    context = { "data":data,
    #                "items":items }
#
    #    return render(request,"purchase_data/purchase_data_create.html",context)
    
    def form_valid(self, form: forms.ModelForm) -> HttpResponse:
        purchase_data = form.save(commit=False)
        items_list = form.cleaned_data.get("item")
	
        purchase_data.save()
	
        if items_list:
            for item in items_list:
                purchase_data.item.add(Item.objects.get_or_create(name=item)[0])
	    
        form.save_m2m()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):

        form = PurchaseDataForm(request.POST)

        if form.is_valid():
            print("バリデーションOK")
            form.save()

        else:
            print("バリデーションNG")

        return redirect("purchase_data:purchase_data_create")
    
    
class ItemCreateCompleteView(TemplateView):
    template_name = 'item/item_create_complete.html'

class PurchaseDataCreateCompleteView(TemplateView):
    template_name = 'purchase_data/purchase_data_create_complete.html'

class ItemListView(ListView):
    template_name = 'item/item_list.html'
    model = Item

class PurchaseDataListView(ListView): ###
    template_name = 'purchase_data/purchase_data_list.html'
    model = PurchaseData

    def get(self, request):
        data    = PurchaseData.objects.all()

        m = draw_utils.visualize_locations()
        m2 = draw_utils.visualize_locations2()
        barfig =draw_utils.draw_graph() 
        circlefig = draw_utils.draw_circle()
        context = { "purchase_data_list":data,
                    'map':m,
                    'map2':m2,
                    'bar':barfig,
                    'circle':circlefig
                    }
        return render(request,"purchase_data/purchase_data_list.html",context)

    



class ItemDetailView(DetailView):
    template_name = 'item/item_detail.html'
    model = Item

class PurchaseDataDetailView(DetailView):
    template_name = 'purchase_data/purchase_data_detail.html'
    model = PurchaseData

class ItemUpdateView(UpdateView):
    template_name = 'item/item_update.html'
    model = Item
    fields = ('name', 'price', 'category')
    success_url: reverse_lazy('purchase_data:item_list')
 
    def form_valid(self, form):
        item = form.save(commit=False)
        item.updated_at = timezone.now()
        item.save()
        return super().form_valid(form)

class PurchaseDataUpdateView(UpdateView):
    template_name = 'purchase_data/purchase_data_update.html'
    model = PurchaseData
    fields = ('date', 'place', 'gender', 'age', 'items')
    success_url: reverse_lazy('purchase_data:purchase_data_list')
 
    def form_valid(self, form):
        purchase_data = form.save(commit=False)
        purchase_data.updated_at = timezone.now()
        purchase_data.save()
        return super().form_valid(form)

class ItemDeleteView(DeleteView):
    template_name = 'item/item_delete.html'
    model = Item
    success_url = reverse_lazy('purchase_data:item_list')

class PurchaseDataDeleteView(DeleteView):
    template_name = 'purchase_data/purchase_data.html'
    model = PurchaseData
    success_url = reverse_lazy('purchase_data:purchase_data_list')