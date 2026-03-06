"""
URL configuration for medicore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from hospital.views import home, dashboard, doctors, patients, appointments, logout_view, book_appointment, login_view

urlpatterns = [

    # Homepage
    path('', home, name='home'),

    # Authentication
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),

    # Pages
    path('doctors/', doctors, name='doctors'),
    path('patients/', patients, name='patients'),
    path('appointments/', appointments, name='appointments'),

    # Book appointment
    path('book-appointment/', book_appointment, name='book'),

    # API
    path('api/', include('hospital.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Admin
    path('admin/', admin.site.urls),

]
from django.conf import settings
from django.conf.urls.static import static
# Media files (images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
