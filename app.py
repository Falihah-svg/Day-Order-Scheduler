"""
Day Order Scheduler — Women's Christian College, Chennai
Semester II / IV / VI · Academic Year 2025–26
"""

import streamlit as st
from datetime import date, timedelta
from typing import Optional, List, Tuple, Dict

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Day Order Scheduler · WCC",
    page_icon="📅",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# GLOBAL CSS  (pastel Gen-Z aesthetic)
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700;800;900&family=Sora:wght@400;600;700&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}
.stApp {
    background: linear-gradient(135deg, #f5f0ff 0%, #e8f4fd 40%, #fff0f5 100%);
    min-height: 100vh;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 760px; }

/* ── Hero header ── */
.hero {
    text-align: center;
    padding: 2.4rem 1.5rem 1.2rem;
}
.hero h1 {
    font-family: 'Sora', sans-serif;
    font-size: 2.6rem;
    font-weight: 700;
    background: linear-gradient(120deg, #a78bfa, #60a5fa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.3rem;
    line-height: 1.2;
}
.hero p {
    color: #7c6ea0;
    font-size: 1rem;
    font-weight: 500;
    margin: 0;
}

/* ── Day order badge ── */
.day-badge-wrap { text-align: center; margin: 0.5rem 0 1.2rem; }
.day-badge {
    display: inline-block;
    background: linear-gradient(135deg, #c4b5fd 0%, #93c5fd 100%);
    color: #fff;
    font-family: 'Sora', sans-serif;
    font-size: 1.65rem;
    font-weight: 700;
    padding: 0.55rem 2.2rem;
    border-radius: 50px;
    letter-spacing: 0.04em;
    box-shadow: 0 4px 18px rgba(139, 92, 246, 0.28);
}
.day-badge.holiday {
    background: linear-gradient(135deg, #fca5a5, #fcd34d);
}
.day-badge.weekend {
    background: linear-gradient(135deg, #d1d5db, #9ca3af);
}

/* ── Section label ── */
.section-label {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 0.6rem;
    text-align: center;
}

/* ── Subject card ── */
.subject-card {
    background: rgba(255,255,255,0.72);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 1rem 1.3rem;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    box-shadow: 0 2px 12px rgba(139,92,246,0.09);
    border: 1.5px solid rgba(255,255,255,0.8);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.subject-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(139,92,246,0.18);
}
.slot-chip {
    background: linear-gradient(135deg, #e9d5ff, #bfdbfe);
    color: #5b21b6;
    font-size: 0.72rem;
    font-weight: 800;
    padding: 0.25rem 0.65rem;
    border-radius: 30px;
    min-width: 2.2rem;
    text-align: center;
    letter-spacing: 0.05em;
}
.slot-chip.active {
    background: linear-gradient(135deg, #a78bfa, #60a5fa);
    color: #fff;
    box-shadow: 0 2px 10px rgba(139,92,246,0.4);
}
.subject-name {
    font-size: 1.05rem;
    font-weight: 700;
    color: #1e1b4b;
    flex: 1;
}
.subject-time {
    font-size: 0.8rem;
    color: #8b7db8;
    font-weight: 600;
}

/* ── Info cards (today / next day) ── */
.info-card {
    background: rgba(255,255,255,0.6);
    backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 1rem 1.2rem;
    border: 1.5px solid rgba(167,139,250,0.2);
    text-align: center;
    box-shadow: 0 2px 10px rgba(139,92,246,0.07);
    margin-bottom: 1rem;
}
.info-card .label { font-size: 0.72rem; font-weight: 800; letter-spacing: 0.1em; color: #a78bfa; text-transform: uppercase; }
.info-card .value { font-size: 1.4rem; font-weight: 800; color: #1e1b4b; font-family: 'Sora', sans-serif; }
.info-card .sub   { font-size: 0.82rem; color: #7c6ea0; font-weight: 500; }

/* ── Divider ── */
.soft-divider { border: none; border-top: 1.5px solid rgba(167,139,250,0.18); margin: 1.2rem 0; }

/* ── Footer ── */
.footer {
    text-align: center;
    color: #b0a0cc;
    font-size: 0.78rem;
    margin-top: 2.5rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(167,139,250,0.15);
}

/* ── Date picker label fix ── */
.stDateInput label { font-weight: 700 !important; color: #5b21b6 !important; font-size: 0.88rem !important; }
.stDateInput > div > div > input {
    border-radius: 14px !important;
    border: 1.5px solid #c4b5fd !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 600 !important;
}

/* ── Week toggle card ── */
.week-row {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 1.2rem;
}
.week-pill {
    background: rgba(255,255,255,0.65);
    border: 1.5px solid rgba(167,139,250,0.25);
    border-radius: 12px;
    padding: 0.45rem 0.9rem;
    font-size: 0.82rem;
    font-weight: 700;
    color: #5b21b6;
    text-align: center;
    min-width: 80px;
}
.week-pill.today {
    background: linear-gradient(135deg, #c4b5fd, #93c5fd);
    color: #fff;
    border-color: transparent;
    box-shadow: 0 3px 12px rgba(139,92,246,0.3);
}
.week-pill.holiday-pill {
    background: rgba(252,211,77,0.18);
    color: #92400e;
    border-color: rgba(252,211,77,0.4);
}
.week-pill.weekend-pill {
    background: rgba(209,213,219,0.3);
    color: #6b7280;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# DATA LAYER
# ─────────────────────────────────────────────

# All holidays from the calendar image
HOLIDAYS: Dict[date, str] = {
    # November 2025
    date(2025, 11, 1): "Saturday",
    # December 2025
    date(2025, 12, 2): "Govt. Declared Holiday",
    date(2025, 12, 3): "Govt. Declared Holiday",
    # January 2026
    date(2026, 1, 14): "Holiday",
    date(2026, 1, 15): "Pongal",
    date(2026, 1, 16): "Thiruvalluvar Day",
    date(2026, 1, 17): "Uzhavar Thirunal",
    date(2026, 1, 26): "Republic Day",
    # February 2026
    date(2026, 2, 6): "Sports Day",   # Saturday anyway
    date(2026, 2, 13): "Festeve",
    date(2026, 2, 14): "Festeve",
    # March 2026
    date(2026, 3, 19): "Telugu New Year",
    date(2026, 3, 31): "Mahavir Jayanti",
    # April 2026
    date(2026, 4, 3): "Good Friday",
    date(2026, 4, 14): "Tamil New Year",
}

# ESE (End Semester Exam) periods — treat as holiday/exam (no day order classes)
ESE_RANGES: List[Tuple[date, date]] = [
    (date(2025, 11, 1), date(2025, 11, 1)),    # Nov 1 (Sat)
    (date(2026, 3, 22), date(2026, 3, 30)),    # ESE block
    (date(2026, 4, 1), date(2026, 4, 2)),      # ESE continues
    (date(2026, 4, 5), date(2026, 4, 6)),      # ESE continues
]

def is_ese(d: date) -> bool:
    for start, end in ESE_RANGES:
        if start <= d <= end:
            return True
    return False

# Semester teaching period
SEMESTER_START = date(2025, 11, 3)   # First Monday of Nov 2025
SEMESTER_END   = date(2026, 4, 25)

def is_holiday(d: date) -> tuple[bool, str]:
    """Returns (is_holiday, reason)"""
    if d.weekday() >= 5:
        return True, "Weekend"
    if is_ese(d):
        return True, "Exam / ESE"
    if d in HOLIDAYS:
        return True, HOLIDAYS[d]
    if d < SEMESTER_START or d > SEMESTER_END:
        return True, "Outside semester"
    return False, ""


def build_day_order_map() -> Dict[date, int]:
    """
    Walk every weekday in the semester, skip holidays,
    and assign rolling day orders I→VI (1→6).
    """
    mapping: dict[date, int] = {}
    counter = 1          # starts at Day Order I
    current = SEMESTER_START

    while current <= SEMESTER_END:
        holiday, _ = is_holiday(current)
        if not holiday:
            mapping[current] = counter
            counter = (counter % 6) + 1
        current += timedelta(days=1)
    return mapping


@st.cache_data
def get_day_order_map() -> Dict[date, int]:
    return build_day_order_map()


def get_day_order(d: date) -> Optional[int]:
    """Returns 1-6 for a teaching day, None otherwise."""
    mapping = get_day_order_map()
    return mapping.get(d)


# ─────────────────────────────────────────────
# TIMETABLE  — II BBA
# ─────────────────────────────────────────────

TIME_SLOTS = [
    ("Slot 1", "12:30 – 1:30"),
    ("Slot 2", "1:30 – 2:30"),
    ("Slot 3", "2:45 – 3:40"),
    ("Slot 4", "3:40 – 4:35"),
    ("Slot 5", "4:35 – 5:30"),
]

SUBJECT_ICONS = {
    "MIS":       "📊",
    "BS":        "📈",
    "OB":        "🧠",
    "ACC":       "🧾",
    "LEG":       "⚖️",
    "LEGAL":     "⚖️",
    "PROD":      "🏭",
    "ME":        "🌍",
    "BE":        "💼",
    "ED":        "💡",
    "IR/AD":     "🤝",
    "IT":        "💻",
    "RES":       "🔬",
    "NME":       "📡",
    "COMP":      "🖥️",
    "LANG":      "🗣️",
    "LANGUAGE":  "🗣️",
    "ENGLISH":   "📝",
    "Scripture": "📖",
    "Assembly":  "🎙️",
    "Lab":       "🔬",
    "ENG SKB":   "✏️",
    "SKB ENG":   "✏️",
}

FULL_SUBJECT_NAMES = {
    "MIS":       "Management Information Systems",
    "BS":        "Business Statistics",
    "OB":        "Organisational Behaviour",
    "ACC":       "Accounting",
    "LEG":       "Legal Aspects of Business",
    "LEGAL":     "Legal Aspects of Business",
    "PROD":      "Production Management",
    "ME":        "Managerial Economics",
    "BE":        "Business Environment",
    "ED":        "Entrepreneurship Development",
    "IR/AD":     "Industrial Relations / Admin",
    "IT":        "Information Technology",
    "RES":       "Research Methodology",
    "NME":       "Non-Major Elective",
    "COMP":      "Computer Applications",
    "LANG":      "Language",
    "LANGUAGE":  "Language",
    "ENGLISH":   "English",
    "Scripture": "Scripture",
    "Assembly":  "Assembly",
    "Lab":       "Lab Session",
    "ENG SKB":   "English (SKB)",
    "SKB ENG":   "English (SKB)",
}

# II BBA timetable  (Day Order → list of subjects per slot)
TIMETABLE: Dict[int, List[str]] = {
    1: ["BS",       "ACC",      "—",         "PROD",     "LEG"],
    2: ["MIS",      "MIS",      "ME",        "Assembly", "Lab"],
    3: ["OB",       "LEGAL",    "ENG SKB",   "BS",       "PROD"],
    4: ["LEG",      "PROD",     "OB",        "ACC",      "LEG"],
    5: ["BS",       "BS",       "PROD",      "ACC",      "OB"],
    6: ["ACC",      "ACC",      "PROD",      "LEG",      "ENG SKB"],
}

def get_schedule(day_order: int) -> List[Tuple[str, str, str]]:
    """
    Returns list of (slot_label, time, subject) for given day order.
    """
    subjects = TIMETABLE.get(day_order, [])
    result = []
    for i, (slot_label, slot_time) in enumerate(TIME_SLOTS):
        sub = subjects[i] if i < len(subjects) else "—"
        result.append((slot_label, slot_time, sub))
    return result


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI"}

def roman(n: int) -> str:
    return ROMAN.get(n, str(n))

def get_current_slot() -> Optional[int]:
    """Returns 0-indexed slot index if we're currently in a slot, else None."""
    from datetime import datetime
    now = datetime.now()
    slot_times = [
        (12, 30, 13, 30),
        (13, 30, 14, 30),
        (14, 45, 15, 40),
        (15, 40, 16, 35),
        (16, 35, 17, 30),
    ]
    for i, (sh, sm, eh, em) in enumerate(slot_times):
        start = now.replace(hour=sh, minute=sm, second=0, microsecond=0)
        end   = now.replace(hour=eh, minute=em, second=0, microsecond=0)
        if start <= now <= end:
            return i
    return None

def next_teaching_day(from_date: date) -> Optional[Tuple[date, int]]:
    mapping = get_day_order_map()
    d = from_date + timedelta(days=1)
    for _ in range(14):
        if d in mapping:
            return d, mapping[d]
        d += timedelta(days=1)
    return None

def get_week_preview(from_date: date, n: int = 5) -> List[Tuple[date, Optional[int], str]]:
    """Return next n calendar days with day order info."""
    result = []
    d = from_date
    mapping = get_day_order_map()
    for _ in range(n):
        hol, reason = is_holiday(d)
        do = mapping.get(d)
        result.append((d, do, reason if hol else ""))
        d += timedelta(days=1)
    return result


# ─────────────────────────────────────────────
# UI COMPONENTS
# ─────────────────────────────────────────────

def render_schedule_cards(day_order: int, selected_date: date):
    schedule = get_schedule(day_order)
    today = date.today()
    current_slot = get_current_slot() if selected_date == today else None

    st.markdown('<p class="section-label">📚 Today\'s Classes — II BBA</p>', unsafe_allow_html=True)
    for i, (slot_label, slot_time, subject) in enumerate(schedule):
        if subject == "—":
            continue
        is_active = (current_slot == i)
        icon = SUBJECT_ICONS.get(subject, "📌")
        full_name = FULL_SUBJECT_NAMES.get(subject, subject)
        chip_class = "slot-chip active" if is_active else "slot-chip"
        active_badge = " 🔴 <em style='font-size:0.72rem;color:#ef4444;'>Now</em>" if is_active else ""

        st.markdown(f"""
        <div class="subject-card">
            <span class="{chip_class}">{slot_label}</span>
            <div style="flex:1">
                <div class="subject-name">{icon} {full_name}{active_badge}</div>
            </div>
            <span class="subject-time">⏰ {slot_time}</span>
        </div>
        """, unsafe_allow_html=True)


def render_week_preview(from_date: date):
    week = get_week_preview(from_date, 7)
    today = date.today()
    st.markdown('<p class="section-label">🗓️ Week at a glance</p>', unsafe_allow_html=True)
    st.markdown('<div class="week-row">', unsafe_allow_html=True)
    html = '<div class="week-row">'
    for d, do, reason in week:
        day_name = d.strftime("%a")
        day_num  = d.strftime("%d %b")
        if d.weekday() >= 5:
            css = "week-pill weekend-pill"
            label = "—"
        elif reason:
            css = "week-pill holiday-pill"
            label = "🎉"
        else:
            css = "week-pill today" if d == today else "week-pill"
            label = roman(do) if do else "—"
        html += f'<div class="{css}"><div style="font-size:0.7rem;opacity:0.7">{day_name}</div><div style="font-size:0.95rem;font-weight:800">{label}</div><div style="font-size:0.65rem;opacity:0.65">{day_num}</div></div>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# MAIN APP
# ─────────────────────────────────────────────

def main():
    today = date.today()
    mapping = get_day_order_map()

    # ── Hero ──────────────────────────────────
    st.markdown("""
    <div class="hero">
        <h1>📅 Day Order Scheduler</h1>
        <p>Women's Christian College, Chennai · II BBA · Sem VI · 2025–26</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Quick info row ─────────────────────────
    today_do   = mapping.get(today)
    next_info  = next_teaching_day(today)

    col1, col2, col3 = st.columns(3)

    with col1:
        if today_do:
            st.markdown(f"""<div class="info-card">
                <div class="label">✨ Today</div>
                <div class="value">Day {roman(today_do)}</div>
                <div class="sub">{today.strftime('%a, %d %b')}</div>
            </div>""", unsafe_allow_html=True)
        else:
            hol, reason = is_holiday(today)
            st.markdown(f"""<div class="info-card">
                <div class="label">✨ Today</div>
                <div class="value">🎉</div>
                <div class="sub">{reason or 'No classes'}</div>
            </div>""", unsafe_allow_html=True)

    with col2:
        if next_info:
            nd, ndo = next_info
            st.markdown(f"""<div class="info-card">
                <div class="label">➡️ Next Class Day</div>
                <div class="value">Day {roman(ndo)}</div>
                <div class="sub">{nd.strftime('%a, %d %b')}</div>
            </div>""", unsafe_allow_html=True)

    with col3:
        total_days = len(mapping)
        days_done  = sum(1 for d in mapping if d <= today)
        pct = int(days_done / total_days * 100) if total_days else 0
        st.markdown(f"""<div class="info-card">
            <div class="label">📊 Semester Progress</div>
            <div class="value">{pct}%</div>
            <div class="sub">{days_done} of {total_days} days done</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    # ── Date picker ────────────────────────────
    st.markdown('<p class="section-label">🗓️ Pick a Date</p>', unsafe_allow_html=True)

    col_l, col_r = st.columns([2, 1])
    with col_l:
        selected = st.date_input(
            "Select date",
            value=today,
            min_value=SEMESTER_START,
            max_value=SEMESTER_END,
            label_visibility="collapsed",
        )

    # ── Day order badge ────────────────────────
    selected_do = get_day_order(selected)
    hol, hol_reason = is_holiday(selected)

    if selected_do:
        badge_class = "day-badge"
        badge_text  = f"Day Order &nbsp;·&nbsp; {roman(selected_do)}"
    elif hol:
        badge_class = "day-badge holiday"
        badge_text  = f"🎉 {hol_reason}"
    else:
        badge_class = "day-badge weekend"
        badge_text  = "No Classes"

    st.markdown(f"""
    <div class="day-badge-wrap">
        <span class="{badge_class}">{badge_text}</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Schedule cards ─────────────────────────
    if selected_do:
        render_schedule_cards(selected_do, selected)

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    # ── Week preview toggle ────────────────────
    show_week = st.toggle("🗓️ Show week at a glance", value=True)
    if show_week:
        # Start from Monday of the selected week
        week_start = selected - timedelta(days=selected.weekday())
        render_week_preview(week_start)

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    # ── Today's full schedule shortcut ─────────
    if today_do and selected != today:
        with st.expander("⚡ Jump to Today's Schedule"):
            render_schedule_cards(today_do, today)

    # ── Footer ────────────────────────────────
    st.markdown("""
    <div class="footer">
        Built with ✨ for II BBA, WCC Chennai &nbsp;·&nbsp;
        Day orders sourced from Academic Calendar 2025–26 &nbsp;·&nbsp;
        <em>Not an official college tool</em>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()