import requests
import time
from datetime import datetime


try:
   s = datetime.now()
   count = 1
   while True:
       st = datetime.now()
       ocr = requests.get("http://192.168.0.116:10050/doSegmentation?img_url=https://s3-ap-southeast-1.amazonaws.com/ocrvdime/ocrtesting/01-02-2016-22-45-993_cc-327931_1462440709.jpg&clientID=FUNDS_INDIA&typeOfImage=CHEQUE")
       et = datetime.now()
       print str(count), ocr.content, str((et - st).total_seconds())
       count += 1
except KeyboardInterrupt:
   
   e = datetime.now()
   print "Total time: %s" % str((e - s).total_seconds())
   pass# nammu
# nammu
