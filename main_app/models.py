from django.db import models

# Create your models here.

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# model for dog
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# model for cat
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# Feeding model
class Feeding(models.Model):
    date = models.DateField("Feeding date")
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default = MEALS[0][0]
    )
    # One to many relations with dog and cat
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    # dog = models.ForeignKey(Dog, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
    



    