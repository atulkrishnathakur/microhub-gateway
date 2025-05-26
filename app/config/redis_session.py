from app.config.redis import get_redis
import json

class RedisSession:
    def __init__(self):
        self.redis_client = get_redis()

    def set_session(self, session_key: str, data: dict):
        json_data = json.dumps(data)  # Convert dictionary to JSON string
        self.redis_client.set(session_key, json_data)

    def get_session(self, session_key: str):
        data = self.redis_client.get(session_key)
        return json.loads(data) if data else None  # Convert JSON back to dictionary
