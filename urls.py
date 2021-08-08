from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi),
    path('mchoose', views.hi1),
    path('matbride', views.hi2),
    path('matgroom', views.hi3),
    path('mabout', views.hi4),
    path('mcontact', views.hi5),
    path('mprivacy', views.hi6),
    path('resume_akshay', views.hi7),
    path('resume_adharsh', views.hi8),
    path('resume_hari', views.hi9),
    path('resume_nihal', views.hi10),
    path('resume_neha', views.hi11),
    path('resume_amisha', views.hi12),
    path('resume_poornima', views.hi13),
    path('resume_parvathy', views.hi14),
    path('minterest1', views.hi15),
    path('minterest2', views.hi16),

]