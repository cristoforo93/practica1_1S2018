# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    seo_title = models.CharField(max_length=60, blank=True, null=True)
    seo_description = models.CharField(max_length=165, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    STATUS_CHOICES = {
        ('Published', 'Published'),
        ('Draft', 'Draft'),
    }
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category)
    seo_title = models.CharField(max_length=60, blank=True, null=True)
    seo_description = models.CharField(max_length=165, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.CharField(max_length=10, default='Draft', choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    

