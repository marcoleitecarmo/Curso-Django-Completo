from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):  # Introdução a testes no python
    def test_the_pytest_is_ok(self):
        print('Olá Mundo!!')
        assert 1 == 1, 'Um é igual a um'

# Teste da url da home da Recipe

    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):  # Teste da url Category
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipe_recipes_url_is_correct(self):
        recipes_url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(recipes_url, '/recipes/1/')
