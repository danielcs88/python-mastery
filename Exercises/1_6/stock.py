class Stock:
    def __init__(self, name: str, shares: int, price: float):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price

# def main():
#     pass
    

# if __name__ == "__main__":
#     main()


s = Stock("GOOG", 100, 490.1)

print(f'{s.name:10} {s.shares:10d} {s.price:10.2f}')
t = Stock("IBM", 50, 91.5)
print(t.cost())