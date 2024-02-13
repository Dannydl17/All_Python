import unittest
from bankApp.account import Account


class AccountTest(unittest.TestCase):
    def test_that_amount_can_be_deposit(self):
        account = Account('name', 0, '1234', '1')
        account.deposit(1_000)
        self.assertEqual(1_000, account.check_balance())

    def test_that_amount_can_be_deposit_Twice_test(self):
        account = Account('name', 0, '1234', '1')
        account.deposit(1_000)
        account.deposit(2_000)
        self.assertEqual(3_000, account.check_balance())

    def test_that_negative_number_cannot_be_deposit_test(self):
        account = Account('name', 0, '1234', '1')
        account.deposit(1_000)
        self.assertEqual(1_000, account.check_balance())
        account.deposit(-1_000)
        self.assertEqual(1_000, account.check_balance())

    def test_that_account_can_withdraw_test(self):
        account = Account('name', 0, '1234', '1')
        account.deposit(2_500)
        self.assertEqual(2_500, account.check_balance())

        account.withdraw(1_000)

        self.assertEqual(1_500, account.check_balance())

    def test_that_account_cannot_withdraw_negative_value_test(self):
        account = Account('name', 0, '1234', '1')
        account.deposit(2_500)
        self.assertEqual(2_500, account.check_balance())

        account.withdraw(-1_000)
        account.withdraw(-2_500)
        self.assertEqual(2_500, account.check_balance())

    def test_that_account_cannot_withdraw_above_your_balance_test(self):
        account = Account('name', 0, '1234', '1')
        account.deposit(2_500)
        self.assertEqual(2_500, account.check_balance())

        account.withdraw(3_500)
        self.assertEqual(2_500, account.check_balance())
        account.withdraw(4_500)
        self.assertEqual(2_500, account.check_balance())
