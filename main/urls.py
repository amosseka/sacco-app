from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('members/', views.members, name="members"),
    path('new-member/', views.new_member, name="new_member"),
    path('update-member/', views.update_member, name="update_member"),
    path('tulinaawe/', views.tulinaawe_view, name="tulinaawe"),
    path('tulinaawe/<slug>/', views.tulinaawe_detail, name="tulinaawe_detail"),
    path('welfare/', views.welfare_view, name="welfare"),
    path('loans/', views.loans_view, name="loans"),
    path('loans/<slug>', views.loan_detail, name="loan_detail"),
    path('loan/application/', views.loan_application_view, name="loan_application"),
    path('loan/application-detail/<slug>', views.loan_application_detail_view, name="loan_application_detail"),
    path('reports/', views.reports_view, name="reports"),
    path('expenses/', views.expenses_view, name="expenses"),
    path('expenses/<slug>/', views.expenses_detail, name="expenses_detail"),
    path('project-fee/', views.project_fee_view, name='project_fee'),
    path('vouchers/', views.vouchers_view, name='vouchers'),
    path('vouchers/<slug>/', views.vouchers_detail, name='vouchers_detail'),
    path('notes/', views.notes_view, name="notes"),

    path('<slug>/<slug2>-new-transaction/', views.member_new_transaction, name='member_new_transaction'),
    path('<slug>/<slug2>-transactions/', views.member_transactions, name="member_transactions"),

    path('<slug>/<slug2>-convert-savings/', views.convert_savings, name="convert_savings"),
    path('<slug>/<slug2>-pay-using-shares/', views.pay_using_shares, name="pay_using_shares"),

    path('new-transaction/', views.new_transaction, name="new_transaction"),
    path('all-transactions/', views.all_transactions, name="all_transactions"),
    path('transaction/<slug>/', views.transaction_view, name="transaction"),

    path('transaction/<slug>/detail/', views.transaction_detail, name="transaction_detail"),

    path('print/', views.print_view, name="print"),

    path('member/', views.member_info, name="member_info"),

    path('member-report/', views.member_report, name="member_report"),
    path('api/reports/', views.reports_api, name="reports_api"),
    path('api/member-report/', views.member_report_api, name="member_report_api"),

    path('api/member/', views.api_member_view, name='member-api'),
    path('api/transactions/', views.api_transaction_view, name='transactions-api'),

    path('settings/', views.settings_view, name="settings"),
]
