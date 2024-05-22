# для перевода модели надо указать нашему приложению, как именно и что именно надо переводить

from .models import Category, Post

# импортируем декоратор для перевода и класс настроек, от которого будем наследоваться
from modeltranslation.translator import register, TranslationOptions

# регистрируем наши модели для перевода
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # указываем, какие именно поля надо переводить в виде кортежа


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)# указываем, какие именно поля надо переводить в виде кортежа

