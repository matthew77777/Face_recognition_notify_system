#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import subprocess

pirPin = 17
ledPin = 18

#BCMモードに設定
GPIO.setmode(GPIO.BCM)

#GPIO17を入力モードに設定
GPIO.setup(pirPin, GPIO.IN)

#GPIO18を出力モードに設定
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        pir_val = GPIO.input(pirPin) 

        if pir_val == GPIO.HIGH:
            print("人を検知しました。")
            GPIO.output(ledPin,GPIO.HIGH)
        else :
            print("人を検知しませんでした。")
            GPIO.output(ledPin,GPIO.LOW)

        time.sleep(0.1)

except KeyboardInterrupt:
    print( 'システム終了')
    GPIO.cleanup()

