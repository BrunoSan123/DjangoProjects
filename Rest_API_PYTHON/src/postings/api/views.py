from rest_framework import generics,mixins
from django.db.models import Q
from postings.models import ApiPost
from .permissions import IsOwnerOrReadOnly
from .serializer import ApiPostSerializer


class ApiPostCreate(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ApiPostSerializer


    
    def get_queryset(self):
        qs= ApiPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs=qs.filter(Q(title__icontains=query)| Q(content__icontains=query)).distinct()
        return qs
    
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def get_serializer_context(self,*args,**kwargs):
        return {"request":self.request}
    



class ApiPostView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    serializer_class =ApiPostSerializer
    permission_classes =[IsOwnerOrReadOnly]
    #queryset = ApiPost.objects.all()


    def get_queryset(self):
        return ApiPost.objects.all()
    
    def get_serializer_context(self,*args,**kwargs):
        return {"request":self.request}

    #def get_object(self):
        #pk =self.kwargs.get("pk")
        #return ApiPost.objects.get(pk=pk)  