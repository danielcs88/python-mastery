def open_input(filename: str):
    return open(filename, encoding='utf8').read()

def solution() -> float:
    portfolio = [line.split() for line in open_input("../Data/portfolio.dat").split("\n")][:-1]
    return sum(int(share[1]) * float(share[2])  for share in portfolio)

def main():
    print(solution())

if __name__ == "__main__":
    main()