from django import forms 


class searchForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=50, required=True, label="Image Name")
    safe_search = forms.BooleanField(required=False, initial=False, label= "safe search")
