# busycal
Just makes all iCalendar events from transparent to opaque (busy).

I use it on Google Calendar for my university lectures. The university's iCalendar publishes all events as "transparent events" and Google Calendar shows my status as "Not Busy" during classes.

## New Feature

You can add the URL parameter `prepend` to prepend a piece of text in every iCalendar event.

Like this: `http://127.0.0.1:8000/?prepend=<Course+Name>&ical=<ical_url>`

The event will be updated from this:

```
Teaching Event
Monday 8 to 10
```

To this:


```
Course Name Teaching Event
Monday 8 to 10
```


## Quickstart

```
docker build . --target build-image -t busycal
sudo docker run busycal --bind 0.0.0.0:8000
```

The new iCalendar link will be: `http://127.0.0.1:8000/?ical=<ical_url>`

You can protect the endpoint with a token by setting the enviroment variable `BUSYCAL_TOKEN` to a token of your choice. After that you just add to the request url the query parameter `token=<BUSYCAL_TOKEN>`.

Like this: `http://127.0.0.1:8000/?token=<secret+token>&prepend=<Course+Name>&ical=<ical_url>`
