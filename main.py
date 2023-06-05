from chain import Blockchain

Miner1_name = "Stephen J Satalino"
Miner2_name = "Stephanie Trainer"
Miner3_name = "Ian :P <3"
# Create a new blockchain
glitchez_coin = Blockchain()

# Add transactions to the pending transactions list
glitchez_coin.add_transaction(Miner2_name, Miner1_name, 5)
glitchez_coin.add_transaction(Miner1_name, Miner3_name, 3)
glitchez_coin.add_transaction(Miner3_name, Miner2_name, 2)

# Mine pending transactions and add a reward for the miner
miner_address = "Miner1"
glitchez_coin.mine_pending_transactions(miner_address)

# Check balances after mining
print(f'''Balances after mining:
{Miner2_name}: {glitchez_coin.get_balance(Miner2_name)}
"{Miner1_name}: {glitchez_coin.get_balance(Miner1_name)}
{Miner3_name}: {glitchez_coin.get_balance(Miner3_name)}
{miner_address}: {glitchez_coin.get_balance(miner_address)}''')

# Add more transactions
glitchez_coin.add_transaction(Miner1_name, Miner2_name, 4)
glitchez_coin.add_transaction(Miner3_name, Miner1_name, 2)

# Mine pending transactions with a different miner
miner_address2 = "Miner2"
glitchez_coin.mine_pending_transactions(miner_address2)

# Check balances after second mining
print(f'''\nBalances after second mining:
{glitchez_coin.get_balance(Miner2_name)}
{glitchez_coin.get_balance(Miner1_name)}
{Miner3_name}: {glitchez_coin.get_balance(Miner3_name)}
{miner_address}: {glitchez_coin.get_balance(miner_address)}
{miner_address2}: {glitchez_coin.get_balance(miner_address2)}''')

# Validate the blockchain
is_valid = glitchez_coin.is_chain_valid()
print(f"\nIs the blockchain valid? {is_valid}")

# Print the blockchain
print(f"\nBlockchain: \n{glitchez_coin}")
