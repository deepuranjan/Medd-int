# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import random


class Student(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.student_id = random.randint(1, 99999)
        self.gender = gender
        self.age = age