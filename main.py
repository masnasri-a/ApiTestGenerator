from core import Core
from generator import GenAuth

base_dir = 'tests'
# Generate a auth
auth = GenAuth(base_dir)
print(auth)

# path_file = 'api-partner.json'
path_file = 'example-api.json'
logic = Core(path_file, base_dir)
logic.run()
