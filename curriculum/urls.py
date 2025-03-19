from django.urls import path
from . import views

app_name = 'curriculum'

urlpatterns = [
    # Technique list view
    path('', views.TechniqueListView.as_view(), name='technique_list'),
    
    # Technique detail view
    path('technique/<int:pk>/', views.TechniqueDetailView.as_view(), name='technique_detail'),
    
    # Checkpoint detail view
    path('checkpoint/<int:pk>/', views.checkpoint_detail, name='checkpoint_detail'),
]