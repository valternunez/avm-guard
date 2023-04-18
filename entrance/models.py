from django.db import models


class Apartment(models.Model):
    number = models.IntegerField()
    tower = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.tower} - {self.number}"

class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    apartments = models.ManyToManyField(Apartment, through='Ownership')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.apartments}"

class Tenant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    owners = models.ManyToManyField(Owner)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.apartment}"

class Ownership(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

class NonResident(models.Model):
    VISIT_TYPE = 'visit'
    SUPPLIER_TYPE = 'supplier'
    EVENT_ATTENDEE_TYPE = 'event_attendee'
    TYPE_CHOICES = (
        (VISIT_TYPE, 'Visit'),
        (SUPPLIER_TYPE, 'Supplier'),
        (EVENT_ATTENDEE_TYPE, 'Event Attendee'),
    )

    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_photo = models.ImageField(upload_to='nonresidents')
    plate_photo = models.ImageField(upload_to='nonresidents')
    apartment_visiting = models.ForeignKey(
        Apartment,
        on_delete=models.CASCADE,
        related_name='visiting_nonresidents'
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=50)
    
    def __str__(self):
        return f"{self.name} {self.last_name}"
    
class SecurityGuard(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)