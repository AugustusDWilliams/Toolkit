from pathlib import Path

server = r"\\chemdaqserver\departments"
server = r"Z:"
share = r"Users/Dan Williams"
filename = "test.txt"

path = Path(server, share, filename)
print(path.exists())
print(path)