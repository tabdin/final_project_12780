import pytest
from inventory.models import Equipment, Checkout

# https://pytest-django.readthedocs.io/en/latest/helpers.html

@pytest.mark.django_db
def test_equipment_create():
    e = Equipment.objects.create(
        name="Test Scope",
        equipmentType="scope",
        serialNumber="TEST-001",
        location="ECE Lab",
        quantity=1,
        isAvailable=True,
    )
    assert e.id is not None
    assert e.serialNumber == "TEST-001"


@pytest.mark.django_db
def test_checkout_page_loads(client):
    response = client.get("/checkout/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_checkout_sets_unavailable(client):
    Equipment.objects.create(
        name="Arduino",
        equipmentType="mcu",
        serialNumber="MCU-001",
        location="Hamerschlag",
        quantity=1,
        isAvailable=True,
    )

    response = client.post("/checkout/", data={
        "equipmentSerialNumber": "MCU-001",
        "borrowerName": "Student",
        "borrowerEmail": "student@andrew.cmu.edu",
        "checkoutDate": "2025-12-15",
        "dueDate": "2025-12-20",
    })

    assert response.status_code == 200
    assert Checkout.objects.count() == 1

    e = Equipment.objects.get(serialNumber="MCU-001")
    assert e.isAvailable is False
