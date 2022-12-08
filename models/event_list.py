from models.event import Event
import datetime

import datetime

date_1 = datetime.date(2022, 12, 11)
date_2 = datetime.date(2022, 12, 21)

event_1 = Event("Concert", date_1, 200, "Edinburgh", "Christmas concert for kids", True)
event_2 = Event("Film", date_2, 100, "Cinema", "Horror film festival", False)

events = [event_1, event_2]