from  datetime import date, datetime
import pytz

bogota_timezon = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezon)
print("Bogotá:", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

hola = ("hola", "1")

for i in hola:
   print(i)
