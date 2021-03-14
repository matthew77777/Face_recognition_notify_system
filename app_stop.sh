#!/bin/sh

ps aux | grep app.py | grep -v grep | awk '{ print "kill -9", $2 }' | sh

