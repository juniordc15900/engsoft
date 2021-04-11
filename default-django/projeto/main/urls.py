from django.contrib import admin
from django.urls import path
from main import views
from django.template.response import TemplateResponse
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static' : StaticViewSitemap,
}

urlpatterns = [
    # Navegação # 
    path('',views.index,name='home'),
    path('menu/',views.index,name='home'),
    path('registrar-aula/',views.registerAula,name='atividade'),
    path('registrar-atividade/',views.registerAtividade,name='aula'),
    path('listar-aulas/',views.listaAulas,name='aulas'),
    path('listar-atividades/',views.listaAtividades,name='atividades'),
    path('delete/<str:delete_type>/<str:delete_pk>/',views.delete, name='delete'),
    path('edit/<str:edit_type>/<str:edit_pk>/',views.edit, name='edit'),

]

handler404 = views.error_404