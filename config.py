### **Key Files**  
**`app/core/config.py`**  
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@db:5432/appdb"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"

settings = Settings()
