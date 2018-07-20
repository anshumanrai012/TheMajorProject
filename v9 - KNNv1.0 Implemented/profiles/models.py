from django.conf import settings
from django.db import models
from django.urls import reverse


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


GENDER_CHOICE = (
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other')
)


class Credit(models.Model):
    title = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    loan_amount = models.FloatField(null=True,blank=True,
                                    help_text='The listed amount of the loan applied for by the borrower.')
    interest_rate = models.FloatField(null=True, blank=True,
                                      help_text='Interest Rate on the loan')
    installment = models.FloatField(null=True, blank=True,
                                    help_text='The monthly payment owed by the borrower if the loan originates.')
    annual_inc = models.FloatField(null=True, blank=True,
                                   help_text='The self-reported annual income provided by the borrower during registration.')
    dti = models.FloatField(null=True, blank=True,
                            help_text='A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations,'
                                      ' excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income.')
    delinq_2yrs = models.IntegerField(null=True, blank=True,
                                      help_text="The number of 30+ days past-due incidences of delinquency in "
                                                "the borrower's credit file for the past 2 years")
    inq_last_6mths = models.IntegerField(null=True, blank=True,
                                         help_text='The number of inquiries in past 6 months (excluding auto and mortgage inquiries)')
    open_acc = models.IntegerField(null=True, blank=True,
                                   help_text="he number of open credit lines in the borrower's credit file.")
    pub_rec = models.IntegerField(null=True, blank=True,
                                  help_text='Number of derogatory public records')
    revol_bal = models.IntegerField(null=True, blank=True,
                                    help_text='Total credit revolving balance')
    revol_util = models.FloatField(null=True, blank=True,
                                   help_text='Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.')
    total_acc = models.IntegerField(null=True, blank=True,
                                    help_text="The total number of credit lines currently in the borrower's credit file")
    home_ownership = models.CharField(choices=HOME_OWNERSHIP_CHOICES, null=True, blank=True, max_length=50)
    verification_status = models.CharField(choices= VERIFICATION_STATUS_CHOICES, null=True, blank=True, max_length=50)
    purpose = models.CharField(choices=PURPOSE_CHOICES, null=True, blank=True, max_length=50)
    term = models.CharField(choices=TERM_CHOICES, null=True, blank=True, max_length=50)




    def get_absolute_url(self):
        return reverse('credit_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Personal(models.Model):
    first_name = models.CharField(max_length= 50,null=True, blank=True)
    last_name = models.CharField(max_length=50,null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, null=True, blank=True, max_length=50)
    birthdate = models.DateField(blank=True, null=True)
    hometown = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('personal_detail',args=[str(self.id)])

    def __str__(self):
        return self.email
