from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from .models import Vehicle, Category,Car_or_Bike

from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from .models import Vehicle, Category, Car_or_Bike, Brand, VehicleModel

class VehicleListView(View):
    
    def get(self, request, *args, **kwargs):

        search_text=request.GET.get("search-text")

        selected_category=request.GET.get("category", "all") 

        selected_type=request.GET.get("type", "all")

        selected_brand=request.GET.get("brand", "all")

        selected_model=request.GET.get("model", "all")

        min_price=request.GET.get("min_price", "")
        max_price=request.GET.get("max_price", "")

        min_year_obj=VehicleModel.objects.order_by("year").first()
        max_year_obj=VehicleModel.objects.order_by("-year").first()

        # ✅ Ensure min_year is at least 2000
        min_year = max(2000, min_year_obj.year) if min_year_obj else 2000

        # ✅ Ensure max_year does not exceed 2025
        max_year = min(2025, max_year_obj.year) if max_year_obj else 2025

        # ✅ Generate year range from 2000 to 2025
        year_range = list(range(min_year, max_year + 1))


        qs = Vehicle.objects.all()

        if selected_category !="all":
            qs = qs.filter(category__name=selected_category)

        if selected_type !="all":
            qs = qs.filter(type__name=selected_type)

        if selected_brand !="all":
            qs = qs.filter(brand__name=selected_brand)

        if selected_model !="all":
            qs = qs.filter(model__year=selected_model)

        # price 

        if min_price:
            qs = qs.filter(price__gte=min_price)

        if max_price:
            qs = qs.filter(price__lte=max_price)

        # search bar 
        if search_text:
            qs = qs.filter(
                Q(Vehicle_name__icontains=search_text) | 
                Q(brand__name__icontains=search_text) | 
                Q(model__year__icontains=search_text) | 
                Q(year_of_manufacture__icontains=search_text) | 
                Q(price__icontains=search_text) | 
                Q(kilometers_driven__icontains=search_text) | 
                Q(ownership_status__icontains=search_text)
            )

       

        selected_model = request.GET.get("model", str(min_year))


        categories=Category.objects.all()
        types=Car_or_Bike.objects.all()
        brands=Brand.objects.all()
        models=VehicleModel.objects.all()
        last_model = VehicleModel.objects.last()

        return render(request, 'vehicle_list.html', {
            'vehicles': qs,
            'categories': categories,
            'selected_category': selected_category,
            "types": types,
            "selected_type": selected_type,
            "brands": brands,
            "selected_brand": selected_brand,
            "models": models,
            "selected_model": selected_model,
            "min_price": min_price,
            "max_price": max_price,
            'last_model': last_model, 

            "year_range": year_range,
            "min_year": min_year,
            "max_year": max_year,
        })
    
class vehicle_details_view(View):

    def get(self,request,*args,**kwargs):

        vehicle_id=kwargs.get('pk')

        vehicle=Vehicle.objects.get(id=vehicle_id)

        return render(request,'vehicle_details.html',{'vehicle':vehicle})
