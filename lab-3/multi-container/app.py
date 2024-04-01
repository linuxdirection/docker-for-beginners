from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis container
# Assuming the default hostname of the Redis service in your docker-compose.yml is 'redis'
redis_client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def hello():
    # Increment the visit count stored in Redis
    visit_count = redis_client.incr('visit_count')
    return f"Hello, World! This page has been visited {visit_count} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0')
