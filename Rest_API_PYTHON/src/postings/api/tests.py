from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status 
from postings.models import ApiPost
from rest_framework_jwt.settings import api_settings

jwt_payload =  api_settings.JWT_PAYLOAD_HANDLER
jwt_encoder =api_settings.JWT_ENCODE_HANDLER




User =get_user_model()

class ApiPostTestCase(APITestCase):
    def setUp(self):
        user_obj =User(username='testPodemos', email='test@tst.com')
        user_obj.set_password("rendompass")
        user_obj.save()
        site_posts =ApiPost.objects.create(user=user_obj,title='Novo Titulo',content='algo_randomico')
        

    def test_um_usuario(self):
        user_count =User.objects.count()
        self.assertEqual(user_count,1)

    def test_um_post(self):
        post_count =ApiPost.objects.count()
        self.assertEqual(post_count,1)

    def test_get_list(self):
        data={}
        url=api_reverse("api-postings:post-create")
        response =self.client.get(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print(response.data)

    def test_post_item(self):
        data={"title":"also some coll","content":"more-content"}
        url=api_reverse("api-postings:post-create")
        response =self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_get_item(self):
        site_posts =ApiPost.objects.first()
        data={}
        url=site_posts.get_api_url()
        response =self.client.get(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    def test_update_item(self):
        site_posts =ApiPost.objects.first()
        url=site_posts.get_api_url()
        data={"title":"also some coll","content":"more-content"}
        response =self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response =self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_update_item_user(self):
        site_posts =ApiPost.objects.first()
        url=site_posts.get_api_url()
        data={"title":"also some coll","content":"more-content"}
        user_obj =User.objects.first()
        payload =jwt_payload(user_obj)
        token =jwt_encoder(payload)
        self.client.credentials(HTTP_ATHORIZATION='JWT'+token)

        
        response =self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        
    
    def test_post_item_user(self):
        user_obj =User.objects.first()
        payload =jwt_payload(user_obj)
        token =jwt_encoder(payload)
        self.client.credentials(HTTP_ATHORIZATION='JWT'+token)
        data={"title":"also some coll","content":"more-content"}
        url=api_reverse("api-postings:post-create")
        response =self.client.post(url,data,format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_use_ownership(self):
        owner =User.objects.create(username='teste123454')
        site_posts =ApiPost.objects.create(user=owner,title='Novo Titulo',content='algo_randomico')
       
        user_obj =User.objects.first()
        self.assertNotEqual(user_obj.username,owner.username)
        payload =jwt_payload(user_obj)
        token =jwt_encoder(payload)
        self.client.credentials(HTTP_ATHORIZATION='JWT'+token)
       
        url=site_posts.get_api_url()
        data={"title":"also some coll","content":"more-content"}
        response =self.client.put(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        #print(response.data)