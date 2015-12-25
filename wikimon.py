#!/usr/bin/python2
import mwclient

def msg_status(msg):
    print "%s{*} %s%s" %(BLUE, msg, CLEAR)

def msg_abort(msg):
	print "%s{!} Fatal Exception has been hit, quitting with stack trace.\n %s%s" %(RED, msg, CLEAR)

def monitor_loop(wiki):

def get_wiki(url, auth=False, username=None, password=None):
    # returns a wiki object, optionally logs in
    msg_status("Attempting to connect to %s" %(url))
    try:
        wiki = mwclient.Site(url)
    except Exception, e:
        msg_abort(str(e))
    if auth == True:
        try:
            msg_status("Attempting to log into the wiki")
            wiki.login(username, password)
        except Exception, e:
            msg_abort(str(e))
        return wiki
    else:
        return wiki 

