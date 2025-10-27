from pathlib import Path
from typing import Union
from collections import Counter
import sys


def load_logs(file_path: str) -> Union[list[dict], None]:
    log_file_path = Path(file_path).absolute()

    # Return None if path does not exist
    if not log_file_path.exists():
        return None

    # Append logs to the list and handle exceptions while reading
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                parsed = parse_log_line(line)
                if parsed:
                    logs.append(parsed)
    except Exception as e:
        print(f"Error reading file: {e}")
    return logs

    # # Optional with generator:
    # def yield_lines() -> Iterator[dict]:

    #     with open(file_path, "r", encoding="utf-8") as file:
    #         for line in file:
    #             parsed_line = parse_log_line(line)
    #             yield parsed_line

    # # return list of yielded parsed lines
    # return list(yield_lines())


def parse_log_line(line: str) -> Union[dict, None]:
    # Return dict with splitted components
    try:
        date, time, level, *message = line.strip().split(" ")
        return {
            "date": date,
            "time": time,
            "level": level,
            "message": (" ").join(message),
        }
    # Skip the line with wrong data format
    except ValueError:
        return None


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level.upper(), logs))
    # return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    return Counter(log["level"] for log in logs)


def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| { count}")


def main():

    # Check if path [and level] was typed
    if len(sys.argv) < 2:
        print("Usage: python read_log.py /path/to/logfile.log [LEVEL]")
        return

    log_file = sys.argv[1]
    logs = load_logs(log_file)

    if logs is None:
        print(f"File not found: {Path(log_file).absolute()}")
        return
    elif not logs:
        print("There are no logs")
        return

    # Count and display statistics
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Show logs for a certain level if there is a 2nd argument
    if len(sys.argv) >= 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)

        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nНе знайдено логів для рівня '{level.upper()}'")


if __name__ == "__main__":
    main()
