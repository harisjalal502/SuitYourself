from django import forms

class UploadForm(forms.Form):
	uploadfile = forms.FileField(
		label = 'Choose a photo',
	)
	title = forms.CharField()
	description = forms.CharField(widget = forms.Textarea)
	SIZES = (
		('S', 'Small'),
		('M', 'Medium'),
		('L', 'Large'),
		('XL', 'Extra large'),
	)
	size = forms.ChoiceField(choices=SIZES)
	price = forms.CharField(widget = forms.NumberInput)


