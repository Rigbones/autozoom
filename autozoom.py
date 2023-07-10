import pyautogui as pyg
import webbrowser as wb
import datetime as dt
import time
import click

# path to google chrome exe file
# CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# wb.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
# wb.register("chrome", )
# today
TODAY = dt.datetime.today()
# ISC 311 zoom link
ZOOM_LINK = r"https://korea-ac-kr.zoom.us/j/97797472566?pwd=NjI5ZENFV2hDU1BPVWpMd21kNXNzQT09"
# Meeting datetime
MEETING_DATETIME = dt.datetime(year=TODAY.year, month=TODAY.month, day=TODAY.day, hour=8, minute=0, second=0)

def format_date(x):
    date_list = x.split(sep="-")
    return list(map(int, date_list))

def format_time(x):
    time_list = x.split(sep="-")
    return list(map(int, time_list))

def given_datetime(given_date, given_time):

    # YY, MM, DD, HH, MM
    return dt.datetime(given_date[2], given_date[1], given_date[0], given_time[0], given_time[1], given_time[2])

def join_meeting(zoom_link: str, meeting_datetime: dt.datetime):
    """
    Joins zoom meeting automatically at the specified time
    Args:
        zoom_link: raw string.  The meeting link
        meeting_datetime: python datetime object.  The meeting datetime
    """
    # detect time now and calculate time left until class starts
    while (True):
        now = dt.datetime.now()
        seconds_left_until_class = (meeting_datetime - now).total_seconds()
        # if class is due to start
        if (seconds_left_until_class < 0):
            print("Class starting!  Joining zoom...")
            break
        # if class hasn't started yet
        print(f"{seconds_left_until_class} seconds left until class starts.")
        dt.time.sleep(30)  # sleeps for 30 seconds
    # join meeting
    wb.open(url=zoom_link, new=2)
    

join_meeting(ZOOM_LINK, MEETING_DATETIME)

# now = dt.datetime.now()
# start = dt.datetime(2023, now.month, now.day, 8, 0, 0)
# time_delta = now - now

# # while not 09:40 yet
# while (time_delta.total_seconds() < 6000):
#     # press enter every 5 seconds
#     pyg.press("enter", presses=1, interval=5)
#     print("ENTER key pressed at", now)
#     # calculate new time difference between 08:00 and now
#     now = dt.datetime.now()
#     time_delta = now-start

    