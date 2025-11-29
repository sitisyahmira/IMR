import os
from dotenv import load_dotenv
# ... kode lainnya di atas tetap

# ==============================
# LOAD API (opsional untuk AI)
# ==============================
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY:
    from groq import Groq
    client = Groq(api_key=GROQ_API_KEY)
else:
    client = None

def generate_ai_commentary(df):
    if not client:
        return "⚠️ AI Commentary tidak aktif (API Key belum diatur)."
    summary = df[["Nama Barang", "Keuntungan"]].to_string(index=False)
    prompt = f"""
    Berikut data keuntungan tiap barang:
    {summary}

    Buat analisis singkat:
    - Barang yang paling menguntungkan
    - Barang yang merugi
    - Strategi perbaikan singkat
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"
