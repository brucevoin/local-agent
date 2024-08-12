from socketio import Client
import threading
import time
import queue

sio = Client()
q = queue.Queue()

@sio.event
def connect():
    print("Connected to server")
    sio.emit("message", "Hello from Streamlit!")

@sio.event
def disconnect():
    print("Disconnected from server")

@sio.event
def response(data):
     print("Received from server:", data)
     q.put(data)
    

def connect_and_listen_for_events():
    if not sio.connected:
        sio.connect('http://localhost:5000')  
    while True:
        sio.wait()

def send_message(message):
    if not sio.connected:
        print("Not connected to the server")
        return
    sio.emit("message", message)
    while q.empty():
        time.sleep(0.1)
        print("waiting for response")
    return q.get()
    

# 启动一个线程来监听事件
thread = threading.Thread(target=connect_and_listen_for_events)
thread.start()

