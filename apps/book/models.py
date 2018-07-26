# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class Nav(models.Model):
    nav_id = models.IntegerField(primary_key=True)
    nav_name = models.CharField(unique=True, max_length=100)
    is_status = models.IntegerField()

    class Meta:
        db_table = 'nav'

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=250, blank=True, null=True,db_index=True)
    book_author = models.CharField(max_length=250, blank=True, null=True)
    book_text = models.CharField(max_length=1000, blank=True, null=True)
    book_img = models.CharField(max_length=250, blank=True, null=True)
    book_img_url = models.CharField(max_length=250, blank=True, null=True)
    book_class_1 = models.ForeignKey('BookClass1', models.DO_NOTHING)
    is_status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'book'


class BookClass(models.Model):
    book_class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=250, blank=True, null=True)
    class_url = models.CharField(max_length=250, blank=True, null=True)
    is_status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'book_class'


class BookClass1(models.Model):
    book_class_1_id = models.AutoField(primary_key=True)
    class_name_1 = models.CharField(max_length=250, blank=True, null=True, unique=True,db_index=True)
    book_class = models.ForeignKey(BookClass, models.DO_NOTHING)
    is_status = models.IntegerField()

    class Meta:
        db_table = 'book_class_1'




