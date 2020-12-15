from django.db import models

class Upload(models.Model):
	uploadfile = models.FileField(upload_to='images/%Y/%m/%d')
	title = models.CharField(max_length=100, default='No title')
	description = models.CharField(max_length=300, default='No description')
	SIZES = (
		('S', 'Small'),
		('M', 'Medium'),
		('L', 'Large'),
		('XL', 'Extra large'),
	)
	size = models.CharField(max_length=2, choices=SIZES, default='NA')
	price = models.CharField(max_length=6, default='0.00')
