from django.db import models
from django.core.exceptions import ValidationError
import re


class FinancialYearManager(models.Manager):
	
	def fn_manager(self, start_date, end_date):
		return super().get_queryset().filter(date__range=(start_date, end_date))

class LoanFinancialYearManager(models.Manager):

	def fn_manager(self, start_date, end_date):
		return super().get_queryset().filter(date_created__range=(start_date, end_date))
	

class ExpensesFinancialYearManager(models.Manager):

	def fn_manager(self, start_date, end_date):
		return super().get_queryset().filter(date__range=(start_date, end_date))


class VoucherFinancialYearManager(models.Manager):

	def fn_manager(self, start_date, end_date):
		return super().get_queryset().filter(date__range=(start_date, end_date))
	

class ProjectFeeYearManager(models.Manager):

	def fn_manager(self, start_date, end_date):
		return super().get_queryset().filter(date__range=(start_date, end_date))


class Settings(models.Model):
	id = models.BigAutoField(primary_key=True)
	results_order = models.CharField(max_length=255, default="show last added")

	def __str__(self):
		return "%s"%self.id


class FinancialYear(models.Model):
	id = models.BigAutoField(primary_key=True)
	first_date = models.DateTimeField()
	second_date = models.DateTimeField()
	active = models.BooleanField(default=False)
	settings = models.ForeignKey(Settings, on_delete=models.CASCADE)

	def __str__(self):
		return "%s --> %s"%(self.first_date.date().strftime('%x') ,self.second_date.date().strftime('%x')) 


