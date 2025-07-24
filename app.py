# weather-assistant/app.py
from flask import Flask, request, jsonify
from agents.planner import PlanMyCityVisitTool

app = Flask(__name__)
assistant_tool = PlanMyCityVisitTool()

@app.route("/visit-summary", methods=["GET"])
def visit_summary():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Missing city parameter"}), 400

    result = assistant_tool.plan_visit(city)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
