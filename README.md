# Python Web Push

Use [pywebpush](https://pypi.org/project/pywebpush/) to push web notification

## End to End steps

1. Subscribe  
https://ryukerliu.github.io/web-push-play-ground/  
Subscribe Push Notification  
Code: https://github.com/RyukerLiu/web-push-play-ground  

2. Push  
Once you get the subscription info, see below how to push.

## How to push with python

You can see test case for some hint.

`python -m unittest`

And you can run it in command line interface

```
python web_push.py '{"endpoint":"https://fcm.googleapis.com/fcm/send/ftnhAYvJICI:APA91bHOgwyoc63thYr6UBAW0CoUlO3Qozv6r2APpVYSwcVlIB4MqjkCz1z9EyfLrWDfxcZW5HmCNHyF9Inp4l55MSz43HM_994fySWn351rKsJSQvRjUXlIbjXQRbhWbOWkeYCD9yQb","expirationTime":null,"keys":{"p256dh":"BLIF4Jliedu67IRqVIUrhlvYKFfJH_FJL0EHkyX40k9aATL8aUd90XbkaVOPLJVN8hwVhSuwTkLEjsM1UHDosDI","auth":"ZwKXLnviy1oh4j0QuBGj0Q"}}' 'Hello World'
```