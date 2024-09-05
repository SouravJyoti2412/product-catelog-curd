from django.contrib import admin
from django.urls import path
from django.urls import path
from app.views import Product_curd , ProductSearch , ProductPopularityHighToLowList,ProductPopularityLowToHighList,ProductBuy

urlpatterns = [
    path('admin/', admin.site.urls),
    path("product-curd/", Product_curd.as_view()),
    path("product-search/" , ProductSearch.as_view()),
    path("product-popularity-high-to-low/", ProductPopularityHighToLowList.as_view()),
    path("product-popularity-low-to-high/", ProductPopularityLowToHighList.as_view()),
    path("product-buy/", ProductBuy.as_view())

    
]
