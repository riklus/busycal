# busycal
Just makes all iCalendar events from transparent to opaque (busy).

I use it on Google Calendar for my university classes. The university's iCalendar publishes all events as "transparent events" and Google Calendar shows my status as "Not Busy" during classes.

## Quickstart

```
sudo docker build . -t busycal
sudo docker run busycal --bind 0.0.0.0:8000
```

The new iCalendar link will be: `http://127.0.0.1:8000/?url=<ical_url>`

You can protect the endpoint with a token by setting the enviroment variable `BUSYCAL_TOKEN` to a token of your choice. After that you just add to the request url the query parameter `token=<BUSYCAL_TOKEN>`.
