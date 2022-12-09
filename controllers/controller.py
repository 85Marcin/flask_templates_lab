from flask import render_template, request, redirect
from app import app
from models.event_list import events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Upcoming events', events= events )

@app.route('/events', methods=['POST'])
def create():
    name = request.form['event_name']
    event_date = request.form['event_date']
    number_of_guests = request.form['number_of_guests']
    location = request.form['location']
    event_description = request.form['event_description']
    recurring_event = request.form['recurring_event']

    new_event = Event(name, event_date, number_of_guests, location, event_description, recurring_event)
    events.append(new_event)
    return redirect('/events')