class Member(models.Model):

	#Choices

	gender_choices = [
		("male", "Male"),
		("female", "Female"),
	]

	marital_status_choices = [
		("single", "Single"),
		("married", "Married")
	]

	source_of_income_choices = [
		("salary", "Salary"),
		("business", "Business"),
		("pension", "Pension")
	]

	business_sector_choices = [
		("transport", "Transport"),
		("hospitality", "Hospitality"),
		("real_estate", "Real Estate"),
		("tourism", "Tourism"),
		("wholesale_retail", "Wholesale / Retail"),
		("financial_services", "Financial Services"),
		("health_care", "Health Care"),
		("manufacturing", "Manufacturing"),
		("education", "Education")
	]

	mode_of_remittance_choices = [
		("check_off", "Check Off"),
		("direct_deposit", "Direct Deposit"),
		("standing_order", "Standing Order"),
		("pay_bill_m_money", "Paybill (M-Money)")
	]



	#Basic Details
	id = models.BigAutoField(primary_key=True)
	code = models.CharField(max_length=255, unique=True)
	image = models.ImageField(blank=False, null=False)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	full_names = models.CharField(max_length=255, default="")
	contact = models.CharField(max_length=255)
	date_joined = models.DateTimeField()

	#Applicant Details
	email_address = models.EmailField(blank=True)
	residence = models.CharField(max_length=255, blank=True)
	town = models.CharField(max_length=255, blank=True)
	box_no = models.CharField(max_length=255, blank=True)
	town_code = models.CharField(max_length=255, blank=True)
	marital_status = models.CharField(max_length=255, choices=marital_status_choices)
	gender = models.CharField(max_length=255, choices=gender_choices)
	date_of_birth = models.DateTimeField(null=True, blank=True)
	identification_no = models.CharField(max_length=255, blank=True)
	source_of_income = models.CharField(max_length=255, blank=True, choices=source_of_income_choices)

	#Employment Details
	employer = models.CharField(max_length=255, blank=True)
	date_of_employment = models.DateTimeField(null=True, blank=True)
	employment_address = models.CharField(max_length=255, blank=True)
	position_in_employment = models.CharField(max_length=255, blank=True)
	staff_number = models.CharField(max_length=255, blank=True)

	#Business Details
	business_name = models.CharField(max_length=255, blank=True)
	business_address = models.CharField(max_length=255, blank=True)
	business_sector = models.CharField(max_length=255, blank=True, choices=business_sector_choices)
	business_sector_others = models.TextField(blank=True)
	business_location = models.CharField(max_length=255, blank=True)
	business_monthly_income = models.PositiveIntegerField(default=0, blank=True)

	#Remittance
	proposed_monthly_contribution = models.IntegerField(default=0, blank=True)
	effective_date = models.DateTimeField(null=True, blank=True)
	amount_in_words = models.CharField(max_length=255, blank=True)
	mode_of_remittance = models.CharField(max_length=255, blank=True, choices=mode_of_remittance_choices)

	#Totals
	shares = models.IntegerField(default=0)
	welfare = models.IntegerField(default=0)
	savings = models.IntegerField(default=0)
	withdraw = models.IntegerField(default=0)
	fines = models.IntegerField(default=0)
	other = models.IntegerField(default=0)
	project_fee = models.IntegerField(default=0)

	#Official Declaration
	data_captured_by = models.CharField(max_length=255, blank=True)
	data_date_capture = models.DateTimeField(null=True, blank=True)
	system_approval_by = models.CharField(max_length=255, blank=True)
	system_approval_date = models.DateField(null=True, blank=True)
	membership_approved_by = models.CharField(max_length=255, blank=True)
	membership_approval_date = models.DateTimeField(null=True, blank=True)
	admitted_by_1 = models.CharField(max_length=255, blank=True)
	admitted_by_1_date = models.DateTimeField(null=True, blank=True)
	admitted_by_2 = models.CharField(max_length=255, blank=True)
	admitted_by_2_date = models.DateTimeField(null=True, blank=True)

	class Meta:
		ordering = ["code"]

	@property
	def date_fields(self):
		return ['date_joined', 'date_of_birth', 'date_of_employment', 'effective_date', 'data_date_capture', 'system_approval_date', 'membership_approval_date', 'admitted_by_1_date', 'admitted_by_2_date']

	@property
	def name_snippet(self):
		if len(self.full_names) > 18:
			return "%s..."%(self.full_names[0:18])
		else:
			return self.full_names

	@property
	def full_name(self):
		return '%s %s'%(self.first_name, self.last_name)

	def clean(self):
		code_pattern = r'KYDI/\d+'
		contact_pattern = r'^\d{10}$'

		match_code = re.match(code_pattern, self.code)
		match_contact = re.match(contact_pattern, self.contact)

		if not match_code:
			raise ValidationError({'code': 'Code should be in the form KYDI/000'})

		if not match_contact:
			raise ValidationError({'contact': 'Invalid Contact'})
	        
	def save(self, *args, **kwargs):
		self.full_names = "%s %s"%(self.first_name, self.last_name)
		self.full_clean()
		return super().save(*args, **kwargs)

	def __str__(self):
		return "%s - %s"%(self.code, self.full_names)



class NomineesForDeposits(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=255)
	id_no = models.CharField(max_length=255)
	relationship = models.CharField(max_length=255, default="")
	percentage = models.PositiveIntegerField(default=0)
	date_of_birth = models.DateTimeField()
	mobile_no = models.CharField(max_length=255)

	member = models.ForeignKey(Member, on_delete=models.CASCADE)

	def __str__(self): 
		return "%s --> %s"%(self.name, self.member)


class NomineesForGFE(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=255)
	id_no = models.CharField(max_length=255)
	relationship = models.CharField(max_length=255, default="")
	percentage = models.PositiveIntegerField(default=0)
	date_of_birth = models.DateTimeField()
	mobile_no = models.CharField(max_length=255)

	member = models.ForeignKey(Member, on_delete=models.CASCADE)

	def __str__(self):
		return "%s -> %s"%(self.name, self.member)
	

