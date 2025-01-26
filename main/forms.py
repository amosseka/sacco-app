from client_side_image_cropping import ClientsideCroppingWidget
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from . import models


class CustomAuthForm(AuthenticationForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({"placeholder": "Enter Username"})
		self.fields['password'].widget.attrs.update({"placeholder": "Enter password"})


class NomineesForDespositForm(forms.ModelForm):
	class Meta:
		models = models.NomineesForDeposits
		fields = '__all__'


class MemberCreate(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		#Placeholders for the new member form
		self.fields['code'].widget.attrs.update({"placeholder": "Member Code"})
		self.fields['first_name'].widget.attrs.update({"placeholder": "First Name"})
		self.fields['last_name'].widget.attrs.update({"placeholder": "Last Name"})
		self.fields['contact'].widget.attrs.update({"placeholder": "Phone Contact"})
		self.fields['email_address'].widget.attrs.update({"placeholder": "example@gmail.com"})
		self.fields['identification_no'].widget.attrs.update({"placeholder": "National ID Number (NIN)"})

		self.fields['residence'].widget.attrs.update({"placeholder": "Residence"})
		self.fields['town'].widget.attrs.update({"placeholder": "Town"})
		self.fields['town_code'].widget.attrs.update({"placeholder": "Code"})
		self.fields['box_no'].widget.attrs.update({"placeholder": "Box No."})

		self.fields['employer'].widget.attrs.update({"placeholder": "Employer"})
		self.fields['employment_address'].widget.attrs.update({"placeholder": "Employment Address"})
		self.fields['position_in_employment'].widget.attrs.update({"placeholder": "Position In Employment"})
		self.fields['staff_number'].widget.attrs.update({"placeholder": "Staff Number"})

		self.fields['proposed_monthly_contribution'].widget.attrs.update({"placeholder": "Proposed Monthly Contribution"})
		self.fields['amount_in_words'].widget.attrs.update({"placeholder": "Amount in words"})

		self.fields['business_name'].widget.attrs.update({"placeholder": "Business Name"})
		self.fields['business_address'].widget.attrs.update({"placeholder": "Business Address"})
		self.fields['business_sector_others'].widget.attrs.update({"placeholder": "Other Business Sector (Specify)"})
		self.fields['business_location'].widget.attrs.update({"placeholder": "Business Location"})

		self.fields['data_captured_by'].widget.attrs.update({"placeholder": "Data captured By"})
		self.fields['system_approval_by'].widget.attrs.update({"placeholder": "System Approval By"})
		self.fields['membership_approved_by'].widget.attrs.update({"placeholder": "Membership Approved By"})
		self.fields['admitted_by_1'].widget.attrs.update({"placeholder": "Admitted By"})
		self.fields['admitted_by_2'].widget.attrs.update({"placeholder": "Admitted By"})


	class Meta:
		model = models.Member
		fields = '__all__'
		exclude = ['shares', 'welfare', 'savings', 'withdraw', 'other', 'fines', 'full_names', 'project_fee']

		widgets = {
			'image': ClientsideCroppingWidget(
				width=400,
				height=400,
				preview_width=200,
				preview_height=200,
				format='jpeg',
				quality=100
			),
			'marital_status': forms.RadioSelect,
			'gender': forms.RadioSelect,
			'source_of_income': forms.RadioSelect,
			'mode_of_remittance': forms.RadioSelect,
			'business_sector': forms.RadioSelect,
		}


class Transaction(forms.ModelForm):

	class Meta:
		model = models.Transaction
		fields = ['date', 'shares', 'welfare', 'savings', 'withdraw', 'fines', 'fine_type', 'other', 'notes']


class TransactionForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['notes'].widget.attrs.update({"placeholder": "Write something about the transaction"})

	class Meta:
		model = models.Transaction
		fields = ['member', 'date', 'shares', 'savings', 'withdraw', 'welfare', 'fines', 'project_fee', 'fine_type', 'other', 'notes']


class TransactionDetail(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['member'].widget.attrs.update({"disabled": "True"})
		self.fields['date'].widget.attrs.update({"disabled": "True"})
		self.fields['shares'].widget.attrs.update({"disabled": "True"})
		self.fields['savings'].widget.attrs.update({"disabled": "True"})
		self.fields['welfare'].widget.attrs.update({"disabled": "True"})
		self.fields['withdraw'].widget.attrs.update({"disabled": "True"})
		self.fields['fines'].widget.attrs.update({"disabled": "True"})
		self.fields['other'].widget.attrs.update({"disabled": "True"})
		self.fields['notes'].widget.attrs.update({"disabled": "True"})

	class Meta:
		model = models.Transaction
		fields = ['member', 'date', 'shares', 'savings', 'withdraw', 'welfare', 'fines', 'fine_type', 'other', 'notes']

	
class EventForm(forms.ModelForm):

	class Meta:
		model = models.Tulinaawe
		fields = ['date_due', 'title', 'description']


class ContributorForm(forms.ModelForm):

	class Meta:
		model = models.TulinaaweContributor
		fields = ['member', 'date', 'amount']


class LoanForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['member_name'].widget.attrs.update({"placeholder": "Applicant Name"})
		self.fields['location_of_business'].widget.attrs.update({"placeholder": "Location of Business"})
		self.fields['residential_address'].widget.attrs.update({"placeholder": "Residential Address"})

		self.fields['amount'].widget.attrs.update({"placeholder": "Amount Applied for"})
		self.fields['amount_in_words'].widget.attrs.update({"placeholder": "Amount in Words"})

		self.fields['purpose_of_loan'].widget.attrs.update({"placeholder": "Purpose of Loan"})
		self.fields['source_of_loan_repayment'].widget.attrs.update({"placeholder": "Source of Loan Repayment"})
		
		self.fields['security_1_name'].widget.attrs.update({"placeholder": "Security 1"})
		self.fields['security_2_name'].widget.attrs.update({"placeholder": "Security 2"})

		self.fields['security_1_location'].widget.attrs.update({"placeholder": "Location / Department"})
		self.fields['security_2_location'].widget.attrs.update({"placeholder": "Location / Department"})

		self.fields['security_1_value'].widget.attrs.update({"placeholder": "Approximate Value"})
		self.fields['security_2_value'].widget.attrs.update({"placeholder": "Approximate Value"})

		self.fields['guarantor_1_name'].widget.attrs.update({"placeholder": "Guarantor Name"})
		self.fields['guarantor_2_name'].widget.attrs.update({"placeholder": "Guarantor Name"})

		self.fields['guarantor_1_membership_no'].widget.attrs.update({"placeholder": "Membership No."})
		self.fields['guarantor_2_membership_no'].widget.attrs.update({"placeholder": "Membership No."})

		self.fields['committee_member_1'].widget.attrs.update({"placeholder": "Name"})
		self.fields['committee_member_2'].widget.attrs.update({"placeholder": "Name"})
		self.fields['committee_member_3'].widget.attrs.update({"placeholder": "Name"})
	
	class Meta:
		model = models.Loan
		fields = '__all__'

		exclude = ['amount_paid', 'interest']


class LoanPaymentForm(forms.ModelForm):

	class Meta:
		model = models.LoanPayment
		fields = ['date', 'amount']


class ExpensesForm(forms.ModelForm):

	class Meta:
		model = models.Expense
		fields = ['receipt_no', 'date', '_from', '_to']


class ExpenseItem(forms.ModelForm):

	class Meta:
		model = models.ExpenseItem
		fields = ['name', 'quantity', 'cost_price', 'total_value']


class VoucherForm(forms.ModelForm):

	class Meta:
		model = models.Voucher
		fields = ['voucher_no', 'date', 'requested_by', 'authorized_by', 'received_by', 'paid_by']


class VoucherItem(forms.ModelForm):

	class Meta:
		model = models.VoucherItem
		fields = ['name', 'quantity', 'cost_price', 'total_value', 'description']


class ProjectFeeForm(forms.ModelForm):

	class Meta:
		model = models.ProjectFee
		fields = '__all__'


class NotesForm(forms.ModelForm):

	class Meta:
		model = models.Note
		fields = '__all__'


class FinancialYearForm(forms.ModelForm):
	
	class Meta:
		model = models.FinancialYear
		fields = ['first_date', 'second_date']