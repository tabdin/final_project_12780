from django.urls import path
from . import views

# Based on urls.py in helloworld/pittrain
urlpatterns = [
    path("", views.hello, name="hello"),
    path("checkouts/", views.checkouts_json, name="checkouts_json"),
    path("equipment/", views.equipment_json, name="equipment_json"),
    path("checkout/", views.checkout_page, name="checkout_page"),
    path("return/", views.return_page, name="return_page"),
    path("chart/", views.checkouts_chart, name="checkouts_chart"),
]