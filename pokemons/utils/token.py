from rest_framework_simplejwt.tokens import RefreshToken


def obter_tokens_para_treinador(user):
    refresh =RefreshToken.for_user(user)

    return{
        'refresh':str(refresh),
        'access': str(refresh.access_token)
    }