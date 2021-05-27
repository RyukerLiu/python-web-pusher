import unittest
from web_push import web_push
from unittest.mock import MagicMock

class TestWebPush(unittest.TestCase):

    def test_web_push(self):
        # Mock it beacuse subscription_info is different from client user
        web_push = MagicMock()

        subscription_info=(
        '{"endpoint":"https://fcm.googleapis.com/fcm/send/ftnhAYvJICI:APA91bHOgwyoc63'
        'thYr6UBAW0CoUlO3Qozv6r2APpVYSwcVlIB4MqjkCz1z9EyfLrWDfxcZW5HmCNHyF9Inp4l55MSz43HM_994fySWn351rKs'
        'JSQvRjUXlIbjXQRbhWbOWkeYCD9yQb","expirationTime":null,"keys":{"p256dh":"BLIF4Jliedu67IRqVIUrhlv'
        'YKFfJH_FJL0EHkyX40k9aATL8aUd90XbkaVOPLJVN8hwVhSuwTkLEjsM1UHDosDI","auth":"ZwKXLnviy1oh4j0QuBGj0'
        'Q"}}'
        )
        data='Test Push'
        web_push(subscription_info, data)
        web_push.assert_called_with(subscription_info, data)

if __name__ == '__main__':
    unittest.main()
