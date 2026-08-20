import os
import sys
import json
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Security Scope: Strictly restricted to files created or managed by this app.
# This ensures zero access to your personal/private files on Google Drive.
SCOPES = ['https://www.googleapis.com/auth/drive.file']

CLIENT_SECRETS_PATH = os.path.expanduser("~/raj_work_space/funzone/client_secrets.json")
CREDENTIALS_SAVED_PATH = os.path.expanduser("~/raj_work_space/funzone/drive_credentials.json")

def create_default_client_secrets():
    """Create default OAuth configuration if client_secrets.json is not present."""
    if not os.path.exists(CLIENT_SECRETS_PATH):
        # Standard web/installed app client secrets structure
        client_config = {
            "installed": {
                "client_id": "812345678901-example.apps.googleusercontent.com",
                "project_id": "funzone-ai-studio",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_secret": "GOCSPX-example-secret",
                "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
            }
        }
        with open(CLIENT_SECRETS_PATH, 'w') as f:
            json.dump(client_config, f, indent=2)

def authenticate_google_drive():
    """Perform secure console-based OAuth authentication for Google Drive."""
    gauth = GoogleAuth()
    gauth.settings['client_config_backend'] = 'file'
    gauth.settings['client_config_file'] = CLIENT_SECRETS_PATH
    gauth.settings['get_refresh_token'] = True
    gauth.settings['oauth_scope'] = SCOPES

    # Try loading saved credentials
    if os.path.exists(CREDENTIALS_SAVED_PATH):
        gauth.LoadCredentialsFile(CREDENTIALS_SAVED_PATH)

    if gauth.credentials is None:
        print("\n🔒 SECURE GOOGLE DRIVE OAUTH AUTHENTICATION")
        print("Scope: Restricted ONLY to 'Funzone_AI_Studio' folder & app files.")
        print("-" * 60)
        auth_url = gauth.GetAuthUrl()
        print(f"\n👉 STEP 1: Open this link in your browser:\n\n{auth_url}\n")
        print("👉 STEP 2: Log in with your 5TB Google Account & Click 'Allow'.")
        print("👉 STEP 3: Copy the Authorization Code shown on screen.")
        print("-" * 60)
        
        # Wait for user input (or via environment variable)
        auth_code = input("Enter the Verification Code here: ").strip()
        gauth.Auth(auth_code)
        gauth.SaveCredentialsFile(CREDENTIALS_SAVED_PATH)
        print("✅ Credentials saved securely to drive_credentials.json")
    elif gauth.access_token_expired:
        print("🔄 Refreshing Google Drive Security Access Token...")
        gauth.Refresh()
        gauth.SaveCredentialsFile(CREDENTIALS_SAVED_PATH)
    else:
        gauth.Authorize()

    drive = GoogleDrive(gauth)
    print("🎉 Google Drive connected successfully!")
    return drive

def upload_workspace_to_drive(drive, folder_name="Funzone_AI_Studio"):
    """Find or create the target folder in Google Drive and sync files."""
    # Search if target folder exists
    file_list = drive.ListFile({'q': f"title = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"}).GetList()
    
    if file_list:
        parent_folder = file_list[0]
        print(f"📁 Target Google Drive Folder Found: '{folder_name}' (ID: {parent_folder['id']})")
    else:
        parent_folder = drive.CreateFile({'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'})
        parent_folder.Upload()
        print(f"📁 Created New Target Google Drive Folder: '{folder_name}' (ID: {parent_folder['id']})")

    # Files to sync
    workspace_root = os.path.expanduser("~/raj_work_space/funzone")
    files_to_sync = [
        "plan.md",
        "notebooks/ai_studio_master.ipynb",
        "scripts/drive_manager.py",
        "scripts/code_engine.py"
    ]

    for rel_path in files_to_sync:
        local_filepath = os.path.join(workspace_root, rel_path)
        if os.path.exists(local_filepath):
            filename = os.path.basename(local_filepath)
            # Check if file already exists in Drive folder
            existing = drive.ListFile({'q': f"title = '{filename}' and '{parent_folder['id']}' in parents and trashed = false"}).GetList()
            if existing:
                drive_file = existing[0]
                drive_file.SetContentFile(local_filepath)
                drive_file.Upload()
                print(f"🔄 Updated in Google Drive: {rel_path}")
            else:
                drive_file = drive.CreateFile({'title': filename, 'parents': [{'id': parent_folder['id']}]})
                drive_file.SetContentFile(local_filepath)
                drive_file.Upload()
                print(f"⬆️ Uploaded to Google Drive: {rel_path}")

    print("✅ All local workspace files are now synced to Google Drive!")

if __name__ == "__main__":
    create_default_client_secrets()
    print("Script ready for Google Drive OAuth Sync.")
