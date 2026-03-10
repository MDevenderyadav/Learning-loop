# VOGUE·AI — Fashion Intelligence System

> An AI-powered fashion recommendation system built with Python (Flask) + HTML/CSS/JS, powered by Claude AI.

---

## Features

| Category       | What it recommends                                      |
|----------------|---------------------------------------------------------|
| 🌤 Weather      | Outfits matched to temperature & weather conditions     |
| 🎨 Skin Tone    | Color palettes & outfits that flatter your complexion   |
| ✦ Body Shape   | Silhouettes & cuts that enhance your figure             |
| 🏋️ Gym          | Performance + style for every workout type              |
| 🎭 Occasion     | Perfect looks for any event or dress code               |
| 💍 Accessories  | Jewelry, bags, footwear & eyewear curation              |

---

## Project Structure

```
fashion-ai/
├── backend/
│   ├── app.py              ← Flask API server
│   ├── requirements.txt    ← Python dependencies
│   ├── .env.example        ← Environment template
│   └── .env                ← Your API key (create this, never commit)
├── frontend/
│   ├── index.html          ← Complete single-file UI
│   └── static/
│       ├── css/            ← Optional extracted CSS
│       ├── js/             ← Optional extracted JS
│       └── images/         ← Brand assets
├── .gitignore
└── README.md
```

---

## Setup & Run

### Step 1 — Install Python dependencies

```bash
cd backend
python -m venv venv

# Activate virtual environment:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### Step 2 — Set your API key

```bash
# Copy the example file
cp .env.example .env

# Edit .env and replace with your real key:
# ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

Get your free API key at: https://console.anthropic.com

### Step 3 — Start the Flask backend

```bash
python app.py
# Server starts at http://localhost:5000
```

### Step 4 — Open the frontend

Open `frontend/index.html` in your browser  
**or** visit `http://localhost:5000`

---

## API Reference

**Endpoint:** `POST /api/recommend`

**Request body:**
```json
{
  "category":    "weather | skin_tone | body_shape | gym | occasion | accessories",
  "weather":     "sunny and hot, temperature 25–35°C, activity: everyday casual",
  "skin_tone":   "medium / olive with warm undertone",
  "body_shape":  "hourglass, height: average",
  "occasion":    "wedding guest",
  "gender":      "women",
  "budget":      "mid-range",
  "style_pref":  "classic & timeless",
  "extra_notes": "any additional context"
}
```

**Response:**
```json
{
  "success": true,
  "recommendation": {
    "category": "Weather-Based",
    "outfits": [...],
    "color_palette": [...],
    "fabrics": [...],
    "avoid": [...]
  }
}
```

---

## Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Python 3.10+, Flask, Flask-CORS
- **AI:** Anthropic Claude (claude-sonnet-4-20250514)
- **Fonts:** Cormorant Garamond + Montserrat (Google Fonts)

---

## Security Notes

- Never commit your `.env` file
- Never expose your API key in frontend code
- The `.gitignore` is pre-configured to exclude `.env`

---

© 2025 VOGUE·AI — All recommendations are AI-generated
