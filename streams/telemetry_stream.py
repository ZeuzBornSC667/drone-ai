
import asyncio

class TelemetryPipeline:
    def __init__(self, state):
        self.state = state
        self._running = False

    async def start(self):
        self._running = True
        while self._running:
            self.state.frame_id += 1
            await asyncio.sleep(1/30)
