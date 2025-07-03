from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('docs/', TemplateView.as_view(template_name='docs_redirect.html'), name='docs_index'),

]
