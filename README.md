# 📅 Day Order Scheduler — WCC Chennai

A Gen-Z-aesthetic Streamlit app for Women's Christian College, Chennai.
Handles the rotating Day Order I–VI system for II BBA, Semester VI (2025–26).

---

## ⚡ Quick Start

```bash
# 1. Install dependency (only one!)
pip install streamlit

# 2. Run the app
streamlit run app.py
```

Then open **http://localhost:8501** in your browser.

---

## ✨ Features

| Feature | Details |
|---|---|
| 📅 Date Picker | Select any date in the semester |
| 🔢 Day Order Badge | Shows Day I–VI (or Holiday reason) |
| 📚 Subject Cards | Full schedule for II BBA with time slots |
| 🔴 Live Slot Highlight | Highlights the currently active class (today only) |
| ➡️ Next Class Day | Quick preview of next teaching day |
| 📊 Semester Progress | % of teaching days completed |
| 🗓️ Week Glance | Toggle to see the week's day orders at a glance |

---

## 🗂️ Data Sources

- **Academic Calendar** extracted from WCC 2025–26 Semester II/IV/VI PDF
- **Timetable** extracted from November 2025 timetable image for II BBA

---

## 🎨 Tech Stack

- **Streamlit** — UI framework
- **Python stdlib only** — `datetime`, `functools` — no heavy dependencies
- **Google Fonts** — Sora + Nunito (loaded via CDN)
- **Custom CSS** — glassmorphism cards, gradient badges, hover effects
