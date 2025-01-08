# google_calendar/utils.py
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from requests import Request
from icecream import ic
from datetime import datetime 


# The file containing the client secret
CLIENT_SECRET_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)),'client_secret.json').replace("\\", "/")


# The scopes required to interact with Google Calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_credentials():
    """Get Google API credentials and authenticate the user."""
    creds = None
    # The token.pickle file stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        try:
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        except Exception as e:
            print("Failed to load token:", e)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=2020)
        
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return creds

def create_event(event_details):
    """Create a Google Calendar event and return the event URL."""
    creds = get_credentials()
    
    try:
        service = build('calendar', 'v3', credentials=creds)

        # Add conferenceData with Google Meet setup
        event_details['conferenceData'] = {
            'createRequest': {
                'requestId': 'random-string',  # Make sure this is unique per event
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet'  # This is for Google Meet
                },
                'status': {
                    'statusCode': 'success'
                }
            }
        }

        event = service.events().insert(
            calendarId='primary',
            body=event_details,
            conferenceDataVersion=1  # Ensure this is set for Google Meet creation
        ).execute()

        # Event URL for Google Meet (if created)
        event_url = event.get('hangoutLink', 'No Meeting Link Available')

        return event_url
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def get_event_details(title, description,date, start_time, end_time):
    """Generate the event details with the Google Meet link."""
    # Combine time with today's date for full datetime
    start_datetime = datetime.combine(date, start_time).isoformat()
    end_datetime = datetime.combine(date, end_time).isoformat() 
    # Format the datetime objects for Google Calendar
    event_details = {
        'summary': title,
        'description': description,
        'start': {
            'dateTime': start_datetime, 
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'Asia/Kolkata',
        },
        'conferenceData': {
            'createRequest': {
                'requestId': 'random-string',
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet',
                },
                'status': {
                    'statusCode': 'success'
                }
            }
        },
        'reminders': {
            'useDefault': True,
        },
    }
    # ic(event_details) 
    return event_details
