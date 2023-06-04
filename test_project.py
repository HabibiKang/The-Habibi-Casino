from project import deposit, payout_win, payout_loss

def test_deposit():
    balance = deposit(100)
    assert balance == "Your balance is now $100!"

def test_payout_win():
    global balance
    balance = 100
    balance = payout_win(100)
    assert balance == 200

def test_payout_loss():
    global balance
    balance = 200
    balance = payout_loss(100)
    assert balance == 100

