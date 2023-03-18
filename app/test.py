import datetime
import pytz
a = datetime.datetime.now(pytz.timezone('America/Mexico_City'))
b=datetime.datetime.strftime(a,'%H%M')
if int(b) < 1000:
    print("A")