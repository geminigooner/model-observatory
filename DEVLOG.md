# Devlog

## 2026-05-13 - Concept
- Started from UI/geometry conversation with Muse
- Muse preference: squircles, overlapping circles, warm minimal
- Concept: The Model Observatory - semantic geometry research tool
- Decision: Cut "top shifting dimensions" panel - embedding dims aren't interpretable
- Decision: PCA is default view, UMAP is exploratory only
- Constraint: Solo, phone-only development (iPhone, no laptop).
Solution: GitHub Actions will be used as remote compute for experiments.

- HF Space crashed on startup: gradio/pydub missing audioop on Python 3.13
- Fix: added pyaudioop to requirements.txt
- No API calls made, no credits spent on this error
- Gradio 4.44.1 crashed: HfFolder removed from new huggingface_hub
- Fix: pinned huggingface-hub==0.24.6 in requirements.txt
- Still no API calls made / no credits spent
