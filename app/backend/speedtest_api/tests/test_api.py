from rest_framework.test import APITestCase

from speedtest_api.models import Node
from speedtest_api.models import Wallet
from speedtest_api.models import Account
from speedtest_api.models import Transaction


class ApiTests(APITestCase):
    def setUp(self):
        mumbai_node = Node.objects.create(IP="http://127.0.0.1:7076",
                                          latitude=1.1,
                                          longitude=1.1,
                                          location_name="Mumbai")

        virginia_node = Node.objects.create(IP="http://127.0.0.1:7077",
                                            latitude=1.1,
                                            longitude=1.1,
                                            location_name="N. Virginia")

        mumbai_wallet = Wallet.objects.create(node=mumbai_node)
        virginia_wallet = Wallet.objects.create(node=virginia_node)

        mumbai_account = Account.objects.create(wallet=mumbai_wallet,
                                                address=
                                                "xrb_3er5ka9cx6nxtcfapcj77za3n4ne74xbp9b6sbxnuzan9iorxj3xoyy6h1n1",
                                                current_balance=10000000000000000000000,
                                                POW="POW")

        virginia_account = Account.objects.create(wallet=virginia_wallet,
                                                  address=
                                                  "xrb_3stk814q3ksqopqgeemzk7kduyjzhu355dmmon3ypco3dwbrm6c93wgspsy6",
                                                  current_balance=10000000000000000000000,
                                                  POW="POW")

        transaction = Transaction.objects.create(id=27,
                                                 origin=mumbai_account,
                                                 destination=virginia_account,
                                                 amount=1,
                                                 initiated_by="127.0.0.1:7076")

    def test_random_transaction(self):
        response = self.client.get('/transactions/random', format='json')
        self.assertEqual(response.status_code, 200)

    def test_send_transaction(self):
        response = self.client.post('/transactions/send', {'id': 27}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_send_transaction_negative(self):
        send_response = self.client.post('/transactions/send', {'id': 0}, format='json')
        self.assertEqual(send_response.status_code, 404)
