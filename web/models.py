import uuid
from django.db import models


# The `Flan` class defines a model with fields for a UUID, name, description, image URL, slug, and a
# boolean flag for private JavaScript.
class Flan(models.Model):
	flan_uuid = models.UUIDField(default=uuid.uuid4,editable=False)
	name = models.CharField(max_length=64)
	description = models.TextField()
	image_url = models.URLField(blank=True)
	slug = models.SlugField()
	js_private = models.BooleanField(default=False)


# This Python class defines a ContactForm model with fields for a unique identifier, customer email,
# customer name, and message.
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


class Cafe(models.Model):
    cafe_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    slug = models.SlugField()
    js_private = models.BooleanField(default=False)


class Dulce(models.Model):
    dulce_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    slug = models.SlugField()
    js_private = models.BooleanField(default=False)
    

