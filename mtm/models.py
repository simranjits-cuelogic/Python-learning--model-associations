from __future__ import unicode_literals

from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=15)
    # articles = models.ManyToManyField(Article)

    class Meta:
        ordering = ('title', )

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ('headline', )

    def __str__(self):
        return self.headline

"""
Note:
Article.objects.first().publications.all()

Article.objects.first().publications.add(obj_article)
Article.objects.first().publications.create(article_attrs)

Article.objects.first().publications.clear() #remove all
Article.objects.first().publications.all().first().remove()
Article.objects.first().delete()

Article.objects.filter(publications__title__startswith="Query Str")

----from other side of mtm
Publication.objects.first().article_set.all()

Publication.objects.first().article_set.add(obj_article)
Publication.objects.first().article_set.create(article_attrs)

Publication.objects.first().article_set.clear() #remove all
Publication.objects.first().article_set.all().first().remove()
Publication.objects.first().delete()

Publication.objects.filter(article__headline__startswith="Query Str")

"""
