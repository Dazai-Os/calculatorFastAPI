from core.config import load_config
from models.postgresql import Database

#create global variables
config = load_config(".env")
db = Database()