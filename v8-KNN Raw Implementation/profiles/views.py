import os
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from .models import Personal, Credit
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PredictForm
from django.conf import settings




# Create your views here.


class CreditListView(LoginRequiredMixin,ListView):
    model = models.Credit
    template_name = 'credit_list.html'
    login_url = 'login'

    def get_queryset(self):
        return Credit.objects.filter(author=self.request.user)


class CreditDetailView(LoginRequiredMixin,DetailView):
    model = models.Credit
    template_name = 'credit_detail.html'
    login_url = 'login'


class CreditUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Credit
    fields = ['title','loan_amount','interest_rate','installment','annual_inc',
              'dti','delinq_2yrs','inq_last_6mths','open_acc','pub_rec','revol_bal',
              'revol_util','total_acc','home_ownership','verification_status','purpose',
              'term']
    template_name = 'credit_edit.html'
    login_url = 'login'


class CreditDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Credit
    template_name = 'credit_delete.html'
    success_url = reverse_lazy('credit_list')
    login_url = 'login'


class CreditCreateView(LoginRequiredMixin,CreateView):
    model = models.Credit
    template_name = 'credit_new.html'
    fields = ['title','loan_amount','interest_rate','installment',
              'annual_inc','dti','delinq_2yrs','inq_last_6mths',
              'open_acc','pub_rec','revol_bal','revol_util',
              'total_acc','home_ownership','verification_status',
              'purpose','term']

    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PersonalListView(LoginRequiredMixin,ListView):
    model = models.Personal
    template_name = 'personal_list.html'
    login_url = 'login'

    def get_queryset(self):
        return Personal.objects.filter(author=self.request.user)


class PersonalDetailView(LoginRequiredMixin,DetailView):
    model = models.Personal
    template_name = 'personal_detail.html'
    login_url = 'login'


class PersonalUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Personal
    fields = ['first_name','last_name','email','gender','birthdate','hometown']
    template_name = 'personal_edit.html'
    login_url = 'login'


class PersonalCreateView(LoginRequiredMixin,CreateView):
    model = models.Personal
    template_name = 'personal_new.html'
    fields = ['email','gender','birthdate','hometown']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class Prediction(LoginRequiredMixin,DetailView):
    models = models.Credit
    template_name = 'result.html'
    login_url = 'login'


