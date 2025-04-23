import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "30"))

DEVS = list(map(int, os.getenv("DEVS", "5937391590").split()))

API_ID = int(os.getenv("API_ID", "26181769"))

API_HASH = os.getenv("API_HASH", "4bf6bf35c4700023a2d1d5f48562f303")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7915079265:AAFyj0V5G2n7vwZ0ZyhlYuu8OOs-Do4oMTE")

OWNER_ID = int(os.getenv("OWNER_ID", "5937391590"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002419662880").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Ipanndongok:Ipanndongok@ipanndongok.bg7xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002614879090"))