class Transaction(models.Model):
	id = models.BigAutoField(primary_key=True)

	fines_choices = [
		("General Meeting", "General Meeting"),
		("Weekly Meeting", "Weekly Meeting"),
		("Late", "Late"),
		("Uniform", "Uniform"),
		("Minimum Savings", "Minimum Savings"),
	]

	date = models.DateTimeField()
	shares = models.IntegerField(default=0)
	welfare = models.IntegerField(default=0)
	savings = models.IntegerField(default=0)
	withdraw = models.IntegerField(default=0)
	project_fee = models.IntegerField(default=0)
	fines = models.IntegerField(default=0)
	fine_type = models.CharField(max_length=255, choices=fines_choices, null=True, blank=True)
	other = models.IntegerField(default=0, blank=True)
	notes = models.TextField(blank=True)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)

	objects = FinancialYearManager()

	@property
	def notes_snippet(self):
		return "%s..."%(self.notes[0:70])

	class Meta:
		ordering = ["-date", "member"]

	def __str__(self):
		return "%s: %s %s --> %s"%(self.member.code, self.member.first_name, self.member.last_name, self.date.date())


class TransactionType(models.Model):
	id = models.BigAutoField(primary_key=True)
	general = models.BooleanField(default=False)
	withdraw = models.BooleanField(default=False)
	fined = models.BooleanField(default=False)
	savings_to_shares = models.BooleanField(default=False)
	paid_fines = models.BooleanField(default=False)
	share_pay = models.BooleanField(default=False)

	transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)

	def __str__(self):
		return "%s %s --> %s"%(self.transaction.member.first_name, self.transaction.member.last_name, self.transaction.date.date())


class Tulinaawe(models.Model):
	id = models.BigAutoField(primary_key=True)
	date_due = models.DateTimeField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	title = models.CharField(max_length=255)
	description = models.TextField()
	status = models.BooleanField(default=True)
	total_amount_contributed = models.IntegerField(default=0)

	@property
	def title_snippet(self):
		if len(self.title) > 15:
			return "%s..."%(self.title[0:15])
		else:
			return "%s"%(self.title)

	@property
	def description_snippet(self):
		if len(self.description) > 40:
			return "%s..."%(self.description[0:40])
		else:
			return "%s"%(self.description)

	class Meta:
		verbose_name_plural = "Tulinaawe"
		ordering = ["-date_due"]

	def __str__(self):
		return "%s"%(self.title)


class TulinaaweContributor(models.Model):
	id = models.BigAutoField(primary_key=True)
	date = models.DateTimeField(null=True)
	event = models.ForeignKey(Tulinaawe, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	amount = models.IntegerField(default=0)

	@property
	def event_status(self):
		if self.event.status:
			return "Event Open"
		else:
			return "Event closed"

	@property
	def event_name(self):
		return self.event.title

	def __str__(self):
		return "%s %s -- %s"%(self.member.first_name, self.member.last_name, self.event)


class Loan(models.Model):
	id = models.BigAutoField(primary_key=True)
	member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)

	member_name = models.CharField(max_length=255)
	amount = models.IntegerField(default=0)
	amount_in_words = models.CharField(max_length=255, blank=True)

	#Computed Data
	amount_paid = models.IntegerField(default=0)
	interest = models.IntegerField(default=0)

	date_due = models.DateTimeField()
	date_taken_out = models.DateTimeField()
	date_created = models.DateTimeField(auto_now_add=True)

	
	residential_address = models.CharField(max_length=255, blank=True)
	location_of_business = models.CharField(max_length=255, blank=True)
	savings_account_no = models.CharField(max_length=255, blank=True)


	purpose_of_loan = models.CharField(max_length=255, blank=True)
	date_when_required = models.DateField(null=True, blank=True)
	source_of_loan_repayment = models.CharField(max_length=255, blank=True)


	security_1_name = models.CharField(max_length=255, blank=True)
	security_1_location = models.CharField(max_length=255, blank=True)
	security_1_value = models.IntegerField(default=0)
	security_2_name = models.CharField(max_length=255, blank=True)
	security_2_location = models.CharField(max_length=255, blank=True)
	security_2_value = models.IntegerField(default=0)

	value_of_shares = models.IntegerField(default=0)
	value_of_savings = models.IntegerField(default=0)

	guarantor_1_name = models.CharField(max_length=255, blank=True)
	guarantor_1_membership_no = models.CharField(max_length=255, blank=True)
	guarantor_2_name = models.CharField(max_length=255, blank=True)
	guarantor_2_membership_no = models.CharField(max_length=255, blank=True)

	#Loans Committee
	committee_member_1 = models.CharField(max_length=255, blank=True)
	committee_member_1_date = models.DateTimeField(blank=True, null=True)
	committee_member_2 = models.CharField(max_length=255, blank=True)
	committee_member_2_date = models.DateTimeField(blank=True, null=True)
	committee_member_3 = models.CharField(max_length=255, blank=True)
	committee_member_3_date = models.DateTimeField(blank=True, null=True)
	
	objects = LoanFinancialYearManager()

	@property
	def balance(self):
		if self.amount_paid <= self.amount:
			return self.amount - self.amount_paid
		else:
			return 0

	@property
	def interests(self):
		if self.amount_paid > self.amount:
			return self.amount_paid - self.amount
		else:
			return 0


	def __str__(self):
		return "%s -- %s"%(self.member_name, self.amount)


