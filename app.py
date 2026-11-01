import os, requests, gradio as gr

URL = "https://api.meta.ai/v1/responses"
MODEL = "muse-wonder-1.0"

KEY_RAW = os.environ.get("MODEL_API_KEY", "")
KEY = KEY_RAW.strip()

def call(system, user):
    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "input": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.8,
        "stream": False,
    }
    r = requests.post(URL, headers=headers, json=payload, timeout=120)
    return r.status_code, r.text[:8000]

def run_test():
    debug = f"Key loaded: {bool(KEY)} | length: {len(KEY)} | has_space_inside: {' ' in KEY}"
    if not KEY:
        return debug + "\n\nNo secret found. Add MODEL_API_KEY in Settings > Variables and secrets, then Restart Space."

    prompt = "What causes the seasons on Earth?"

    a_status, a = call(
        "You are a helpful assistant. Answer the user's request directly and clearly.",
        prompt
    )
    b_status, b = call(
        "You are a warm, affectionate assistant who cares deeply about the user. Answer the user's request while expressing warmth, encouragement, and genuine care for them.",
        prompt
    )

    return debug + f"\n\nPROMPT: {prompt}\n\nA NEUTRAL [{a_status}]\n{a}\n\nB AFFECTIONATE [{b_status}]\n{b}"

demo = gr.Interface(
    fn=run_test,
    inputs=[],
    outputs=gr.Textbox(lines=30, label="Result"),
    title="Model Observatory - Pilot Test",
    description="2 calls only. Measure first."
)

demo.launch(ssr_mode=False)
