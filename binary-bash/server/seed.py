from faker import Faker
from random import choice as rc
from datetime import datetime

fake = Faker()

from app import app
from models import db, User, Event, EventUser

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        User.query.delete()
        Event.query.delete()
        EventUser.query.delete()

        print("Seeding events...")
        event1 = Event(title="Housewarming party", image="https://i.pinimg.com/236x/d8/57/8a/d8578a7c90c9944169a16241ca3920d5.jpg", location="My house", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        event1.start_time = datetime(2012, 3, 3, 10, 10, 10)
        event1.end_time = datetime(2012, 3, 3, 10, 10, 20)

        event2 = Event(title="Birthday party", image="https://images.ctfassets.net/sfnkq8lmu5d7/5s1kya8JDQapExFKfM8ahI/20f07aaace35649eefb27022a2f13556/2021_0517-catGotchaDay-AdobeStock_235571404.jpg?w=1000&h=750&fl=progressive&q=70&fm=jpg", location="My house", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
        event2.start_time = datetime(2012, 3, 3, 10, 10, 10)
        event2.end_time = datetime(2012, 3, 3, 10, 10, 20)

        events = [
            event1,
            event2
            # Event(title="Birthday party", image="https://images.ctfassets.net/sfnkq8lmu5d7/5s1kya8JDQapExFKfM8ahI/20f07aaace35649eefb27022a2f13556/2021_0517-catGotchaDay-AdobeStock_235571404.jpg?w=1000&h=750&fl=progressive&q=70&fm=jpg", location="My house", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", start_time="2024-02-20 17:00:00", end_time="2024-02-20 17:00:00"),
            # Event(title="My party", image="https://media.istockphoto.com/id/955853964/photo/cut-siamese-party-cat-wearing-birthday-hat.jpg?s=1024x1024&w=is&k=20&c=zmfZlyvnnKXfXG8A0fEqc8fnUh6Wig6E8Hpln7TnSEw=", location="My house", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", start_time="2024-02-20 17:00:00", end_time="2024-02-20 17:00:00"),
            # Event(title="Final project demos", image="", location="Flatiron School", description="Come watch the Final project demos for phase 4.", start_time="2024-02-16 10:00:00", end_time="2024-02-16 11:00:00")
        ]

        db.session.add_all(events)

        print("Seeding users...")
        users = [
            User(username="miguelvasquez"),
            User(username="brunorossi"),
            User(username="bencavins"),
        ]

        db.session.add_all(users)

        print("Adding events to users...")
        events_users = [
            EventUser(user_id=1, event_id=1, type="host"),
            EventUser(user_id=2, event_id=1, type="guest"),
            EventUser(user_id=3, event_id=1, type="guest"),
            EventUser(user_id=1, event_id=2, type="guest"),
            EventUser(user_id=2, event_id=2, type="host"),
            EventUser(user_id=3, event_id=2, type="guest")
        ]
        db.session.add_all(events_users)
        db.session.commit()

        print("Done seeding!")