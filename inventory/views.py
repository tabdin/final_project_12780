from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Equipment, Checkout
import json
# Create your views here.
# Follows view structure from helloworld/pittrain/views.py

def hello(request):
    return HttpResponse("Hello from the Equipment Inventory App!")

def checkouts_json(request):
    data = list(Checkout.objects.values())
    return JsonResponse(data, safe=False)


def equipment_json(request):
    data = list(Equipment.objects.values())
    return JsonResponse(data, safe=False)

# error is 404
# view for checkout submission
def checkout_page(request):
    if request.method == "POST":
        equipmentName = request.POST.get("equipmentName")
        equipmentSerialNumber = request.POST.get("equipmentSerialNumber")
        borrowerName = request.POST.get("borrowerName")
        borrowerEmail = request.POST.get("borrowerEmail", "")
        checkoutDate = request.POST.get("checkoutDate")
        dueDate = request.POST.get("dueDate")

        if not (equipmentSerialNumber and borrowerName and checkoutDate and dueDate):
            return HttpResponse("Missing required fields", status=404)

        try:
            e = Equipment.objects.get(serialNumber=equipmentSerialNumber, isAvailable=True)
        except Equipment.DoesNotExist:
            return HttpResponse("Equipment not available", status=404)

        Checkout.objects.create(
            equipmentName=e.name,  
            equipmentSerialNumber=equipmentSerialNumber,
            equipmentType=e.equipmentType,
            borrowerName=borrowerName,
            borrowerEmail=borrowerEmail,
            checkoutDate=checkoutDate,
            dueDate=dueDate,
            returned=False,
        )

        e.isAvailable = False
        e.save()

        return HttpResponse("Checkout submitted successfully.")

    equipment = Equipment.objects.filter(isAvailable=True).order_by("name")
    return render(request, "checkout_page.html", {"equipment": equipment})


def return_page(request):
    if request.method == "POST":
        checkout_id = request.POST.get("checkout_id")
        if not checkout_id:
            return HttpResponse("Missing checkout_id", status=404)

        try:
            c = Checkout.objects.get(id=checkout_id)
        except Checkout.DoesNotExist:
            return HttpResponse("Checkout not found", status=404)

        c.returned = True
        c.save()
        try:
            e = Equipment.objects.get(serialNumber=c.equipmentSerialNumber)
            e.isAvailable = True
            e.save()
        except Equipment.DoesNotExist:
            pass

        return HttpResponse("Return submitted successfully.")

    active_checkouts = Checkout.objects.filter(returned=False).order_by("checkoutDate")
    return render(request, "return_page.html", {"active_checkouts": active_checkouts})


def checkouts_chart(request):
    active_checkouts = Checkout.objects.filter(returned=False)

    unique_types = []
    for c in active_checkouts:
        if c.equipmentType not in unique_types:
            unique_types.append(c.equipmentType)

    labels = []
    data = []

    for t in unique_types:
        labels.append(str(t))
        count = 0

        for c in active_checkouts:
            if c.equipmentType == t:
                count = count + 1

        data.append(count)

    return render(request, "checkouts_chart.html", {
        "labels": json.dumps(labels),
        "data": json.dumps(data),
    })
