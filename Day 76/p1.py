import datetime

class LogWriter:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'a')
        return self

    def log(self, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.file.write(f"[{timestamp}] {message}\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

print("Writing entries to log.txt...")

with LogWriter('Day 76/log.txt') as logger:
    logger.log("Application has started.")
    logger.log("Processing data batch #1.")
    logger.log("Processing complete.")

print("Finished writing logs.")