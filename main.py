from chain import Blockchain

# Create a new blockchain
my_blockchain = Blockchain()

# Add transactions to the pending transactions list
my_blockchain.add_transaction("Alice", "Bob", 5)
my_blockchain.add_transaction("Bob", "Charlie", 3)
my_blockchain.add_transaction("Charlie", "Alice", 2)

# Mine pending transactions and add a reward for the miner
miner_address = "Miner1"
my_blockchain.mine_pending_transactions(miner_address)

# Check balances after mining
print("Balances after mining:")
print(f"Alice: {my_blockchain.get_balance('Alice')}")
print(f"Bob: {my_blockchain.get_balance('Bob')}")
print(f"Charlie: {my_blockchain.get_balance('Charlie')}")
print(f"{miner_address}: {my_blockchain.get_balance(miner_address)}")

# Add more transactions
my_blockchain.add_transaction("Bob", "Alice", 4)
my_blockchain.add_transaction("Charlie", "Bob", 2)

# Mine pending transactions with a different miner
miner_address2 = "Miner2"
my_blockchain.mine_pending_transactions(miner_address2)

# Check balances after second mining
print("\nBalances after second mining:")
print(f"Alice: {my_blockchain.get_balance('Alice')}")
print(f"Bob: {my_blockchain.get_balance('Bob')}")
print(f"Charlie: {my_blockchain.get_balance('Charlie')}")
print(f"{miner_address}: {my_blockchain.get_balance(miner_address)}")
print(f"{miner_address2}: {my_blockchain.get_balance(miner_address2)}")

# Validate the blockchain
is_valid = my_blockchain.is_chain_valid()
print(f"\nIs the blockchain valid? {is_valid}")

# Print the blockchain
print("\nBlockchain:")
print(my_blockchain)
