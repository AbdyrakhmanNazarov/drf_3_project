from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, OTPVerification
from .serializers import RegisterSerializer, OTPVerifySerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        OTPVerification.objects.create(user=user)
        return Response({"msg": "Пользователь создан, OTP отправлен"}, status=201)

class OTPLoginView(GenericAPIView):
    serializer_class = OTPVerifySerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            otp = OTPVerification.objects.filter(user=user, is_used=False).latest('created_at')
        except (User.DoesNotExist, OTPVerification.DoesNotExist):
            return Response({"error": "Неверный код или email"}, status=400)

        if otp.is_expired():
            return Response({"error": "OTP истёк"}, status=400)

        if otp.code != serializer.validated_data['code']:
            return Response({"error": "Неверный код"}, status=400)

        otp.is_used = True
        otp.save()

        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)})
