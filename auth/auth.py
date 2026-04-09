import config
from authlib.integrations.starlette_client import OAuth

# Initialise OAuth
oauth = OAuth()

oauth.register(
    name="google",
    client_id=config.GOOGLE_AUTH_CLIENT_ID,
    client_secret=config.GOOGLE_AUTH_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={
        "scope": "openid email profile"
    }
)