from django.urls import path, include
from .views import (
    InstaListView
)

app_name = 'projectmini'

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', InstaListView.as_view(), name='post_list'),
]