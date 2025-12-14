from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# reference from models.py in helloworld/pittrain

# Create your models here.


# Two models: Equipment and Checkout
# These models are for an inventory management system
# charfield is better for short text
# textfield is better for long text

class Equipment(models.Model):
    dateAdded = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    equipmentType = models.CharField(
        max_length=50,
        choices=[
            ("scope", "Oscilloscope"),
            ("mcu", "Microcontroller"),
            ("sensor", "Sensor"),
            ("psu", "Power Supply"),
            ("fpga", "Field Programmable Gate Array"),
            ("other", "Other"),
        ],
    )
    serialNumber = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.serialNumber})"

class Checkout(models.Model):
    dateAdded = models.DateField(auto_now_add=True)

    equipmentName = models.CharField(max_length=100)
    equipmentSerialNumber = models.CharField(max_length=100)

    borrowerName = models.CharField(max_length=100)
    # django has a built-in email field type that does validation
    borrowerEmail = models.EmailField(blank=True)

    checkoutDate = models.DateField()
    dueDate = models.DateField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.borrowerName}: {self.equipmentName}"