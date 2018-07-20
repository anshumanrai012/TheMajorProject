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

    loan_amount = forms.DecimalField(max_digits=12, decimal_places=3)
    interest_rate = forms.DecimalField(max_digits=5, decimal_places=2)
    installment = forms.DecimalField(max_digits=12, decimal_places=2)
    annual_inc = forms.DecimalField(max_digits=12, decimal_places=3)
    dti = forms.DecimalField(max_digits=12, decimal_places=3)
    delinq_2yrs = forms.DecimalField(max_digits=2, decimal_places=0)
    inq_last_6mths = forms.DecimalField(max_digits=2, decimal_places=0)
    open_acc = forms.DecimalField(max_digits=2, decimal_places=0)
    pub_rec = forms.DecimalField(max_digits=2, decimal_places=0)
    revol_bal = forms.DecimalField(max_digits=8, decimal_places=2)
    revol_util = forms.DecimalField(max_digits=12,decimal_places=3)
    total_acc = forms.DecimalField(max_digits=2, decimal_places=0)
    home_ownership = forms.ChoiceField(choices=HOME_OWNERSHIP_CHOICES)
    verification_status = forms.ChoiceField(choices=VERIFICATION_STATUS_CHOICES)
    purpose = forms.ChoiceField(choices=PURPOSE_CHOICES)
    term = forms.ChoiceField(choices=TERM_CHOICES)

