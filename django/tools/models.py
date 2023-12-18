from django.db import models

# Create your models here.

class Drawing(models.Model):
    drawing_name = models.CharField(max_length=200)
    svg = models.TextField()
    parent_drawing = models.ForeignKey(Drawing)
    displacement-x = models.FloatField()
    displacement-y = models.FloatField()
    width = models.FloatField()
    add_date = models.DateTimeField("date added", auto_now_add = True)

class Place(models.Model):
    place_name = models.CharField(max_length=200)
    drawing = models.ForeignKey(Drawing)
    add_date = models.DateTimeField("date added" , auto_now_add = True)

class Pile(models.Model):
    pile_name = models.CharField(max_length=200)
    place = models.ForeignKey(Place)
    add_date = models.DateTimeField("date added", auto_now_add = True)

class Object(models.Model):
    question_name = models.CharField(max_length=200)
    add_date = models.DateTimeField("date added", auto_now_add = True)
    pile = models.ForeignKey(Pile) 

