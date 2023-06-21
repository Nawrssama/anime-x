from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import kimitsu
# Create your tests here.

class KimitsuTest(TestCase):

    def setUp(self):
        self.otaku_name = get_user_model().objects.create(username="tester",password="tester")
        self.Game = kimitsu.objects.create(char_name="tester", otaku_name=self.otaku_name, char_discription='abs')

    def test_home_page_status(self):
        url = reverse('kimitsu_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_page_response(self):
        url = reverse('kimitsu_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'k/kimitsu-list.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_home_page_context(self):
        url = reverse('kimitsu_list')
        response = self.client.get(url)
        Anime_list = response.context['Anime']
        self.assertEqual(len(Anime_list), 1)
        self.assertEqual(Anime_list[0].char_name, "tester")
        self.assertEqual(Anime_list[0].otaku_name.username, "tester")
        self.assertEqual(Anime_list[0].char_discription, "abs")
        

    def test_detail_page_status_code(self):
        url = reverse('kimitsu_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('kimitsu_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'k/kimitsu-detail.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_detail_page_context(self):
        url = reverse('kimitsu_detail',args=(1,))
        response = self.client.get(url)
        game_detail = response.context['kimitsu']
        self.assertEqual(game_detail.char_name, "tester")
        self.assertEqual(game_detail.otaku_name.username, "tester")
        self.assertEqual(game_detail.char_discription, "abs")
        

    
    def test_create_view(self):
        obj={
            'char_name':"test2",
            'otaku_name':self.otaku_name.id,
            'char_discription' :"abs"
        }

        url = reverse('kimitsu_create')
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertEqual(len(kimitsu.objects.all()),2)
        # self.assertRedirects(response, reverse('kimitsu_list'))

    def test_update_view(self):
        obj={
            'char_name':"test2",
            'otaku_name':self.otaku_name.id,
            'char_discription' :"abs"
        }

        url = reverse('kimitsu_update', args=(1,))
        response = self.client.post(path=url,data=obj,follow=True)
        # self.assertEqual(len(Game.objects.all()),2)
        self.assertRedirects(response, reverse('kimitsu_list'))

    
    def test_delete_view(self):
       

        url = reverse('kimitsu_delete', args=(1,))
        response = self.client.post(path=url,follow=True)
        # self.assertEqual(len(Game.objects.all()),0)
        self.assertRedirects(response, reverse('kimitsu_list'))


    def test_str_method(self):
        self.assertEqual(str(self.Game),"tester")


    def test_create_response(self):
        url = reverse('kimitsu_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'k/kimitsu-create.html')
        self.assertTemplateUsed(response, '_base.html')


    def test_update_response(self):
        url = reverse('kimitsu_update', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response,'k/kimitsu-update.html')
        self.assertTemplateUsed(response, '_base.html')


    def test_delete_response(self):
        url = reverse('kimitsu_delete', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response,'k/kimitsu-delete.html')
        self.assertTemplateUsed(response, '_base.html')