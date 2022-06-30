from datetime import datetime
from playsound import playsound
alarm_time=input("ENter the time of the alarm o be set:HH:MM:SS\n")
def validate_time(alarm_time):
    if len(alarm_time) !=11:
        return "Invalid time format. Please try again.."
    else:
        if int((alarm_time[0:2]) > 12:
               return "Invalid Hour format. Please try again.."
        elif int((alarm_time[3:5]) > 59 :
               return "Invalid Minute Format. Please try again.."
        elif int((alarm_time[6:8]) > 59 :
               return "Invalid Seconds Format, Please try again.."
        else:
                 return "ok"
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period=alarm_time[9:11].upper()
print("Setting up alarm...")
while True:
    now=datetime.now()
    current_hour=now.strftime("%I")
    current_minute=now.strftime("%M")
    current_seconds=now.strftime("%S")
    current_period=now.strftime("%p")
    if (alarm_period == current_period):
        if(alarm_hour==current_hour):
            if (alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wakie Wakie")
                    playsound("Alarm Clock.mp3")
                    break
