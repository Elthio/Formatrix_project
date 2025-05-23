"""
URL configuration for formatrix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import register_view, home_view, admin_register_view
from django.conf import settings
from django.conf.urls.static import static
from formateurs import urls as formateurs_urls

urlpatterns = [
    # L'administration Django doit rester active pour le fonctionnement du site,
    # mais nous avons masqué le lien dans la barre latérale
    path('formatrix/admin/', admin.site.urls),
    
    # URLs pour les templates de formateurs - déplacé en haut pour priorité
    path('formateurs/', include((formateurs_urls.urlpatterns, 'formateurs'))),
    
    # API URLs - using REST framework
    path('api/', include(('cours.urls', 'api_cours'))),
    path('api/', include('modules.urls')),
    path('api/', include('documents.urls')),
    path('api/', include('renouvellements.urls')),
    # path('api/', include('seances.urls')),  # Commenté car nous utilisons maintenant des vues basées sur des classes
    path('api/seances/', include('seances.api_urls')),  # Nouvelle URL pour l'API des séances
    path('api/', include(('clients.urls', 'clients'))),  # Ajout du namespace 'clients'
    path('api/', include('lieux.urls')),
    path('api/', include('apprenants.urls')),
    path('api/', include(('inscriptions.urls', 'api'), namespace='api')),
    path('api/', include('evaluations.urls')),
    path('api/', include('presences.urls')),
    
    # URLs pour les templates
    path('cours/', include(('cours.urls', 'cours'))),
    path('seances/', include(('seances.urls', 'seances'))),
    path('apprenants/', include(('apprenants.template_urls', 'apprenants'))),
    path('clients/', include(('clients.urls', 'clients'))),
    path('inscriptions/', include(('inscriptions.urls', 'inscriptions'))),
    path('lieux/', include(('lieux.urls', 'lieux'))),  # Ajout de l'URL pour les templates de lieux
    path('paiements/', include(('paiements.urls', 'paiements'))),  # Ajout de l'URL pour les paiements
    path('rapports/', include(('rapports.urls', 'rapports'))),  # Ajout de l'URL pour les rapport
    path('notifications/', include(('notifications.urls', 'notifications'))),  # Ajout des URLs de notifications
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_view, name='register'),
    path('admin-register/', admin_register_view, name='admin-register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logged_out.html'), name='logout'),
    path('', home_view, name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
