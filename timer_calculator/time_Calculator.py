Durations_flag = "AM"
D_days = 0

days={
    "Saturday":0 ,
    "Sunday" :1,
    "Monday":2,
    "Tuesday":3, 
    "Wednesday":4,
    "Thursday":5,
    "Friday":6
}

def day_identifier(current_day , D_days):
    global days

    current_day = int(days.get(current_day))
    current_day+= D_days

    if current_day >= 14 :
      current_day -=14

    
    if current_day >= 7:
        current_day-=7

    for key , val in days.items() :
        if val == current_day:
            return key



def chang_Duration():

    global Durations_flag , D_days  

    if Durations_flag == "AM" :
        Durations_flag = "PM"
    else :
        Durations_flag = "AM"
        D_days+=1




def add_time(start, duration , current_day = None):

    global Durations_flag ,D_days 

    """operation on Duration"""

    D_hours ,D_mints = duration.split(':')
    D_hours ,D_mints = int(D_hours) , int(D_mints)
    D_mints = "{:02d}".format(D_mints)

    #conver Hours Duration into days and hours
    if D_hours >= 24 :
        D_days = D_hours / 24
        D_days = int(D_days)
        D_hours = D_hours % 24
       

    """Operation on Current time"""

    C_hour, C_min  = start.split(':')
    C_min , Durations_flag = C_min.split()

    
    C_hour, C_min = int(C_hour) ,int(C_min)
    C_hour += int(D_hours)
    C_min  += int(D_mints)



    if C_min > 60:
        C_hour+=1
        C_min = C_min - 60
        


    if C_hour > 12:
       C_hour-= 12
       chang_Duration()

    if  C_hour >= 12:  
       chang_Duration()

    #Channging the format of minutes to two digits
    C_min = "{:02d}".format(int(C_min))
    #Printing time
    if current_day == None :
        if D_days == 1:
            new_time =f"{C_hour}:{C_min} {Durations_flag} (next day)"
        elif D_days == 0:
            new_time =f"{C_hour}:{C_min} {Durations_flag}"
        else:
            new_time =f"{C_hour}:{C_min} {Durations_flag} ({D_days} days later)"    
    else:
        current_day = current_day.capitalize()
        if D_days == 1:
            new_time =f"{C_hour}:{C_min} {Durations_flag}, {day_identifier(current_day, D_days)} (next day)"
        elif D_days == 0:
            new_time =f"{C_hour}:{C_min} {Durations_flag}, {day_identifier(current_day, D_days)}"               
        else:
            new_time =f"{C_hour}:{C_min} {Durations_flag}, {day_identifier(current_day, D_days)} ({D_days} days later)"

    Durations_flag = "AM"
    D_days = 0
    return new_time
