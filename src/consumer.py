import redis

r = redis.Redis(host="redis", port=6379, db=0)

while True:
    pubsub = r.pubsub()
    pubsub.subscribe("test_channel")
    print("Consumer is waiting for messages...")

    for message in pubsub.listen():
        if message["type"] != "message": continue
            
        print(f"Consumed: {message["data"].decode("utf-8")}")