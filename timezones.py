from datetime import datetime
import pytz

bogota_tz = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_tz)
print("Bogotá:", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_tz = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_tz)
print("Ciudad de México:", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))

caracas_tz = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_tz)
print("Caracas:", caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))
