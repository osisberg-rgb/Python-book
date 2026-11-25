from pathlib import Path
import json

path = Path('favorite_numbers.json')
content = path.read_text()
favNum = json.loads(content)

print(f"Your favorite numbers are {favNum}")

