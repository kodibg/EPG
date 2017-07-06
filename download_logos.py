import json
import requests
import shutil
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

streams = []
print "Starting..."
s = requests.Session()
s.verify=False
    
with open("mapping.json") as f:
  streams = json.load(f)["streams"]
  
for key,stream in streams.iteritems():
  url = stream.get("logo")
  if url == None:
    print "no logo for %s" % key
    continue
    
  headers = {"Accept-Encoding": "gzip, deflate"}
  r = None
  try:
    print "Getting logo from %s" % url
    r = s.get(url, headers=headers, stream=True, verify=False)
  except Exception, e:
    print str(e)
    continue
    
  path = ".\\logos\\%s.png" % key.replace(" ", "").replace(")", "").replace("(", "").replace("+", "plus").replace("-", "minus").lower()
  print "log=%s" % path
  
  with open(path, 'wb') as w:
    r.raw.decode_content = True
    shutil.copyfileobj(r.raw, w)