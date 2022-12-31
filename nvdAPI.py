import requests
import json
from pprint import pprint
import os

ops = os.name

response = requests.get(f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={ops}&keywordExactMatch")
pprint(response.json())