class LoanPayment(models.Model):
	id = models.BigAutoField(primary_key=True)
	date = models.DateTimeField()
	amount = models.IntegerField(default=0)
	loan = models.ForeignKey(Loan, on_delete=models.CASCADE)

	def __str__(self):
		return "%s -- %s"%(self.loan, self.amount)


class Expense(models.Model):
	id = models.BigAutoField(primary_key=True)
	receipt_no = models.IntegerField(unique=True)
	_from = models.CharField(max_length=255, default="", blank=True)
	_to = models.CharField(max_length=255, default="", blank=True)
	date = models.DateTimeField()
	items_no = models.IntegerField(default=0)
	total_amount = models.IntegerField(default=0)

	objects = ExpensesFinancialYearManager()

	@property
	def get_from(self):
		return self._from

	@property
	def get_to(self):
		return self._to

	def __str__(self):
		return "%s --> %s"%(self.receipt_no, self.date.date())


class ExpenseItem(models.Model):
	id = models.BigAutoField(primary_key=True)
	expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	quantity = models.IntegerField(default=0)
	cost_price = models.IntegerField(default=0)
	total_value = models.IntegerField(default=0)

	def __str__(self):
		return "%s --> %s"%(self.expense, self.name)


class Note(models.Model):
	id = models.BigAutoField(primary_key=True)
	content = models.TextField()


class Voucher(models.Model):
	id = models.BigAutoField(primary_key=True)
	voucher_no = models.IntegerField(unique=True)
	date = models.DateTimeField()
	items_no = models.IntegerField(default=0)
	total_amount = models.IntegerField(default=0)

	requested_by = models.CharField(max_length=255, blank=True, null=True)
	authorized_by = models.CharField(max_length=255, blank=True, null=True)
	paid_by = models.CharField(max_length=255, blank=True, null=True)
	received_by = models.CharField(max_length=255, blank=True, null=True)

	objects = VoucherFinancialYearManager()

	def __str__(self):
		return "%s --> %s"%(self.voucher_no, self.date.date())
	

class VoucherItem(models.Model):
	id = models.BigAutoField(primary_key=True)
	voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField()
	quantity = models.IntegerField(default=0)
	cost_price = models.IntegerField(default=0)
	total_value = models.IntegerField(default=0)

	def __str__(self):
		return "%s --> %s"%(self.voucher, self.name)


class ProjectFee(models.Model):
	id = models.BigAutoField(primary_key=True)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	date = models.DateField()
	amount = models.IntegerField(default=0)

	objects = ProjectFeeYearManager()

	def __str__(self):
		return "%s --> %s"%(self.memeber, self.amount)