from brownie import network, accounts, config, SimpleStorage


def deploy_simple_storage():
    account = get_account()

    simple_storage = SimpleStorage.deploy({"from": account})
    print(f"\t{simple_storage}")

    stored_value = simple_storage.retrieve()
    print(f"\tOriginal value: {stored_value}\n")

    tx = simple_storage.store(15, {"from": account})
    stored_value = simple_storage.retrieve()
    print(f"\tUpdated value: {stored_value}")


def get_account():
    if network.show_active() == "custom-polygon-main-fork":
        return accounts[0]

    return config["wallets"]["ACCOUNT1"]


def main():
    deploy_simple_storage()
