from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# ─── Debug info on startup ────────────────────────────────────────────────────
print("=" * 60)
print(f"✅ Flask running from folder: {os.getcwd()}")
templates_path = os.path.join(os.getcwd(), 'templates')
print(f"👉 Flask expects templates in:  {templates_path}")
print(f"👉 Does templates folder exist? {os.path.exists(templates_path)}")
if os.path.exists(templates_path):
    print(f"👉 Files inside templates:      {os.listdir(templates_path)}")
print("=" * 60)


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    return open("index.html", encoding="utf-8").read()


@app.route('/recommend', methods=['POST'])
def recommend():
    user_data = {
        'name':       request.form.get('name'),
        'gender':     request.form.get('gender'),
        'weather':    request.form.get('weather'),
        'skin_tone':  request.form.get('skin_tone'),   # ✅ fixed: was 'skinTone'
        'body_shape': request.form.get('body_shape'),
        'occasion':   request.form.get('occasion'),
    }

    from recommendation_engine import get_recommendations
    results = get_recommendations(user_data)

    # render_template_string is now imported ✅
    return render_template_string(
        open("result.html", encoding="utf-8").read(),
        user=user_data,
        results=results
    )


# ─── Run ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    # host='0.0.0.0' makes the app reachable from your phone on the same Wi-Fi
    app.run(host='0.0.0.0', port=5000, debug=True)