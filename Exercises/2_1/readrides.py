# readrides.py
import csv
from collections import namedtuple


class Row_class:
    def __init__(self, route: str, date: str, daytype: str, rides: int):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class Row_class_w_slot:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route: str, date: str, daytype: str, rides: int):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


Row_named_tuple = namedtuple("Row_named_tuple", ["route", "date", "daytype", "rides"])


def read_data(filename: str):
    return csv.reader(open(filename))


def option_for_data(option: str, route: str, date: str, daytype: str, rides: int):
    return {
        "dict": {"route": route, "date": date, "daytype": daytype, "rides": rides},
        "namedtuple": Row_named_tuple(route, date, daytype, rides),
        "class": Row_class(route, date, daytype, rides),
        "slot_class": Row_class_w_slot(route, date, daytype, rides),
    }[option]


def process_rides(data_rows, option: str):
    """
    Read the bus ride data as a lit of tuples
    """

    records = []
    _ = next(data_rows)  # Skip headers
    for row in data_rows:
        route = row[0]
        date = row[1]
        daytype = row[2]
        rides = int(row[3])
        record = option_for_data(option, route, date, daytype, rides)
        records.append(record)
        return records


def tracemalloc_diag(option: str):
    import tracemalloc

    tracemalloc.start()
    data = read_data("../../Data/ctabus.csv")
    rows = process_rides(data, option)
    print(
        f"Memory Use: Current {tracemalloc.get_traced_memory()[0]}, Peak {tracemalloc.get_traced_memory()[1]}"
    )


if __name__ == "__main__":
    for o in ["dict", "namedtuple", "class", "slot_class"]:
        print(o)
        tracemalloc_diag(o)
