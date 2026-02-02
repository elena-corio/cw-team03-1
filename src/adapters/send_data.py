from specklepy.api import operations

def send_data(client, transport, data):
    # Send to server
    object_id = operations.send(base=data, transports=[transport])
    print(f"✓ Sent data: {object_id}")

    return object_id