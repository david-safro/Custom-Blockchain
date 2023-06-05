import hashlib
import time


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount


class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.transactions).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.nonce).encode('utf-8'))
        return sha.hexdigest()

    def mine_block(self, difficulty, reward_address, reward_amount):
        target = "0" * difficulty
        reward_transaction = Transaction("System", reward_address, reward_amount)
        self.transactions.append(reward_transaction)
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        transaction_info = "\n".join(
            [f"Sender: {tx.sender}, Receiver: {tx.receiver}, Amount: {tx.amount}" for tx in self.transactions]
        )
        return f"Block #{self.index}\nTimestamp: {self.timestamp}\nTransactions:\n{transaction_info}\nPrevious Hash: {self.previous_hash}\nNonce: {self.nonce}\nHash: {self.hash}"
