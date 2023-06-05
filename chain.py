from block import Block, Transaction
import time

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.reward_amount = 1
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, "01/01/2023", [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        block = Block(len(self.chain), time.time(), self.pending_transactions, self.get_latest_block().hash)
        block.mine_block(self.difficulty, miner_address, self.reward_amount)

        self.chain.append(block)
        self.pending_transactions = []

    def add_transaction(self, sender, receiver, amount):
        transaction = Transaction(sender, receiver, amount)
        self.pending_transactions.append(transaction)

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender == address:
                    balance -= transaction.amount
                if transaction.receiver == address:
                    balance += transaction.amount
        return balance

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        chain_info = ""
        for block in self.chain:
            chain_info += str(block) + "\n\n"
        return chain_info
