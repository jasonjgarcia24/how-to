import pytest
from brownie import SimpleStorage, config


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_deploy():
    account = config["wallets"]["ACCOUNT1"]

    simple_storage = SimpleStorage.deploy({"from": account})

    start_stored_value = simple_storage.retrieve()
    expected_stored_value = 0

    assert start_stored_value == expected_stored_value


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_updating_storage():
    account = config["wallets"]["ACCOUNT1"]

    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(15, {"from": account})
    start_stored_value = simple_storage.retrieve()
    expected_stored_value = 15

    assert start_stored_value == expected_stored_value
