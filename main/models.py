from django.db import models

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phoneNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)


    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text