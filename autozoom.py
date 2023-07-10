import pyautogui as pyg
import webbrowser as wb
import datetime as dt
import time
import click

# Today
TODAY = dt.datetime.today()
# ISC 311 zoom link
ZOOM_LINK = r"https://korea-ac-kr.zoom.us/j/97797472566?pwd=NjI5ZENFV2hDU1BPVWpMd21kNXNzQT09"
# Class start datetime
CLASS_START_DATETIME = dt.datetime(year=TODAY.year, month=TODAY.month, day=TODAY.day, hour=8, minute=0, second=0)
# Class end datetime
CLASS_END_DATETIME = dt.datetime(year=TODAY.year, month=TODAY.month, day=TODAY.day, hour=9, minute=40, second=0)


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
        time.sleep(30)  # sleeps for 30 seconds

    # join meeting
    wb.open(url=zoom_link, new=2)
    time.sleep(5)  # sleep 5 seconds to allow browser to open and load
    # press open meeting
    pyg.press("left", _pause=1) # left to choose "open zoom meetings", pause 1 second after
    pyg.press("enter", _pause=6) # enter key to click "open zoom meetings", pause 6 seconds after
    # KU agreements
    pyg.press("enter") # accept KU agreements

def join_breakout():
    """
    Joins breakout rooms automatically during the class time
    Works by spam-clicking the enter key
    """
    # calculate how long each class is in seconds
    class_duration = (CLASS_END_DATETIME - CLASS_START_DATETIME).total_seconds()
    while (True):
        now = dt.datetime.now()
        seconds_passed_since_class_started = (now - CLASS_START_DATETIME).total_seconds()
        # if not 09:40 yet
        if (seconds_passed_since_class_started > class_duration):
            print("Hooray!  Class has ended.")
            break
        # if still not 09:40 yet
        print("ENTER key pressed at", now)
        pyg.press("enter", _pause=5)  # pause 5 seconds after ENTER key press

join_meeting(ZOOM_LINK, CLASS_START_DATETIME)
join_breakout()




    