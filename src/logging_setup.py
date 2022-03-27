import logging

logging.basicConfig(
    format="%(asctime)s => %(filename)s => %(levelname)s => %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="log.txt",
    level=logging.DEBUG
)

# Error and critical logs we will write to console
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console_formatter = logging.Formatter("%(asctime)s => %(filename)s => %(levelname)s => %(message)s")
console.setFormatter(console_formatter)

# And also, to another file
file = logging.FileHandler(filename="important_logs.txt")
file.setLevel(logging.ERROR)
file_formatter = logging.Formatter("%(asctime)s => %(filename)s => %(levelname)s => %(message)s")
console.setFormatter(file_formatter)

# Getting root logger
root_logger = logging.getLogger("")

root_logger.addHandler(console)
root_logger.addHandler(file)


class DrawFilter(logging.Filter):
    def filter(self, record):
        return not (record.msg.startswith("Battle") and record.msg.endswith("0"))


root_logger.addFilter(DrawFilter())
