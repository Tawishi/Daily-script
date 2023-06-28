import datetime
import json
from dateutil import parser

# path of directory for saving the Activity Log
DIR = '/home/tawishi/Desktop/t./Daily-script/data/activities_'

"""
Class defining objects with Activities and their time entries (a JSON list)
"""
class ActivityList:
    def __init__(self, activities):
        self.activities = activities
        
    """
    Returns an object of this class
    Object has the activity name + time entries from get_activities_from_json() and get_time_entires_from_json()
    """
    def initialize_me(self):
        activity_list = ActivityList([])
        with open(DIR + str(datetime.date.today()) + '.json', 'r+') as f:
            data = json.load(f)
            activity_list = ActivityList(
                activities = self.get_activities_from_json(data)
            )
        return activity_list
    
    """
    Returns a list of activities for the day
    """
    def get_activities_from_json(self, data):
        return_list = []
        for activity in data['activities']:
            return_list.append(
                Activity(
                    name = activity['name'],
                    time_entries = self.get_time_entires_from_json(activity),
                )
            )
        self.activities = return_list
        return return_list
        
    """
    Returns a list of time entries for the activities returned in get_activities_from_json()
    """
    def get_time_entires_from_json(self, data):
        return_list = []
        for entry in data['time_entries']:
            return_list.append(
                TimeEntry(
                    start_time = parser.parse(entry['start_time']),
                    end_time = parser.parse(entry['end_time']),
                    days = entry['days'],
                    hours = entry['hours'],
                    minutes = entry['minutes'],
                    seconds = entry['seconds'],
                )
            )
        self.time_entries = return_list
        return return_list
    
    """
    Returna a JSON object of key: value form where
    key = 'activities' and
    value = result of activities_to_json()
    """
    def serialize(self):
        return {
            'activities' : self.activities_to_json()
        }
    
    """
    Returns a JSON object after
    serializing the activities listed in `activities`
    """
    def activities_to_json(self):
        activities_ = []
        for activity in self.activities:
            activities_.append(activity.serialize())
        
        return activities_

"""
Returns JSON of a single Activity and its time entries
"""
class Activity:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries
    
    """
    Return JSON object with the defined structure
    with name of activity and its time entries
    """
    def serialize(self):
        return {
            'name' : self.name,
            'time_entries' : self.make_time_entires_to_json()
        }
        
    """
    Returs a JSON of time entries 
    serialized using TimeEntry class serialize() 
    """
    def make_time_entires_to_json(self):
        time_list = []
        for time in self.time_entries:
            time_list.append(time.serialize())
        return time_list

"""
Class for time entry objects
"""
class TimeEntry:
    def __init__(self, start_time, end_time, days, hours, minutes, seconds):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = end_time - start_time
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def _get_specific_times(self):
        self.days, self.seconds = self.total_time.days, self.total_time.seconds
        self.hours = self.days * 24 + self.seconds // 3600
        self.minutes = (self.seconds % 3600) // 60
        self.seconds = self.seconds % 60

    def serialize(self):
        return {
            'start_time' : self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end_time' : self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            'days' : self.days,
            'hours' : self.hours,
            'minutes' : self.minutes,
            'seconds' : self.seconds
        }
