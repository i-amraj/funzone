import os
import sys
from pydrive2.auth import GoogleAuth

gauth = GoogleAuth()
gauth.settings['get_refresh_token'] = True
gauth.settings['oauth_scope'] = ['https://www.googleapis.com/auth/drive.file']

auth_url = gauth.GetAuthUrl()

print("=" * 80)
print("🔒 GOOGLE DRIVE OAUTH AUTHENTICATION LINK:")
print("=" * 80)
print(auth_url)
print("=" * 80)
