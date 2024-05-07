import os
import requests
import pandas as pd
from datetime import datetime

url = "xxx"

payload = {
    'description': 'Hello dear, this is a text sms.',
    'service_id': '1',
    'mask_id': '1',
    'organization_id': '1'
}

