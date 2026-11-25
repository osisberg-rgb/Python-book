from pathlib import Path
import json

favNum = input("What is your favorite number")

path = Path('favorite_numbers.json')
content = json.dumps(favNum)
path.write_text(content)