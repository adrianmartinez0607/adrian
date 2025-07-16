import streamlit as st
from PIL import Image

# Define courses and their holes with yardages and tips

courses = {
"Coyote Moon": {
"holes": \[
{"number": 1, "image": "hole1.jpg", "yardage": 485,
"overview": "📝 **Overview:** A dramatic opening par 5 with an elevated tee shot and generous fairway.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Aim slightly right-center. From the white tees (\~485 yards), most players should play for position rather than try to reach in two.",
"approach": "🔍 **Approach Game:** A layup short of the hazard sets up a wedge to a slightly elevated green.",
"tip": "💡 **Tee Tip:** Don’t get greedy—start the round with a smart par or birdie chance."},
{"number": 2, "image": "hole2.jpg", "yardage": 365,
"overview": "📝 **Overview:** A sharp dogleg left par 4 that rewards accuracy over power.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor a 200-220 yard tee shot down the middle-left to avoid running through the fairway.",
"approach": "🔍 **Approach Game:** A short to mid iron remains. Be aware of the elevated green.",
"tip": "💡 **Tee Tip:** Use a hybrid or long iron to control placement."},
{"number": 3, "image": "hole3.jpg", "yardage": 190,
"overview": "📝 **Overview:** A picturesque par 3 over water.",
"tee\_shot": "🎯 **Tee Shot Strategy:** At 190 yards, club up if wind is into you. Favor the right side.",
"approach": "🔍 **Approach Game:** Bail out short or right is safe—avoid the water left.",
"tip": "💡 **Tee Tip:** Don’t get too aggressive—middle of the green is your friend."},
{"number": 4, "image": "hole4.jpg", "yardage": 410,
"overview": "📝 **Overview:** Blind tee shot on this strong par 4.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Trust your line over the tree and aim just right of center.",
"approach": "🔍 **Approach Game:** Uphill second shot plays 5–10 yards longer.",
"tip": "💡 **Tee Tip:** Walk up and visualize if unsure off the tee."},
{"number": 5, "image": "hole5.jpg", "yardage": 330,
"overview": "📝 **Overview:** Short risk/reward par 4.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Lay up with long iron or try to drive green if wind is helping.",
"approach": "🔍 **Approach Game:** Precise wedge needed — narrow green.",
"tip": "💡 **Tee Tip:** Play to your strength — driver not always best."},
{"number": 6, "image": "hole6.jpg", "yardage": 380,
"overview": "📝 **Overview:** Demanding tee shot with trouble left.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor right side to stay away from water.",
"approach": "🔍 **Approach Game:** Mid-iron to slightly elevated green.",
"tip": "💡 **Tee Tip:** Avoid left at all costs."},
{"number": 7, "image": "hole7.jpg", "yardage": 195,
"overview": "📝 **Overview:** Long par 3 with tough carry.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Bunker short right is common miss — aim center.",
"approach": "🔍 **Approach Game:** Club up if wind is present.",
"tip": "💡 **Tee Tip:** Trust a high, soft landing shot."},
{"number": 8, "image": "hole8.jpg", "yardage": 540,
"overview": "📝 **Overview:** Signature par 5 with stunning elevation drop.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Let it rip! Massive fairway.",
"approach": "🔍 **Approach Game:** Lay up to flat zone or go for green if downhill lie is favorable.",
"tip": "💡 **Tee Tip:** Stay below the hole for your third."},
{"number": 9, "image": "hole9.jpg", "yardage": 425,
"overview": "📝 **Overview:** Long uphill par 4.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Must carry ridge — driver essential.",
"approach": "🔍 **Approach Game:** Uphill target plays longer.",
"tip": "💡 **Tee Tip:** Err short — long misses are dead."},
{"number": 10, "image": "hole10.jpg", "yardage": 365,
"overview": "📝 **Overview:** Elevated tee with slight dogleg.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Aim for right half with a fade.",
"approach": "🔍 **Approach Game:** Short wedge, but green can be slippery.",
"tip": "💡 **Tee Tip:** Don’t get cute on approach — hit center."},
{"number": 11, "image": "hole11.jpg", "yardage": 185,
"overview": "📝 **Overview:** Short but intimidating par 3 over ravine.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Commit — anything short is jail.",
"approach": "🔍 **Approach Game:** Wind swirls — trust your yardage.",
"tip": "💡 **Tee Tip:** Pick club and swing — no indecision."},
{"number": 12, "image": "hole12.jpg", "yardage": 400,
"overview": "📝 **Overview:** Dogleg left, tree-lined fairway.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Draw off tee ideal — avoid long right.",
"approach": "🔍 **Approach Game:** Elevated green plays firm.",
"tip": "💡 **Tee Tip:** Don’t chase back pins."},
{"number": 13, "image": "hole13.jpg", "yardage": 425,
"overview": "📝 **Overview:** Wide but sloping fairway.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Driver to left-center avoids trees.",
"approach": "🔍 **Approach Game:** Mid-iron into a green with slope.",
"tip": "💡 **Tee Tip:** Don’t short-side yourself."},
{"number": 14, "image": "hole14.jpg", "yardage": 190,
"overview": "📝 **Overview:** Tough par 3 with bunkers everywhere.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor front-center.",
"approach": "🔍 **Approach Game:** Middle of green always safe.",
"tip": "💡 **Tee Tip:** Use tee to adjust aim."},
{"number": 15, "image": "hole15.jpg", "yardage": 525,
"overview": "📝 **Overview:** Risk/reward par 5.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Left-center opens the hole.",
"approach": "🔍 **Approach Game:** Lay up short or attack with hybrid.",
"tip": "💡 **Tee Tip:** Think backwards — position is key."},
{"number": 16, "image": "hole16.jpg", "yardage": 355,
"overview": "📝 **Overview:** Short par 4 with temptation.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Play to your yardage — driver may not be best.",
"approach": "🔍 **Approach Game:** Wedge to narrow green.",
"tip": "💡 **Tee Tip:** Spin control matters."},
{"number": 17, "image": "hole17.jpg", "yardage": 175,
"overview": "📝 **Overview:** Straightforward par 3 with elevation.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Trust the number — it plays shorter.",
"approach": "🔍 **Approach Game:** Back of green is danger.",
"tip": "💡 **Tee Tip:** Commit to your line."},
{"number": 18, "image": "hole18.jpg", "yardage": 510,
"overview": "📝 **Overview:** Memorable closing hole.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Aim left-center — opens approach.",
"approach": "🔍 **Approach Game:** Avoid water left.",
"tip": "💡 **Tee Tip:** Stay calm — finish strong."},
]
},
"Grays Crossing": {
"holes": \[
\# Similar full definition for holes 1–18 with strategies
\# Add this next if you’d like me to continue with Grays Crossing
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

# Strategy tips display

st.markdown(f"""
\### 🧠 Hole {hole\['number']} – Strategy & Tips

```
{hole['overview']}

{hole['tee_shot']}

{hole['approach']}

{hole['tip']}
```

""")
