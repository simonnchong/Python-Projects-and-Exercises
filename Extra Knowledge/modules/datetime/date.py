from datetime import date
from datetime import datetime
def main():
    ##DATETIME OBJECTS
    #Get today's date from datetime class
    today=datetime.now()
    #print (today)
    # Get the current time
    #t = datetime.time(datetime.now())
    #print "The current time is", t
    #weekday returns 0 (monday) through 6 (sunday)
    wd=date.weekday(today)
    #Days start at 0 for monday
    print(today)
    days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    print("Today is day number %d" % wd)
    print("which is a " + days[wd])

if __name__== "__main__":
    main()