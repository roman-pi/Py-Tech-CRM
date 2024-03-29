from django import forms
from opportunity.forms import OpportunityForm

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


class OpportunityForm(forms.ModelForm):
    probability = forms.IntegerField(max_value=100, required=False)

    def __init__(self, *args, **kwargs):
        assigned_users = kwargs.pop('assigned_to', [])
        opp_accounts = kwargs.pop('account', [])
        opp_contacts = kwargs.pop('contacts', [])
        super(OpportunityForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        self.fields['description'].widget.attrs.update({
            'rows': '8'})
        self.fields['assigned_to'].queryset = assigned_users
        self.fields['account'].queryset = opp_accounts
        self.fields['contacts'].queryset = opp_contacts
        self.fields['assigned_to'].required = False
        self.fields['contacts'].required = False
        for key, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.label

        self.fields['closed_on'].widget.attrs.update({
            'placeholder': 'Due Date'})

        self.fields['probability'].widget.attrs.update({
            'placeholder': 'Probability'})

    class Meta:
        model = Opportunity
        fields = (
            'name', 'amount', 'account', 'contacts', 'assigned_to', 'currency',
            'probability', 'closed_on', 'lead_source', 'description', 'stage',
        )
