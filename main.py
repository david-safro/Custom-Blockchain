from chain import Blockchain
from block import Block
# Create a new blockchain
glitchez_coin = Blockchain()

# Add blocks to the blockchain
block1 = Block(1, "02/01/2023", "Block 1 Data", "")
glitchez_coin.add_block(block1)

block2 = Block(2, "03/01/2023", "Block 2 Data", "")
glitchez_coin.add_block(block2)

# Print the blockchain details
print("Blockchain:")
print(glitchez_coin)

# Validate the blockchain
is_valid = glitchez_coin.is_chain_valid()
print(f"\nIs the blockchain valid? {is_valid}")
