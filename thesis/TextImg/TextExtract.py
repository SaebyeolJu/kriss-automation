from __future__ import print_function
import httplib2
import os
import io
import argparse
import natsort

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

try:
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = '/Users/SBJ/Desktop/kriss/thesis/credenetials.json'
APPLICATION_NAME = 'Kriss'

def get_credentials():
    credential_path = os.path.join("../", 'credentials.json')
    store = Storage(credential_path)
    credentials = None
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    DIR = '/Users/SBJ/Desktop/kriss/thesis/TextImg'
    image_list = (os.listdir(DIR))
    image_list = natsort.natsorted(image_list)
    print(image_list)

    for i in range(0, len(image_list)):
        print(i, image_list[i])
        imgfile = image_list[i]
        textfile = image_list[i] + '.txt'
        print(textfile)

        mime = 'application/vnd.google-apps.document'
        res = service.files().create(
            body={
                'name': imgfile,
                'mimeType': mime
            },
            media_body=MediaFileUpload(imgfile, mimetype=mime, resumable=True)
        ).execute()

        downloader = MediaIoBaseDownload(
            io.FileIO(textfile, 'wb'),
            service.files().export_media(fileId=res['id'], mimeType="text/plain")
        )
        done = False
        while done is False:
            status, done = downloader.next_chunk()

    service.files().delete(fileId=res['id']).execute()
    print("Done.")


if __name__ == '__main__':
    main()