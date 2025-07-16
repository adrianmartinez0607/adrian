import streamlit as st
from PIL import Image

# Define courses and their holes with yardages

courses = {
"Coyote Moon": {
"holes": \[
{"number": i, "image": f"hole{i}.jpg", "yardage": \[485, 365, 190, 410, 330, 380, 195, 540, 425,
365, 185, 400, 425, 190, 525, 355, 175, 510]\[i-1]}
for i in range(1, 19)
]
},
"Grays Crossing": {
"holes": \[
{"number": i, "image": f"grays{i}.jpg", "yardage": \[405, 375, 585, 165, 420, 325, 580, 185, 455,
395, 205, 420, 435, 340, 535, 175, 410, 555]\[i-1]}
for i in range(1, 19)
]
}
}

# Sidebar: Course and Hole selection

st.sidebar.title("Golf Course Guide")
selected\_course = st.sidebar.selectbox("Select Course", list(courses.keys()))
hole\_numbers = \[f"Hole {h\['number']}" for h in courses\[selected\_course]\["holes"]]
selected\_hole\_label = st.sidebar.selectbox("Select Hole", hole\_numbers)
selected\_hole\_index = hole\_numbers.index(selected\_hole\_label)
hole = courses\[selected\_course]\["holes"]\[selected\_hole\_index]

# Load and display image

try:
image = Image.open(hole\['image'])
st.image(image, caption=f"{selected\_course} - Hole {hole\['number']}", use\_column\_width=True)
except Exception as e:
st.warning(f"Image for Hole {hole\['number']} not found.")

# Yardage display

st.markdown(f"📏 **Yardage:** {hole\['yardage']} yards")

# Hole descriptions (White Tees for Coyote Moon, full Grays Crossing)

descriptions = {
\# Grays Crossing holes 10–18 with expanded tips
("Grays Crossing", 10): {
"overview": "📍 **Overview:** Tight tee shot into prevailing wind on this long par 4. Accuracy matters.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Thread it between right bunkers. A 250-yard tee shot should clear them and set up a mid-iron approach.",
"approach": "🎯 **Approach Game:** With wind helping, club down for your second shot — the green slopes subtly from back to front.",
"tip": "💡 **Tee Tip:** Use a 3W or controlled driver. Middle of green is smart."},

```
("Grays Crossing", 11): {
    "overview": "📍 **Overview:** Narrow and deep par 3 green protected by a nasty left bunker.",
    "tee_shot": "🎯 **Tee Shot Strategy:** Aim center-right. The slope will feed your ball left.",
    "approach": "🎯 **Approach Game:** Best to land middle and let it release back.",
    "tip": "💡 **Tee Tip:** Play a full club — short gets punished."},

("Grays Crossing", 12): {
    "overview": "📍 **Overview:** Classic par 4 with wide fairway and guarded green.",
    "tee_shot": "🎯 **Tee Shot Strategy:** Favor the left side off the tee to open up a clean angle.",
    "approach": "🎯 **Approach Game:** Bunkers guard both sides — fly it in high.",
    "tip": "💡 **Tee Tip:** Be aggressive only if you're inside 130 yards."},

("Grays Crossing", 13): {
    "overview": "📍 **Overview:** Water hugs the right from tee to green — one of the most intimidating holes.",
    "tee_shot": "🎯 **Tee Shot Strategy:** A 230-yard drive aimed safely left avoids danger.",
    "approach": "🎯 **Approach Game:** Avoid short siding yourself. Take enough club to clear the water.",
    "tip": "💡 **Tee Tip:** Par here beats the field — don’t be the hero."},

("Grays Crossing", 14): {
    "overview": "📍 **Overview:** Short and driveable par 4 — pure risk/reward.",
    "tee_shot": "🎯 **Tee Shot Strategy:** Long hitters can go for it (~300 yards); others should aim right of bunkers.",
    "approach": "🎯 **Approach Game:** Elevated green with subtle slopes. Precision counts.",
    "tip": "💡 **Tee Tip:** If you lay up, leave a full wedge (~100 yds)."},

("Grays Crossing", 15): {
    "overview": "📍 **Overview:** Reachable par 5 with risk on second shot.",
    "tee_shot": "🎯 **Tee Shot Strategy:** Aim right-center to avoid the left slope.",
    "approach": "🎯 **Approach Game:** Front of green slopes hard — fly it pin-high.",
    "tip": "💡 **Tee Tip:** Use 3-shot strategy unless you’re inside 230 yds on second."},

("Grays Crossing", 16): {
    "overview": "📍 **Overview:** Short downhill par 3 that plays 10–15 yards less.",
    "tee_shot": "🎯 **Tee Shot Strategy:** Pick your landing spot and swing smooth.",
    "approach": "🎯 **Approach Game:** Anything short-middle feeds to the pin.",
    "tip": "💡 **Tee Tip:** Don’t overthink club selection."},

("Grays Crossing", 17): {
    "overview": "📍 **Overview:** Downwind par 4 with firm, fast green.",
    "tee_shot": "🎯 **Tee Shot Strategy:** Avoid running through fairway by aiming left of bunker.",
    "approach": "🎯 **Approach Game:** A high approach is needed to hold this green.",
    "tip": "💡 **Tee Tip:** Land it short and let it release."},

("Grays Crossing", 18): {
    "overview": "📍 **Overview:** Strong closing par 5 with dual fairway options.",
    "tee_shot": "🎯 **Tee Shot Strategy:** Safe play is right-center; long hitters can cross to left fairway.",
    "approach": "🎯 **Approach Game:** Avoid the right hazard on second. Green is narrow.",
    "tip": "💡 **Tee Tip:** Commit to your layup yardage — wedge control wins here."}
```

}

# Display strategy

desc = descriptions.get((selected\_course, hole\['number']))
if desc:
st.markdown(f"""
\### 🧠 Hole {hole\['number']} – Strategy & Tips
{desc\['overview']}

```
    {desc['tee_shot']}

    {desc['approach']}

    {desc['tip']}
""")
```

else:
st.info("Strategy info not yet available for this hole.")
