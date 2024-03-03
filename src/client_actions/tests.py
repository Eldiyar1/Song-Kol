# from django.urls import reverse
# from rest_framework.test import APITestCase
#
# from .models import CommentName, CommentView
#
#
# class CommentNameViewSetTest(APITestCase):
#     def setUp(self):
#         self.comment_name = CommentName.objects.create(name='John Doe')
#
#     def test_list_comment_names(self):
#         url = reverse('commentname-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['name'], self.comment_name.name)
#
#     def test_create_comment_name(self):
#         url = reverse('commentname-list')
#         data = {'name': 'Jane Doe'}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(CommentName.objects.count(), 2)
#         self.assertEqual(CommentName.objects.get(pk=response.data['id']).name, 'Jane Doe')
#
#
# class CommentViewViewSetTest(APITestCase):
#     def setUp(self):
#         self.comment_view = CommentView.objects.create(text='Test comment', stars=10)
#
#     def test_list_comment_views_unauthorized(self):
#         url = reverse('commentview-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 401)
#
#     def test_list_comment_views_authorized(self):
#         url = reverse('commentview-list')
#         self.client.login(username='admin', password='admin')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['text'], self.comment_view.text)
#
#     def test_create_comment_view_unauthorized(self):
#         url = reverse('commentview-list')
#         data = {'text': 'New comment', 'stars': 4}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 401)
#         self.assertEqual(CommentView.objects.count(), 1)
#
#     def test_create_comment_view_authorized(self):
#         url = reverse('commentview-list')
#         data = {'text': 'New comment', 'stars': 4}
#         self.client.login(username='admin', password='admin')
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(CommentView.objects.count(), 2)
#         self.assertEqual(CommentView.objects.get(pk=response.data['id']).text, 'New comment')
