import os
from dotenv import load_dotenv

### Cities
# McKinney, Prosper, Selina, Frisco, Little Elm

load_dotenv()

class Config:
    LAT_MCKINNEY = os.getenv("LAT_MCKINNEY")
    LONG_MCKINNEY = os.getenv("LONG_MCKINNEY")
    LAT_PROSPER = os.getenv("LAT_PROSPER")
    LONG_PROSPER = os.getenv("LONG_PROSPER")
    LAT_CELINA = os.getenv("LAT_SELINA")
    LONG_CELINA = os.getenv("LONG_SELINA")
    LAT_FRISCO = os.getenv("LAT_FRISCO")
    LONG_FRISCO = os.getenv("LONG_FRISCO")
    LAT_LELM = os.getenv("LAT_LELM")
    LONG_LELM = os.getenv("LONG_LELM")
    KEYWORD = os.getenv("KEYWORD")
    RADIUS = os.getenv("RADIUS")
    CITIES = os.getenv("CITIES")
    API_KEY = os.getenv("API_KEY")

config = Config()