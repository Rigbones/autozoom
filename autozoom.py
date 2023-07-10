import pyautogui as pyg
import webbrowser as wb
import datetime as dt
import time
import click

# ISC 311 zoom link
ZOOM_LINK = r"https://korea-ac-kr.zoom.us/j/97797472566?pwd=NjI5ZENFV2hDU1BPVWpMd21kNXNzQT09"
# Meeting time
MEETING_TIME = dt.time(hour=8, minute=0, second=0)

def format_date(x):
    date_list = x.split(sep="-")
    return list(map(int, date_list))

def format_time(x):
    time_list = x.split(sep="-")
    return list(map(int, time_list))

def given_datetime(given_date, given_time):

    # YY, MM, DD, HH, MM
    return dt.datetime(given_date[2], given_date[1], given_date[0], given_time[0], given_time[1], given_time[2])

def join_meeting(zoom_link, meeting_date, meeting_time):
    """
    Joins zoom meeting automatically at the specified time
    Args:
        zoom_link: raw string.  The meeting link
        meeting_time: time object.  The meeting time
    """

    now = dt.datetime.now()

    # time difference between current and meeting time
    wait_time_sec = (required_datetime - dt.datetime.now().replace(microsecond=0)).total_seconds()
    print("Your ZOOM meeting starts in " + str(wait_time_sec/60) + " min")
    time.sleep(wait_time_sec)

    # zoom app related
    wb.get(using='chrome').open(zoom_link, new=2) #open zoom link in a new window
    time.sleep(5) # given time for the link to show app top-up window
    pyg.click(x=805, y=254, clicks=1, interval=0, button='left') # click on open zoom.app option
    time.sleep(10) # wait for 10 sec
    pyg.click(x=195, y=31, clicks=1, interval=0, button='left') # maximize zoom app
    time.sleep(3) # wait for 3 sec
    pyg.click(x=50, y=776, clicks=1, interval=0, button='left')

now = dt.datetime.now()
start = dt.datetime(2023, now.month, now.day, 8, 0, 0)
time_delta = now - now

# while not 09:40 yet
while (time_delta.total_seconds() < 6000):
    # press enter every 5 seconds
    pyg.press("enter", presses=1, interval=5)
    print("ENTER key pressed at", now)
    # calculate new time difference between 08:00 and now
    now = dt.datetime.now()
    time_delta = now-start

    