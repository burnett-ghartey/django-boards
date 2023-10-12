from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse
from ..views import home, board_topics
from ..models import Board,Post,Topic

# Create your tests here.


