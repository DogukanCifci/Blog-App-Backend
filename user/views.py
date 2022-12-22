
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Kullanıcı Çıkış (Token Sil)
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({"message": 'User Logout: Token Deleted'})


#####-------------------------------------------------------------
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser # Djangonun kullanici admin mi diye sorguladigi kendi methodu
from rest_framework.viewsets import ModelViewSet

class UserView(ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser] # Permission icin djangonun kendi hazir kütüphanesini kullandik. Bu komut sayesinde sadece admin kisi userlari görebilir. Giris yapmis normal kullanici göremez
