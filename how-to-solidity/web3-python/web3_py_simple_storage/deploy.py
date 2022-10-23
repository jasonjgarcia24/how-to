import os
import json

from dotenv import load_dotenv
from solcx import compile_standard
from web3 import Web3

load_dotenv()

# from solcx import install_solc
# install_solc("0.6.0")


with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile Solidity code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.6.0",
)

simple_storage_abi_file = compiled_sol["contracts"]["SimpleStorage.sol"][
    "SimpleStorage"
]

with open("SimpleStorage.json", "w") as file:
    json.dump(compiled_sol, file)


bytecode = simple_storage_abi_file["evm"]["bytecode"]["object"]
abi = simple_storage_abi_file["abi"]

# Connect to Ganache
host = f'http://{os.getenv("HOST")}'
port = os.getenv("PORT")
print(f"{host}:{port}")
w3 = Web3(Web3.HTTPProvider(f"{host}:{port}"))
print((f"\n\tRPC on: {host}:{port} ({str(w3.isConnected()).lower()})"))

chainId = int(os.getenv("CHAINID"))
account = os.getenv("DEAD_ACCOUNT_PUBLIC_KEY_1")
private_key = os.getenv("DEAD_ACCOUNT_PRIVATE_KEY_1")
print(f"\tOperating account: {account}")

# Create contract instance
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get latest transaction
nonce = w3.eth.get_transaction_count(account)
print(f"\tNonce: {nonce}\n")

# Build transaction
tx = SimpleStorage.constructor().buildTransaction(
    {"chainId": chainId, "from": account, "nonce": nonce}
)

# Sign transaction
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)

# Send signed transaction
tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(tx)
print(f"\tDeployed contract to {receipt.contractAddress}\n")

# Working with contracts
nonce = w3.eth.get_transaction_count(account)
simple_storage = w3.eth.contract(address=receipt.contractAddress, abi=abi)

# Initial value of fav number
print(f"\tFav number: {simple_storage.functions.retrieve().call()}")
tx = simple_storage.functions.store(15).buildTransaction(
    {"chainId": chainId, "from": account, "nonce": nonce}
)
signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(tx)
print(f"\tNew fav number: {simple_storage.functions.retrieve().call()}")
