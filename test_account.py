import pytest
from account import *
def test_deposit():
    # Strings
    assert pytest.raises(ValueError, Account.deposit, "x", "y")
    assert pytest.raises(ValueError, Account.deposit, 1, "y")
    assert pytest.raises(ValueError, Account.deposit, "x", 1.0)

    with pytest.rasies(TypeError):
        #negatives
        Account.deposit(-1,-1)
        Account.deposit(1,-1)
        Account.deposit(-1,1)
        #0
        Account.deposit(0,0)
        Account.deposit(0,1)
        Account.deposit(1,0)


def test_withdraw():
    # Strings
    assert pytest.raises(ValueError, Account.withdraw, "x", "y")
    assert pytest.raises(ValueError, Account.withdraw, 1, "y")
    assert pytest.raises(ValueError, Account.withdraw, "x", 1.0)

    with pytest.rasies(TypeError):
        # negatives
        Account.withdraw(-1, -1)
        Account.withdraw(1, -1)
        Account.withdraw(-1, 1)
        # 0
        Account.withdraw(0, 0)
        Account.withdraw(0, 1)
        Account.withdraw(1, 0)


