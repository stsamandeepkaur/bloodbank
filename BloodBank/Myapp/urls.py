from django.conf.urls import url
from Myapp import views

app_name = 'Myapp'
urlpatterns= [
    url('donorRegisteration/', views.donor, name='donor'),
    url('DonorList/',views.donors, name='donors')

]
