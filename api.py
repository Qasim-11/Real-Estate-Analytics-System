import requests
from requests.adapters import HTTPAdapter
import ssl
import urllib3
import json

# The code will work without this line, but will show a lot of warnings, and it's because of the SSL certificate of the server
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# A custom adapter to handle the lagacy SSL connections
class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.options |= ssl.OP_LEGACY_SERVER_CONNECT
        kwargs['ssl_context'] = context
        return super(SSLAdapter, self).init_poolmanager(*args, **kwargs)

# Create a session and mount the custom adapter
session = requests.Session()
session.mount('https://', SSLAdapter())

def test_request():
    headers = { "Accept": "application/json" }
    data = None
    response = session.get('https://open.data.gov.sa/data/api/datasets?version=-1&dataset=a530f315-f5b7-4693-9d12-e46c7208cb18', headers=headers, data=data)
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))

test_request()
