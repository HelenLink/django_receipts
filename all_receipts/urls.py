from django.urls import path, register_converter
from . import views, converters

urlpatterns = [
    path('', views.index, name = 'all_receipts_index'),
    path('type', views.index2),
    path('<int:sign>',views.get_info_about_receipts_by_number),
    path('<str:sign>',views.get_info_about_receipts, name='eat-name'),
    path('type/<str:signtype>',views.get_info_about_type_bluda, name='type-name'),

]