from flask import Flask, request, jsonify, render_template
from api import get_weather_data

app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')

@app.route("/")
def index():
    """Serve the frontend HTML page."""
    return render_template("index.html")

@app.route("/weather")
def weather():
    """
    Get weather for a city.
    Query param: city (required)
    Returns: JSON with weather data or error
    """
    city = request.args.get("city", "").strip()

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    try:
        data = get_weather_data(city)

        current = data.get("currentConditions", {})
        result = {
            "city": city,
            "temperature": current.get("temp"),
            "feels_like": current.get("feelslike"),
            "conditions": current.get("conditions"),
            "humidity": current.get("humidity"),
            "wind_speed": current.get("windspeed"),
            "icon": current.get("icon"),
            "description": data.get("description", ""),
            "address": data.get("resolvedAddress", city)
        }

        return jsonify(result)

    except ValueError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": f"Failed to fetch weather: {str(e)}"}), 500

@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)