#!/bin/sh

curl -X POST -H 'Authorization: Bearer ここにアクセストークンを入力' -F 'message=不審者を検知しました!' https://notify-api.line.me/api/notify
