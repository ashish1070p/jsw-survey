from django.urls import path
from . import views

urlpatterns = [
    # Welcome / Home
    path('', views.welcome, name='welcome'),

    # Survey forms – MT
    path('survey/mt/happy-sheet/', views.happy_sheet, {'role': 'mt'}, name='mt_happy_sheet'),
    path('survey/mt/pre-assessment/', views.pre_assessment, {'role': 'mt'}, name='mt_pre_assessment'),
    path('survey/mt/post-assessment/', views.post_assessment, {'role': 'mt'}, name='mt_post_assessment'),
    path('survey/mt/bars-technical/', views.bars_technical, {'role': 'mt'}, name='mt_bars_technical'),
    path('survey/mt/bars-behavioural/', views.bars_behavioural, {'role': 'mt'}, name='mt_bars_behavioural'),
    path('survey/mt/bars-leadership/', views.bars_leadership, {'role': 'mt'}, name='mt_bars_leadership'),
    path('survey/mt/success/', views.success, {'role': 'mt'}, name='mt_success'),

    # Survey forms – GET
    path('survey/get/happy-sheet/', views.happy_sheet, {'role': 'get'}, name='get_happy_sheet'),
    path('survey/get/pre-assessment/', views.pre_assessment, {'role': 'get'}, name='get_pre_assessment'),
    path('survey/get/post-assessment/', views.post_assessment, {'role': 'get'}, name='get_post_assessment'),
    path('survey/get/bars-technical/', views.bars_technical, {'role': 'get'}, name='get_bars_technical'),
    path('survey/get/bars-behavioural/', views.bars_behavioural, {'role': 'get'}, name='get_bars_behavioural'),
    path('survey/get/bars-leadership/', views.bars_leadership, {'role': 'get'}, name='get_bars_leadership'),
    path('survey/get/success/', views.success, {'role': 'get'}, name='get_success'),

    # Admin
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-qr-codes/', views.qr_codes, name='qr_codes'),
    path('admin-responses/<str:survey_type>/', views.admin_responses, name='admin_responses'),
    path('admin-export/<str:survey_type>/', views.export_excel, name='export_excel'),
]
