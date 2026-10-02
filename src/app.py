"""
Flask application: NIDS dashboard + JSON API.

Routes:
  GET  /                    -> dashboard page
  GET  /api/stats           -> summary stats (counts, categories, severities)
  GET  /api/activity        -> recent scored records (all traffic)
  GET  /api/alerts          -> recent flagged alerts only
  POST /api/simulator/start -> start the background traffic simulator
  POST /api/simulator/stop  -> stop it
  POST /api/clear           -> clear logs (reset demo)
"""

from pathlib import Path
from flask import Flask, render_template, jsonify, request

from logger import get_recent_activity, get_recent_alerts, get_stats, clear_logs
from simulator import TrafficSimulator

BASE_DIR = Path(__file__).resolve().parent.parent
app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)
simulator = TrafficSimulator(interval_seconds=1.5)


@app.route("/")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/stats")
def api_stats():
    return jsonify(get_stats())


@app.route("/api/activity")
def api_activity():
    limit = request.args.get("limit", 50, type=int)
    return jsonify(get_recent_activity(limit))


@app.route("/api/alerts")
def api_alerts():
    limit = request.args.get("limit", 50, type=int)
    return jsonify(get_recent_alerts(limit))


@app.route("/api/simulator/start", methods=["POST"])
def start_simulator():
    simulator.start()
    return jsonify({"status": "started"})


@app.route("/api/simulator/stop", methods=["POST"])
def stop_simulator():
    simulator.stop()
    return jsonify({"status": "stopped"})


@app.route("/api/clear", methods=["POST"])
def api_clear():
    clear_logs()
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
