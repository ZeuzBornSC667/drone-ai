
from dashboard.app import create_dashboard
from core.state import DroneState
from streams.telemetry_stream import TelemetryPipeline

state = DroneState()
pipeline = TelemetryPipeline(state)
app, socketio = create_dashboard(state, pipeline)

if app:
    socketio.run(app, host='0.0.0.0', port=5000)
