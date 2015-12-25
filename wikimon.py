#!/usr/bin/python2
# coding: utf-8
import mwclient # mediawiki library.
import json # because why not use json.
import sys # sys.exit and sys.argv
import urlparse # because mwclient can't daelwae urls
import time

# colours, because everything is better with colours.
RED = "\x1b[1;31m" # fatal errors
GREEN = "\x1b[1;32m" # page creation
CLEAR = "\x1b[0m" # clear
CYAN = "\x1b[1;36m" # page names.
BLUE = "\x1b[1;34m" # status
YELLOW = "\x1b[1;33m" # page deletion/exterminatus


# status message/output functions.
def msg_status(msg):
    # status messages about state of program itself.
    print "%s{*} %s%s" %(BLUE, msg, CLEAR)

def msg_abort(msg):
    # fatal errors and stack traces. aborts.
    sys.exit("%s{!} Fatal Exception has been hit, quitting with stack trace.\n %s%s" %(RED, msg, CLEAR))

def msg_create(msg):
    # page creation events. Hideous use of format strings.
    print "%s{+} Page: %s%s%s has been created.%s" %(GREEN, CYAN, msg, GREEN, CLEAR)

def msg_delete(msg):
    # page deletion event. Hideous use of format strings.
    print "%s{-} Page: %s%s%s has been deleted/purged.%s" %(YELLOW, CYAN, msg, YELLOW, CLEAR)

# now for the actual wiki handling functions...
def monitor_loop(wiki):
    # monitors for page create/delete instances. alerts.
    msg_status("Entering Monitor Loop... Populating the initial list.")
    pages = []
    for page in wiki.allpages():
        pages.append(page.name)
    print 'got initial pages list'
    # now we poke it every 5 minutes to find pages missing or present
    while True:
        new_pagelist = []
        for page in wiki.allpages():
            new_pagelist.append(page.name)
        # first we check if there is any difference at all...
        if cmp(pages, new_pagelist) != 0:
            # ok, if we get here, its non zero, so something changed.
            # now for the horrible comparison. lets see if any items in list 1
            # are NOT in list 2. this is how we determine if a page was purged
            for page in pages:
                if page in new_pagelist:
                    pass # its in both, do nothing
                else:
                    log_event('delete', page)
                    msg_delete(page)
            # now we do the same disgusting logic in reverse to find created pages
            for page in new_pagelist:
                if page in pages:
                    pass # its in both, do nothing
                else:
                    log_event('create', page)
                    msg_create(page)
        pages = new_pagelist # this SHOULD overwrite the variable pages. I hope.
        else:
            msg_status("%s: No change, sleeping for 5 minutes." %(time.time()))
            time.sleep(300) # sleep for 5 minutes

def log_event(event_type, page_name):
    # we want to log if pages were created or expunged, for fun.
    # this is in a pseudo-csv format for now because reasons.
    # we basically log "time.time(),create/delete,page_name"
    f = open("wiki_event_log.txt", "a+")
    entry = "%s,%s,%s\n" %(time.time(), event_type, page_name)
    f.write(entry)
    f.close()


def get_wiki(url, auth=False, username=None, password=None):
    # returns a wiki object, optionally logs in
    msg_status("Attempting to connect to %s" %(url))
    # ah fuck. we have to parse the url...
    wiki_url = urlparse.urlparse(url)
    try:
        wiki = mwclient.Site((wiki_url.scheme, wiki_url.netloc), path=wiki_url.path)
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

def run_it(config):
    # parses config, does voodoo.
    try:
        msg_status("Parsing config file: %s" %(config))
        config = json.loads(open(config, 'rb').read())
    except Exception, e:
        msg_abort(e)
    if config['auth'] == 1:
        wiki = get_wiki(url=config['wiki'], auth=True, username=config['username'], password=config['password'])
    else:
        wiki = get_wiki(url=config['wiki'], auth=False, username=None, password=None)
    monitor_loop(wiki)

def main(args):
    if len(args) != 2:
        sys.exit("use: %s config.json" %(args[0]))
    run_it(config=args[1])

if __name__ == "__main__":
    main(args=sys.argv)
