import redis, time

r = redis.Redis(host="redis", port=6379, db=0)

while True:
    message = "Hello World!"
    r.publish("test_channel", message)
    print(f"Produced: {message}")
    time.sleep(1)