from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json, os, re
from dotenv import load_dotenv
import anthropic

load_dotenv()

app = Flask(__name__)
CORS(app)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# ─────────────────────────────────────────────
#  Serve Frontend
# ─────────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route("/static/<path:path>")
def serve_static(path):
    return send_from_directory('../frontend/static', path)

# ─────────────────────────────────────────────
#  API: Fashion Recommendation
# ─────────────────────────────────────────────
@app.route("/api/recommend", methods=["POST"])
def recommend():
    data        = request.get_json()
    category    = data.get("category", "general")
    weather     = data.get("weather", "")
    skin_tone   = data.get("skin_tone", "")
    body_shape  = data.get("body_shape", "")
    occasion    = data.get("occasion", "")
    gender      = data.get("gender", "unspecified")
    budget      = data.get("budget", "mid-range")
    style_pref  = data.get("style_pref", "")
    extra_notes = data.get("extra_notes", "")

    prompt = build_prompt(category, weather, skin_tone, body_shape,
                          occasion, gender, budget, style_pref, extra_notes)

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )
    response_text = message.content[0].text

    try:
        json_match = re.search(r"```json\s*(.*?)\s*```", response_text, re.DOTALL)
        result = json.loads(json_match.group(1)) if json_match else json.loads(response_text)
    except Exception:
        result = {"raw": response_text}

    return jsonify({"success": True, "recommendation": result})


# ─────────────────────────────────────────────
#  Prompt Builder
# ─────────────────────────────────────────────
def build_prompt(category, weather, skin_tone, body_shape,
                 occasion, gender, budget, style_pref, extra_notes):

    base = f"""You are a world-class AI fashion stylist. Return ONLY a JSON object inside a ```json block.
Gender: {gender} | Budget: {budget} | Style preference: {style_pref or 'any'}
Extra notes: {extra_notes or 'none'}\n\n"""

    schemas = {
        "weather": f"""Weather condition: {weather}. Recommend 2 complete outfits suited for this weather.
```json
{{
  "category": "Weather-Based",
  "weather": "{weather}",
  "outfits": [
    {{"name": "...", "top": "...", "bottom": "...", "footwear": "...", "accessories": "...", "tip": "..."}},
    {{"name": "...", "top": "...", "bottom": "...", "footwear": "...", "accessories": "...", "tip": "..."}}
  ],
  "color_palette": ["color1", "color2", "color3"],
  "fabrics": ["fabric1", "fabric2"],
  "avoid": ["item1", "item2"]
}}
```""",

        "skin_tone": f"""Skin tone: {skin_tone}. Recommend colors and outfits that complement this complexion.
```json
{{
  "category": "Skin Tone Based",
  "skin_tone": "{skin_tone}",
  "best_colors": ["c1", "c2", "c3", "c4"],
  "avoid_colors": ["c1", "c2"],
  "outfits": [
    {{"name": "...", "description": "...", "colors_used": ["..."], "why_it_works": "..."}},
    {{"name": "...", "description": "...", "colors_used": ["..."], "why_it_works": "..."}}
  ],
  "patterns": ["p1", "p2"],
  "makeup_tip": "..."
}}
```""",

        "body_shape": f"""Body shape: {body_shape}. Recommend flattering outfits for this figure.
```json
{{
  "category": "Body Shape Based",
  "body_shape": "{body_shape}",
  "styling_goal": "...",
  "outfits": [
    {{"name": "...", "top": "...", "bottom": "...", "silhouette_tip": "..."}},
    {{"name": "...", "top": "...", "bottom": "...", "silhouette_tip": "..."}}
  ],
  "best_cuts": ["cut1", "cut2", "cut3"],
  "avoid": ["item1", "item2"],
  "pro_tip": "..."
}}
```""",

        "gym": f"""Gym/Workout outfit recommendations for {gender}.
```json
{{
  "category": "Gym & Workout",
  "outfits": [
    {{"name": "...", "top": "...", "bottom": "...", "footwear": "...", "accessories": "...", "best_for": "..."}},
    {{"name": "...", "top": "...", "bottom": "...", "footwear": "...", "accessories": "...", "best_for": "..."}}
  ],
  "fabrics": ["fabric1", "fabric2"],
  "color_palette": ["c1", "c2", "c3"],
  "performance_tips": ["tip1", "tip2"],
  "brands_to_explore": ["brand1", "brand2", "brand3"]
}}
```""",

        "occasion": f"""Occasion: {occasion}. Provide a complete outfit guide.
```json
{{
  "category": "Occasion Based",
  "occasion": "{occasion}",
  "dress_code": "...",
  "outfits": [
    {{"name": "...", "top": "...", "bottom": "...", "footwear": "...", "accessories": "...", "vibe": "..."}},
    {{"name": "...", "top": "...", "bottom": "...", "footwear": "...", "accessories": "...", "vibe": "..."}}
  ],
  "color_palette": ["c1", "c2", "c3"],
  "styling_dos": ["do1", "do2"],
  "styling_donts": ["dont1", "dont2"]
}}
```""",

        "accessories": f"""Accessories recommendation for context: {occasion or style_pref or 'everyday'}.
Skin tone: {skin_tone or 'not specified'}.
```json
{{
  "category": "Accessories",
  "context": "...",
  "jewelry": [{{"item": "...", "why": "..."}}],
  "bags":    [{{"item": "...", "why": "..."}}],
  "footwear":[{{"item": "...", "why": "..."}}],
  "headwear":[{{"item": "...", "why": "..."}}],
  "eyewear": [{{"item": "...", "why": "..."}}],
  "pro_tip": "..."
}}
```""",
    }

    return base + schemas.get(category, schemas["occasion"])


if __name__ == "__main__":
    print("🚀 VOGUE·AI Backend running at http://localhost:5000")
    app.run(debug=True, port=5000)
