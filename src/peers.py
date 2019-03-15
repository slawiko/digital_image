import json
import asyncio

from websockets.exceptions import ConnectionClosed

class Peers():
  def __init__(self):
    self.peers = dict()

  async def register_connection(self, address, websocket, con_type):
    self.peers[address] = websocket
    print(f'Connection {con_type} {address} is registered ({websocket.local_address}:{websocket.remote_address})')
    asyncio.ensure_future(self.unregister_connection(address))

  async def unregister_connection(self, address, reason='closed'):
    await self.peers[address].wait_closed()
    del self.peers[address]
    print(f'{address} is unregistered. Reason: {reason}')
