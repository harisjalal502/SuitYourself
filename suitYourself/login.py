#!/usr/bin/env python3

from django import forms

class EmailForm(forms.Form):
	email = forms.CharField(label='Email', max_length=30)



