# from django import forms
# from django.contrib.postgres.fields import ArrayField
# from django.core.exceptions import ValidationError
    
# class SetupGameForm(forms.Form):

#     # TODO: Leaving as this can be used as a form later
#     # players
#     player0 = forms.CharField(max_length=200)

#     # rules
#     ace_rule = forms.CharField()

#     def clean_names_and_rules(self):
#         data = self.cleaned_data['player0']

#         # Check these fields as 1?
#         if data == '':
#             raise ValidationError(('All rules and at least 2 players must be supplied'))

#         # Remember to always return the cleaned data.
#         return data