# NBN Housing Guide 2013

## Initial Setup

To get the app working locally, first set up a postGIS database using the settings configuration.

Once you've synced the database and migrated using South, run the following commands in /housing:

```bash
./manage.py import_shapes  
./manage.py csvimport --model='guide.Dorm' csv/dorms.csv  
./manage.py csvimport --mappings='column1=name,column2=text,column3=source,column4=dorm(Dorm|name)' --model='guide.Quote' --charset='utf-8' csv/quotes.csv  
```

Then, runserver and the app should be working.
