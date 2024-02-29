"""
URL configuration for valvenumerique project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home,name="home"),
    path('doc/', views.doc,name="doc"),
    path('ann_igf', views.ann_igf,name="ann_igf"),
    path('ann_saft', views.ann_saft,name="ann_saft"),
    path('blog_interne', views.blog_interne,name="blog_interne"),
    path('service', views.service,name="service"),
    path('contact', views.contact,name="contact"),
    path('actu_accueil', views.actu_accueil,name="actu_accueil"),
    path('form_actual', views.form_actual, name="form_actual"),
    path('formajout_doc', views.formajout_doc, name="formajout_doc"),
    path('listactualitepub', views.listactualitepub, name="listactualitepub"),
    path('contactform', views.contactform, name="contactform")
 

]
