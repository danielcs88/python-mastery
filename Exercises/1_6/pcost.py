def open_input(filename: str):
    return open(filename, encoding="utf8").read()


def solution(portfolio_file: str) -> float:
    portfolio = [line.split() for line in open_input(portfolio_file).split("\n")][:-1]
    return sum(int(share[1]) * float(share[2]) for share in portfolio)


def main():
    print(solution("../../Data/portfolio.dat"))
    print(solution("../../Data/portfolio2.dat"))


if __name__ == "__main__":
    main()
