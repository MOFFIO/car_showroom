# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from cars_project.models import Car

@receiver(post_save, sender=Car)
def my_mail_sender(sender, created, **kwargs):
    if created:
        car_id = kwargs.get('instance').id
        car = Car.objects.get(id=car_id)
        car_dict = Car.car_as_dict(car)
        car_dict.update({u'car_id': car_id})
        send_mail('Subject here', 'Car Create', 'from@example.com',['to@example.com'], fail_silently=False,  html_message=str(car_dict))
