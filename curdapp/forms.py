# from django import forms
#
# class InsertingDataForm(forms.Form):
#     product_id=forms.IntegerField(label='Enter Product Id:',widget=forms.NumberInput(
#         attrs={'placeholder':'product id','class':'form-control'}
#     ))
#     product_name=forms.CharField(label='Enter Product Name:',widget=forms.TextInput(
#         attrs={'placeholder':'product name','class':'form-control'}
#     ))
#     product_cost = forms.IntegerField(label='Enter Product cost:', widget=forms.NumberInput(
#         attrs={'placeholder': 'product cost', 'class': 'form-control'}
#     ))
#     product_class = forms.CharField(label='Enter Product class:', widget=forms.TextInput(
#         attrs={'placeholder': 'High/Medium/Low', 'class': 'form-control'}
#     ))
#     no_of_products = forms.IntegerField(label='Enter No. of products:', widget=forms.NumberInput(
#         attrs={'placeholder': 'no. of products', 'class': 'form-control'}
#     ))
#     x=range(1990,2021)
#     manfacture_date = forms.DateField(label='Select Product Manfacture Date:', widget=forms.SelectDateWidget(years=x))
#     y=range(1990,2050)
#     expiry_date = forms.DateField(label='Select Expiry Date:', widget=forms.SelectDateWidget(years=y))
#     customer_name=forms.CharField(label='Enter Customer Name:',widget=forms.TextInput(
#         attrs={'placeholder':'customer name','class':'form-control'}
#     ))
#     mobile=forms.IntegerField(label='Enter Mobile Number:',widget=forms.NumberInput(
#         attrs={'placeholder':'customer mobile number','class':'form-control'}
#     ))
#     email = forms.EmailField(label='Enter Email-ID:', widget=forms.EmailInput(
#         attrs={'placeholder': 'customer email-id', 'class': 'form-control'}
#     ))
# class UpdateDataForm(forms.Form):
#     product_id = forms.IntegerField(label='Enter Product Id:', widget=forms.NumberInput(
#         attrs={'placeholder': 'product id', 'class': 'form-control'}))
#     product_cost = forms.IntegerField(label='Enter Product cost:', widget=forms.NumberInput(
#         attrs={'placeholder': 'product cost', 'class': 'form-control'}
#     ))
# class DeleteDataForm(forms.Form):
#     product_id = forms.IntegerField(label='Enter Product Id:', widget=forms.NumberInput(
#         attrs={'placeholder': 'product id', 'class': 'form-control'}))