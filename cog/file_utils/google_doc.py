import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/documents"]


def connect_google_doc():
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
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("docs", "v1", credentials=creds)


def count_quotes(document_id):
    service = connect_google_doc()

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=document_id).execute()
    body = document.get("body")["content"][1:-1]

    return len(body)


def get_quote(document_id, number):
    service = connect_google_doc()

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=document_id).execute()
    body = document.get("body")["content"][1:-1]

    for count, quote in enumerate(body):
        if count == number - 1:
            return quote["paragraph"]["elements"][0]["textRun"]["content"]
    return None


def read_quotes(document_id):
    service = connect_google_doc()

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=document_id).execute()
    body = document.get("body")["content"][1:-1]

    response = ""
    for count, quote in enumerate(body):
        response += (
            str(count + 1)
            + ": "
            + quote["paragraph"]["elements"][0]["textRun"]["content"]
        )
    return response


def write_quote(sentence, message, document_id):
    service = connect_google_doc()

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=document_id).execute()
    count = len(document.get("body")["content"][1:-1])
    index = document.get("body")["content"][-1]["paragraph"]["elements"][0]["endIndex"]

    quote = (
        '"'
        + sentence
        + '", '
        + message.author.display_name
        + ", "
        + message.created_at.strftime("%d/%m/%Y, %H:%M:%S")
        + "\n"
    )
    requests = [
        {
            "insertText": {
                "location": {
                    "index": index - 1,
                },
                "text": quote,
            }
        }
    ]
    service.documents().batchUpdate(
        documentId=document_id, body={"requests": requests}
    ).execute()

    return count, quote
