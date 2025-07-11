import os.path
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

# If modifying these SCOPES, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

class EmailInput(BaseModel):
    """Input for sending an email."""
    to_email: str = Field(..., description="Recipient email address.")
    subject: str = Field(..., description="The subject of the email.")
    message: str = Field(..., description="The body of the email.")

class SendEmailTool(BaseTool):
    name: str = "Send Email"
    description: str = "Sends an email to a specified recipient using the Gmail API."
    args_schema: Type[BaseModel] = EmailInput

    def _run(self, to_email: str, subject: str, message: str) -> str:
        """Uses the Gmail API to send an email."""
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            service = build("gmail", "v1", credentials=creds)
            mime_message = MIMEMultipart()
            mime_message.attach(MIMEText(message, "html"))
            mime_message["to"] = to_email
            mime_message["subject"] = subject
            encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

            create_message = {"raw": encoded_message}
            send_message = (
                service.users()
                .messages()
                .send(userId="me", body=create_message)
                .execute()
            )
            return f"Email sent successfully! Message ID: {send_message['id']}"

        except HttpError as error:
            return f"An error occurred: {error}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"