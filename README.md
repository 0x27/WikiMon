# WikiMon
Monitors a MediaWiki Instance for page creation and deletion events in a loop.  
Designed to monitor the 32c3 wiki for fun.  
Oh, it also alerts/logs if the Wiki is not responding properly, as it has less uptime than a not-up thing. I might be able to make some cool charts of wiki uptime over time as the event goes on :)

## Configuration
Just edit the config.json file. Auth can be 0 or 1. Credentials are ignored if auth is 0.

```
{
    "wiki": "https://events.ccc.de/congress/2015/wiki/",
    "auth": 0,
    "username": "blank",
    "password": "blank"
}
```

## Requirements  
Depends on the [mwclient](https://github.com/mwclient/mwclient) library, so just do `pip install mwclient`. Written for Python2, don't expect it to actually work on Python3.

## Running
Just run it with the config file as the arg.

## Cool ideas
I'll be logging downtime/wiki not respond properly using this script throughout the event, and might be able to generate some cool graphs from the logs, maybe :)  
If it works out, next version will have an IRC notifier and twitter bot for 33c3, or maybe I will code that during 32c3 as I am stuck on my arse at home trying to avoid studying for exams :P

## Licence
Licenced under the [WTFPL](http://wtfpl.net), so do whatever. 

## Documentation
Most of the code is self-documenting with comments, if anything is unclear as to why I did it, let me know in the issue tracker or on twitter.

## Beer?
Send yer cryptologically generated beer tokens to fuel further opensource software:  
[coinbase, for convenience](https://www.coinbase.com/infodox/), or the following bitcoin address: `13rZ67tmhi7M3nQ3w87uoNSHUUFmYx7f4V`

## Bug Reports and Feature Requests
Please submit all bug reports and feature requests to the [Github Issue Tracker](https://github.com/0x27/WikiMon/issues)

## Footnote  
This script is not intended for serious purposes. Just curious about what gets created/rm'd as congress goes on.
