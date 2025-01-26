from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Member)
admin.site.register(models.Transaction)
admin.site.register(models.TransactionType)
admin.site.register(models.Tulinaawe)
admin.site.register(models.TulinaaweContributor)
admin.site.register(models.Loan)
admin.site.register(models.LoanPayment)
admin.site.register(models.Expense)
admin.site.register(models.ExpenseItem)
admin.site.register(models.Settings)
admin.site.register(models.FinancialYear)
admin.site.register(models.NomineesForDeposits)
admin.site.register(models.NomineesForGFE)