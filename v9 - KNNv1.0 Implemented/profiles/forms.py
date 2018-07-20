from django import forms


HOME_OWNERSHIP_CHOICES = (
    ('MORTGAGE','Mortgage'),
    ('NONE','None'),
    ('OTHER','Other'),
    ('OWN','Own'),
    ('RENT','Rent')
)

VERIFICATION_STATUS_CHOICES = (
    ('NOT_VERIFIED','Not Verified'),
    ('SOURCE_VERIFIED','Source Verified'),
    ('VERIFIED','Verified')
)

PURPOSE_CHOICES = (
    ('CAR','Car'),
    ('CREDIT_CARD','Credit Card'),
    ('DEBT_CONSOLIDATION','Debt Consolidation'),
    ('EDUCATIONAL','Educational'),
    ('HOME_IMPROVEMENT','Home Improvement'),
    ('HOUSE','House'),
    ('MAJOR_PURCHAGE','Major Purchase'),
    ('MEDICAL', 'Medical'),
    ('MOVING','Moving'),
    ('OTHER','Other'),
    ('RENEWABLE_ENERGY','Renewable Energy'),
    ('SMALL_BUSINESS','Small Business'),
    ('VACATION','Vacation'),
    ('WEDDING','Wedding')

)

TERM_CHOICES = (
    ('36', '36 Months'),
    ('60', '60 Months')
)



class PredictForm(forms.Form):
    loan_amount = forms.CharField(max_length=50)
    interest_rate = forms.CharField(max_length=50)
    installment = forms.CharField(max_length=100)
    annual_inc = forms.CharField(max_length=50)
    dti = forms.CharField(max_length=50)
    delinq_2yrs = forms.CharField(max_length=50)
    inq_last_6mths = forms.CharField(max_length=50)
    open_acc = forms.CharField(max_length=50)
    pub_rec = forms.CharField(max_length=50)
    revol_bal = forms.CharField(max_length=50)
    revol_util = forms.CharField(max_length=50)
    total_acc = forms.CharField(max_length=50)

    home_ownership = forms.ChoiceField(choices=HOME_OWNERSHIP_CHOICES)


    verification_status = forms.ChoiceField(choices=VERIFICATION_STATUS_CHOICES)
    purpose = forms.ChoiceField(choices=PURPOSE_CHOICES)
    term = forms.ChoiceField(choices=TERM_CHOICES)

