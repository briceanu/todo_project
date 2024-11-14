from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def get_new_access_token_for_user(username):
    refresh = RefreshToken.for_user(username)
    return {'access_token':str(refresh.access_token)}