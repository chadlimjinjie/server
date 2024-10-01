import socketio

sio = socketio.AsyncServer(async_mode='asgi')
socket_app = socketio.ASGIApp(sio)