def prediction(request):
    submitbutton = request.POST.get("submit")
    loan_amount = ''
    interest_rate = ''
    installment = ''
    annual_inc = ''
    dti = ''
    delinq_2yrs = ''
    inq_last_6mths = ''
    open_acc = ''
    pub_rec = ''
    revol_bal = ''
    revol_util = ''
    total_acc = ''
    home_ownership = ''
    verification_status = ''
    purpose = ''
    term = ''
    prediction = ''
    result = 0

    form = PredictForm(request.POST or None)
    if form.is_valid():
        loan_amount = float(form.cleaned_data.get("loan_amount"))
        interest_rate = float(form.cleaned_data.get("interest_rate"))
        installment = float(form.cleaned_data.get("installment"))
        annual_inc = float(form.cleaned_data.get("annual_inc"))
        dti = float(form.cleaned_data.get("dti"))
        delinq_2yrs = float(form.cleaned_data.get("delinq_2yrs"))
        inq_last_6mths = float(form.cleaned_data.get("inq_last_6mths"))
        open_acc = float(form.cleaned_data.get("open_acc"))
        pub_rec = float(form.cleaned_data.get("pub_rec"))
        revol_bal = float(form.cleaned_data.get("revol_bal"))
        revol_util = float(form.cleaned_data.get("revol_util"))
        total_acc = float(form.cleaned_data.get("total_acc"))
        home_ownership = form.cleaned_data.get("home_ownership")
        verification_status = form.cleaned_data.get("verification_status")
        purpose = form.cleaned_data.get("purpose")
        term = form.cleaned_data.get("term")
        result = loan_amount + interest_rate


        #Knn scipt starts here

        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        from IPython.display import display  # Allows the use of display() for DataFrames
        plt.style.use('fivethirtyeight')


        file = open(os.path.join(settings.STATIC_ROOT, 'dataset\clean_loan_data.csv'),encoding="utf8")
        '''
        loan_data = pd.read_csv(file, low_memory=False, skiprows=1)

        
        try:
            loan_data = pd.read_csv("F:\College\ML Project\KNN\Dataset\LoanStats3a.csv", low_memory=False, skiprows=1)
        # print("The loan dataset has {} samples with {} features.".format(*loan_data.shape))
        except:
            print("The loan dataset could not be loaded. The dataset is missing")

        init_ld = loan_data.head()
        desc_init_row = loan_data.iloc[0]

        loan_data = loan_data.drop(['desc', 'url'], axis=1)
        desc_init_ld = loan_data.describe()

        # Count half point of the dataset.
        half_point = len(loan_data) / 2
        loan_data = loan_data.dropna(thresh=half_point, axis=1)

        # We save it in the new file
        loan_data.to_csv('loan_data.csv', index=False, encoding="utf-8")

        # Import the newly saved file
        loan_data = pd.read_csv('loan_data.csv', low_memory=False)
        loan_data.drop_duplicates()
        desc_unique_ld = loan_data.iloc[0]

        # Analysis
        # Feature meaning and Usefulness

        first_entry = loan_data.iloc[0]
        first_entry.to_csv('first_entry.csv', index=True, encoding="utf-8")

        description = pd.read_csv('F:\College\ML Project\KNN\Dataset\LCDataDictionary.csv', low_memory=False)

        import csv
        list_first_entry = open('first_entry.csv', 'r')
        first_csvreader = csv.reader(list_first_entry)
        first_list = list(first_csvreader)

        list_data_dictio = open('F:\College\ML Project\KNN\Dataset\LCDataDictionary.csv', 'r')
        second_csvreader = csv.reader(list_data_dictio)
        second_list = list(second_csvreader)

        table = []
        for row in first_list:
            table.append(row[0])

        new_table = []
        for col in second_list:
            if col[0] in table:
                new_table.append(col)

        df_table = pd.DataFrame(new_table, columns=['Variable', 'Description'])
        df_table = df_table.set_index(['Variable', 'Description'])

        first_13 = ['id', 'member_id', 'loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'term',
                    'int_rate', 'installment', 'grade', 'sub_grade', 'emp_title', 'emp_length', 'home_ownership']

        # We drop the columns(features) that are not useful.
        loan_data = loan_data.drop(['id', 'member_id', 'funded_amnt', 'funded_amnt_inv',
                                    'grade', 'sub_grade', 'emp_title'], axis=1)

        second_13 = ['annual_inc', 'verification_status', 'issue_d', 'loan_status', 'pymnt_plan', 'purpose',
                     'title', 'zip_code', 'addr_state', 'dti', 'delinq_2yrs', 'earliest_cr_line', 'inq_last_6mths']

        loan_data = loan_data.drop(['issue_d', 'zip_code'], axis=1)

        third_13 = ['open_acc', 'pub_rec', 'revol_bal', 'revol_util', 'total_acc', 'initial_list_status', 'out_prncp',
                    'out_prncp_inv', 'total_pymnt', 'total_pymnt_inv', 'total_rec_prncp', 'total_rec_int',
                    'total_rec_late_fee']
        loan_data = loan_data.drop(['out_prncp', 'out_prncp_inv', 'total_pymnt', 'total_pymnt_inv',
                                    'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee'], axis=1)

        fourth_13 = ['recoveries', 'collection_recovery_fee', 'last_pymnt_d', 'last_pymnt_amnt', 'last_credit_pull_d',
                     'collections_12_mths_ex_med', 'policy_code', 'application_type', 'acc_now_delinq',
                     'chargeoff_within_12_mths',
                     'delinq_amnt', 'pub_rec_bankruptcies', 'tax_liens']

        loan_data = loan_data.drop(['recoveries', 'collection_recovery_fee',
                                    'last_pymnt_d', 'last_pymnt_amnt'], axis=1)

        loan_st_count = loan_data['loan_status'].value_counts()
        loan_data['loan_status'].value_counts().plot(kind='barh', color='orange', title='Possible Loan Status',
                                                     alpha=0.75)
        plt.show()

        loan_data = loan_data[(loan_data['loan_status'] == "Fully Paid") | (loan_data['loan_status'] == "Charged Off")]

        loan_data['loan_status'].value_counts().plot(kind='barh', color='blue', title='Simplified Possible Loan Status',
                                                     alpha=0.55)
        plt.show()

        # We need to change the object value to numerical for the algorithm processing
        # So we will use Dictonary
        status_replace = {
            "loan_status": {
                "Fully Paid": 1,
                "Charged Off": 0,
            }
        }
        loan_data = loan_data.replace(status_replace)
        binary_satus = loan_data['loan_status'].value_counts()

        # Final Data Cleaning¶

        orig_columns = loan_data.columns
        drop_columns = []
        for col in orig_columns:
            col_series = loan_data[col].dropna().unique()
            if len(col_series) == 1:
                drop_columns.append(col)
        loan_data = loan_data.drop(drop_columns, axis=1)
        drop_columns

        # Methodology

        null_counts = loan_data.isnull().sum()
        loan_data = loan_data.drop("pub_rec_bankruptcies", axis=1)
        loan_data = loan_data.dropna(axis=0)

        # Handling Non-Numeric Data Types

        print(loan_data.dtypes.value_counts())

        # We have 11 objects that need to handled
        object_columns_df = loan_data.select_dtypes(include=["object"])
        # print (object_columns_df.iloc[0])
        columns = ['term', 'emp_length', 'home_ownership', 'verification_status', 'addr_state']
        for col in columns:
            print(loan_data[col].value_counts())
            print(" ")

        print(loan_data["purpose"].value_counts())
        print(" ")
        print(loan_data["title"].value_counts())

        mapping_dict = {
            "emp_length": {
                "10+ years": 10,
                "9 years": 9,
                "8 years": 8,
                "7 years": 7,
                "6 years": 6,
                "5 years": 5,
                "4 years": 4,
                "3 years": 3,
                "2 years": 2,
                "1 year": 1,
                "< 1 year": 0,
                "n/a": 0
            }
        }
        loan_data = loan_data.drop(["last_credit_pull_d", "earliest_cr_line", "addr_state", "title"], axis=1)
        loan_data["int_rate"] = loan_data["int_rate"].str.rstrip("%").astype("float")
        loan_data["revol_util"] = loan_data["revol_util"].str.rstrip("%").astype("float")
        loan_data = loan_data.replace(mapping_dict)

        categorical_columns = ["home_ownership", "verification_status", "emp_length", "purpose", "term"]
        dummy_df = pd.get_dummies(loan_data[categorical_columns])
        loan_data = pd.concat([loan_data, dummy_df], axis=1)
        loan_data = loan_data.drop(categorical_columns, axis=1)

        # cleaned and filtered data to csv
        loan_data.to_csv('clean_loan_data.csv', index=False)
        '''

        # Model Training
        # KNN
        from sklearn import preprocessing, cross_validation, neighbors

        df = pd.read_csv(file)

        X = np.array(df.drop(['loan_status'], 1))
        y = np.array(df['loan_status'])

        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25)

        clf = neighbors.KNeighborsClassifier()
        clf.fit(X_train, y_train)

        accuracy = clf.score(X_test, y_test)
        print(accuracy)

        examples = np.array([[5000, 10.65, 162.87, 24000, 27.65, 0, 1, 3, 0, 13648, 83.7, 9, 0, 0, 0, 0, 0, 1, 0, 0, 1,
                              0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])
        examples = examples.reshape(len(examples), -1)
        prediction = clf.predict(examples)
        print(prediction)
        


    context = {'form': form, 'loan_amount': loan_amount, 'interest_rate': interest_rate,
               'submitbutton': submitbutton, 'installment': installment,
               'annual_inc': annual_inc,'dti':dti,'delinq_2yrs': delinq_2yrs,
               'inq_last_6mths': inq_last_6mths, 'open_acc': open_acc, 'pub_rec':pub_rec,
               'revol_bal': revol_bal,'revol_util': revol_util, 'total_acc': total_acc,
               'home_ownership': home_ownership, 'verification_status': verification_status,
               'purpose': purpose, 'term': term, 'result': result, 'prediction': prediction
               }

    return render(request, 'predict.html', context)


