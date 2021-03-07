#!/bin/sh

ps aux | grep human_detection.py | grep -v grep | awk '{ print "kill -9", $2 }' | sh

