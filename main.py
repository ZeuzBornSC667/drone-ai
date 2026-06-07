
from core.drone_state import DroneState
from streams.telemetry_stream import TelemetryPipeline
from dashboard.app import create_dashboard
import asyncio
import threading

def main():
    state = DroneState()
    pipeline = TelemetryPipeline(state=state)

    app, socketio = create_dashboard(state, pipeline)

    if app:
        def run():
            socketio.run(app, host="0.0.0.0", port=5000)
        threading.Thread(target=run, daemon=True).start()

    asyncio.run(pipeline.start())

if __name__ == "__main__":
    main()
