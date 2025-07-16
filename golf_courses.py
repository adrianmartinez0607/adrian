import streamlit as st
from PIL import Image

# Define courses and their holes with yardages and tips

descriptions = {
\*\*{
("Coyote Moon", i): data for i, data in enumerate(\[
{"overview": "📝 **Overview:** A dramatic opening par 5 with an elevated tee shot and generous fairway.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Aim slightly right-center. From the white tees (\~485 yards), most players should play for position rather than try to reach in two.",
"approach": "🔍 **Approach Game:** A layup short of the hazard sets up a wedge to a slightly elevated green.",
"tip": "💡 **Tee Tip:** Don’t get greedy—start the round with a smart par or birdie chance."},
{"overview": "📝 **Overview:** A sharp dogleg left par 4 that rewards accuracy over power.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor a 200-220 yard tee shot down the middle-left to avoid running through the fairway.",
"approach": "🔍 **Approach Game:** A short to mid iron remains. Be aware of the elevated green.",
"tip": "💡 **Tee Tip:** Use a hybrid or long iron to control placement."},
{"overview": "📝 **Overview:** A picturesque par 3 over water.",
"tee\_shot": "🎯 **Tee Shot Strategy:** At 190 yards, club up if wind is into you. Favor the right side.",
"approach": "🔍 **Approach Game:** Bail out short or right is safe—avoid the water left.",
"tip": "💡 **Tee Tip:** Don’t get too aggressive—middle of the green is your friend."},
\*\[{"overview": f"📝 **Overview:** Placeholder for Coyote Moon Hole {i+4}.",
"tee\_shot": "🎯 **Tee Shot Strategy:** ...",
"approach": "🔍 **Approach Game:** ...",
"tip": "💡 **Tee Tip:** ..."} for i in range(15)]
], start=1)
},
\*\*{
("Grays Crossing", i): data for i, data in enumerate(\[
{"overview": "📝 **Overview:** Opens into prevailing wind — tough start.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor left side to avoid bunkers and open angle.",
"approach": "🔍 **Approach Game:** Green is guarded right — middle is smart.",
"tip": "💡 **Tee Tip:** Driver required — commit to line."},
{"overview": "📝 **Overview:** Slight dogleg left with tricky fairway bunker.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Stay short of left bunker off tee.",
"approach": "🔍 **Approach Game:** Green slopes right with bunkers left.",
"tip": "💡 **Tee Tip:** Long iron or hybrid off tee works."},
{"overview": "📝 **Overview:** Sweeping par 5 downwind.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Left side ideal — catch fairway slope.",
"approach": "🔍 **Approach Game:** Wedge in or go for it over last bunker.",
"tip": "💡 **Tee Tip:** Miss right for safe bounce."},
\*\[{"overview": f"📝 **Overview:** Placeholder for Grays Crossing Hole {i+4}.",
"tee\_shot": "🎯 **Tee Shot Strategy:** ...",
"approach": "🔍 **Approach Game:** ...",
"tip": "💡 **Tee Tip:** ..."} for i in range(15)]
], start=1)
}
}

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

# Strategy tips display

desc = descriptions.get((selected\_course, hole\['number']))
if desc:
st.markdown(f"""
\### 🧠 Hole {hole\['number']} – Strategy & Tips

```
    {desc['overview']}

    {desc['tee_shot']}

    {desc['approach']}

    {desc['tip']}
""")
```

else:
st.info("Strategy info not yet available for this hole.")
