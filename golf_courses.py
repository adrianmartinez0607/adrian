import streamlit as st
from PIL import Image

# Define courses and their holes with yardages and tips

courses = {
"Coyote Moon": {
"holes": \[
{"number": 1, "image": "hole1.jpg", "yardage": 485,
"overview": "📝 **Overview:** Scenic downhill opener with generous landing area.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor the left side to catch the slope.",
"approach": "🔍 **Approach Game:** Avoid going long — green slopes back to front.",
"tip": "💡 **Tee Tip:** Use a 3W or hybrid for safety."},
{"number": 2, "image": "hole2.jpg", "yardage": 365,
"overview": "📝 **Overview:** Dogleg left through trees.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Position drive near corner for best angle.",
"approach": "🔍 **Approach Game:** Green is protected short-left — fly it all the way.",
"tip": "💡 **Tee Tip:** Mid-iron off tee leaves full wedge."},
{"number": 3, "image": "hole3.jpg", "yardage": 190,
"overview": "📝 **Overview:** Uphill par 3 to a narrow green.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Take one more club due to elevation.",
"approach": "🔍 **Approach Game:** Avoid right — steep runoff.",
"tip": "💡 **Tee Tip:** Middle of green is never bad."},
{"number": 4, "image": "hole4.jpg", "yardage": 410,
"overview": "📝 **Overview:** Tough par 4 with a blind tee shot.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Aim at the tree line and trust the fairway opens up.",
"approach": "🔍 **Approach Game:** Second shot plays slightly uphill.",
"tip": "💡 **Tee Tip:** Use yardage markers carefully."},
{"number": 5, "image": "hole5.jpg", "yardage": 330,
"overview": "📝 **Overview:** Short par 4 with options.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Lay up with long iron or drive corner with draw.",
"approach": "🔍 **Approach Game:** Small green with bunkers left.",
"tip": "💡 **Tee Tip:** Don’t overthink the tee shot."},
{"number": 6, "image": "hole6.jpg", "yardage": 380,
"overview": "📝 **Overview:** Par 4 with water left.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Drive up right side for safest approach.",
"approach": "🔍 **Approach Game:** Avoid pulling approach into hazard.",
"tip": "💡 **Tee Tip:** Trust your fade."},
{"number": 7, "image": "hole7.jpg", "yardage": 195,
"overview": "📝 **Overview:** Another strong par 3.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Front bunker catches mishits.",
"approach": "🔍 **Approach Game:** Middle of green is fine — green slopes back.",
"tip": "💡 **Tee Tip:** Commit to your number."},
{"number": 8, "image": "hole8.jpg", "yardage": 540,
"overview": "📝 **Overview:** Scenic downhill par 5.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Grip it and rip it — wide landing zone.",
"approach": "🔍 **Approach Game:** Second shot needs placement for third.",
"tip": "💡 **Tee Tip:** Avoid going long on approach."},
{"number": 9, "image": "hole9.jpg", "yardage": 425,
"overview": "📝 **Overview:** Long uphill par 4.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Drive must carry ridge.",
"approach": "🔍 **Approach Game:** Elevated green demands club selection.",
"tip": "💡 **Tee Tip:** Driver essential — don’t lay back."},
{"number": 10, "image": "hole10.jpg", "yardage": 365,
"overview": "📝 **Overview:** Dogleg right with elevated tee.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Cut the corner with a fade.",
"approach": "🔍 **Approach Game:** Short wedge in if tee shot is ideal.",
"tip": "💡 **Tee Tip:** Play aggressive off tee."},
{"number": 11, "image": "hole11.jpg", "yardage": 185,
"overview": "📝 **Overview:** Short par 3 over a gorge.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Do not miss short — it’s jail.",
"approach": "🔍 **Approach Game:** Take enough club — swirling wind here.",
"tip": "💡 **Tee Tip:** Club up if unsure."},
{"number": 12, "image": "hole12.jpg", "yardage": 400,
"overview": "📝 **Overview:** Tree-lined dogleg left.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Driver leaves wedge if hit well.",
"approach": "🔍 **Approach Game:** Green is shallow and firm.",
"tip": "💡 **Tee Tip:** Middle-left is safe zone."},
{"number": 13, "image": "hole13.jpg", "yardage": 425,
"overview": "📝 **Overview:** Straightaway par 4 with slight rise.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Driver sets up a good mid-iron.",
"approach": "🔍 **Approach Game:** Avoid right-side trees.",
"tip": "💡 **Tee Tip:** Play for center of green."},
{"number": 14, "image": "hole14.jpg", "yardage": 190,
"overview": "📝 **Overview:** Flat par 3 with tricky green.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Accuracy is key — bunkers short left.",
"approach": "🔍 **Approach Game:** Pin front right? Be bold.",
"tip": "💡 **Tee Tip:** Don’t flirt with long left."},
{"number": 15, "image": "hole15.jpg", "yardage": 525,
"overview": "📝 **Overview:** Risk-reward par 5.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Left side opens up second shot.",
"approach": "🔍 **Approach Game:** Green is reachable — bunkers short.",
"tip": "💡 **Tee Tip:** Eagle possible with two perfect shots."},
{"number": 16, "image": "hole16.jpg", "yardage": 355,
"overview": "📝 **Overview:** Short par 4 you can drive.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Go for it or lay back — both work.",
"approach": "🔍 **Approach Game:** Sloped green defends well.",
"tip": "💡 **Tee Tip:** Wedge game matters here."},
{"number": 17, "image": "hole17.jpg", "yardage": 175,
"overview": "📝 **Overview:** Straightforward par 3.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Wind can swirl — trust your number.",
"approach": "🔍 **Approach Game:** Back shelf is hard to hold.",
"tip": "💡 **Tee Tip:** Middle of green all day."},
{"number": 18, "image": "hole18.jpg", "yardage": 510,
"overview": "📝 **Overview:** Great closing hole.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Big tee shot makes it reachable.",
"approach": "🔍 **Approach Game:** Second must carry hazard.",
"tip": "💡 **Tee Tip:** Finish strong — birdie in play."}
]
},
"Grays Crossing": {
"holes": \[
{"number": 1, "image": "grays1.jpg", "yardage": 428, "overview": "📝 **Overview:** Strategic opening hole with bunkers down the right.", "tee\_shot": "🎯 **Tee Shot Strategy:** Favor the left side to avoid fairway bunkers.", "approach": "🔍 **Approach Game:** Watch the wind into this elevated green.", "tip": "💡 **Tee Tip:** Club up if you’re unsure on approach."},
{"number": 2, "image": "grays2.jpg", "yardage": 363, "overview": "📝 **Overview:** Dogleg left with pine framing both sides.", "tee\_shot": "🎯 **Tee Shot Strategy:** Draw off the tee sets up a great angle.", "approach": "🔍 **Approach Game:** Miss short rather than long.", "tip": "💡 **Tee Tip:** You can be aggressive off the tee."},
{"number": 3, "image": "grays3.jpg", "yardage": 194, "overview": "📝 **Overview:** Scenic downhill par 3 with a view.", "tee\_shot": "🎯 **Tee Shot Strategy:** Choose club wisely — elevation makes it play short.", "approach": "🔍 **Approach Game:** Use slopes to feed it to the hole.", "tip": "💡 **Tee Tip:** Be decisive — wind can swirl."},
{"number": 4, "image": "grays4.jpg", "yardage": 548, "overview": "📝 **Overview:** Risk-reward par 5 with trouble right.", "tee\_shot": "🎯 **Tee Shot Strategy:** Hit to the wide landing area left.", "approach": "🔍 **Approach Game:** Smart layup leaves a full wedge.", "tip": "💡 **Tee Tip:** Don’t chase eagle unless perfectly set up."},
{"number": 5, "image": "grays5.jpg", "yardage": 429, "overview": "📝 **Overview:** Demanding par 4 with elevated green.", "tee\_shot": "🎯 **Tee Shot Strategy:** Long and straight required.", "approach": "🔍 **Approach Game:** Green is deep but protected.", "tip": "💡 **Tee Tip:** Aim for center of green."},
{"number": 6, "image": "grays6.jpg", "yardage": 389, "overview": "📝 **Overview:** Dogleg right with bunkers.", "tee\_shot": "🎯 **Tee Shot Strategy:** Hug left to shorten the hole.", "approach": "🔍 **Approach Game:** Don’t flirt with the right edge.", "tip": "💡 **Tee Tip:** Safe play pays off."},
{"number": 7, "image": "grays7.jpg", "yardage": 162, "overview": "📝 **Overview:** Short par 3 with deep bunkers.", "tee\_shot": "🎯 **Tee Shot Strategy:** High shot lands soft.", "approach": "🔍 **Approach Game:** Don’t miss left.", "tip": "💡 **Tee Tip:** Aim center green regardless of pin."},
{"number": 8, "image": "grays8.jpg", "yardage": 480, "overview": "📝 **Overview:** Reachable par 5 with narrow landing.", "tee\_shot": "🎯 **Tee Shot Strategy:** Hug the right side for better angle.", "approach": "🔍 **Approach Game:** Lay up to full wedge.", "tip": "💡 **Tee Tip:** Birdie hole if played smart."},
{"number": 9, "image": "grays9.jpg", "yardage": 438, "overview": "📝 **Overview:** Tough finish to the front nine.", "tee\_shot": "🎯 **Tee Shot Strategy:** Favor left side to open green.", "approach": "🔍 **Approach Game:** Club up for uphill shot.", "tip": "💡 **Tee Tip:** Big green — know your pin."},
{"number": 10, "image": "grays10.jpg", "yardage": 410, "overview": "📝 **Overview:** Bunkers define this dogleg right.", "tee\_shot": "🎯 **Tee Shot Strategy:** Aim left edge of fairway bunker.", "approach": "🔍 **Approach Game:** Avoid short right.", "tip": "💡 **Tee Tip:** Right side of green feeds left."},
{"number": 11, "image": "grays11.jpg", "yardage": 172, "overview": "📝 **Overview:** Challenging par 3 over water.", "tee\_shot": "🎯 **Tee Shot Strategy:** Hit solid — carry is key.", "approach": "🔍 **Approach Game:** Middle of green is safe.", "tip": "💡 **Tee Tip:** Play smart — par is a great score."},
{"number": 12, "image": "grays12.jpg", "yardage": 378, "overview": "📝 **Overview:** Straightforward par 4.", "tee\_shot": "🎯 **Tee Shot Strategy:** Drive center fairway.", "approach": "🔍 **Approach Game:** Avoid back left miss.", "tip": "💡 **Tee Tip:** Trust your yardage."},
{"number": 13, "image": "grays13.jpg", "yardage": 412, "overview": "📝 **Overview:** Demanding par 4 with water in play.", "tee\_shot": "🎯 **Tee Shot Strategy:** Accuracy is key — aim right.", "approach": "🔍 **Approach Game:** Avoid long into water.", "tip": "💡 **Tee Tip:** Use extra club in wind."},
{"number": 14, "image": "grays14.jpg", "yardage": 334, "overview": "📝 **Overview:** Short par 4 with tempting green.", "tee\_shot": "🎯 **Tee Shot Strategy:** Lay up right or go for it.", "approach": "🔍 **Approach Game:** Green is tricky.", "tip": "💡 **Tee Tip:** A wedge is your friend here."},
{"number": 15, "image": "grays15.jpg", "yardage": 525, "overview": "📝 **Overview:** Strategic par 5 with tilt.", "tee\_shot": "🎯 **Tee Shot Strategy:** Right side is best.", "approach": "🔍 **Approach Game:** Think about third shot yardage.", "tip": "💡 **Tee Tip:** You can score here."},
{"number": 16, "image": "grays16.jpg", "yardage": 194, "overview": "📝 **Overview:** Downhill par 3 plays short.", "tee\_shot": "🎯 **Tee Shot Strategy:** Elevation affects club.", "approach": "🔍 **Approach Game:** Green is firm.", "tip": "💡 **Tee Tip:** Take 1–3 clubs less."},
{"number": 17, "image": "grays17.jpg", "yardage": 354, "overview": "📝 **Overview:** Wind-assisted short par 4.", "tee\_shot": "🎯 **Tee Shot Strategy:** Avoid going too long.", "approach": "🔍 **Approach Game:** Firm green, hard to hold.", "tip": "💡 **Tee Tip:** Land short and bounce on."},
{"number": 18, "image": "grays18.jpg", "yardage": 475, "overview": "📝 **Overview:** Long, tough closer.", "tee\_shot": "🎯 **Tee Shot Strategy:** Favor right-center.", "approach": "🔍 **Approach Game:** Avoid right hazard.", "tip": "💡 **Tee Tip:** Three-shot hole for most."}
]
}
}

# Sidebar: Course and Hole selection

st.sidebar.title("Golf Course Guide")
selected\_course = st.sidebar.selectbox("Select Course", list(courses.keys()))
hole\_numbers = \[f"Hole

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
], 
},
"Grays Crossing": {
"holes": \[
{"number": 1, "image": "grays1.jpg", "yardage": 375,
"overview": "📝 **Overview:** A solid opening par 4 that sets the tone for the round with gentle dogleg right.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor the left side off the tee to open up your approach. A 240–260 yard drive is ideal.",
"approach": "🔍 **Approach Game:** Slightly elevated green requires a high shot to hold. Watch for bunkers left.",
"tip": "💡 **Tee Tip:** Take one more club than you think into this firm green."},
{"number": 2, "image": "grays2.jpg", "yardage": 405,
"overview": "📝 **Overview:** Challenging par 4 with a tight driving corridor and uphill finish.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Keep it straight — fairway narrows beyond 240 yards.",
"approach": "🔍 **Approach Game:** Uphill second plays longer than it looks. Avoid missing right.",
"tip": "💡 **Tee Tip:** Don’t flirt with right-side trees — safe play is to the middle."},
{"number": 3, "image": "grays3.jpg", "yardage": 160,
"overview": "📝 **Overview:** A mid-length par 3 guarded tightly by bunkers.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor the left-center of green. Short is better than long.",
"approach": "🔍 **Approach Game:** Stay below the hole on this tricky green.",
"tip": "💡 **Tee Tip:** Play for the center and avoid flag hunting here."},
{"number": 4, "image": "grays4.jpg", "yardage": 520,
"overview": "📝 **Overview:** Long par 5 that rewards careful plotting more than aggression.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Hit your most reliable club — fairway is key.",
"approach": "🔍 **Approach Game:** Lay up short of cross bunkers for a full wedge.",
"tip": "💡 **Tee Tip:** Don’t overthink — 3 smart shots will get you a birdie look."},
{"number": 5, "image": "grays5.jpg", "yardage": 410,
"overview": "📝 **Overview:** Demanding par 4 with a forced carry over water off the tee.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Choose club based on carry yardage — it’s all about confidence.",
"approach": "🔍 **Approach Game:** Green slopes severely back to front. Stay below the hole.",
"tip": "💡 **Tee Tip:** Trust your number and swing committed."},
{"number": 6, "image": "grays6.jpg", "yardage": 360,
"overview": "📝 **Overview:** Short, fun par 4 with scoring potential.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Long iron or hybrid to center sets up wedge.",
"approach": "🔍 **Approach Game:** Stay aggressive — this green is generous.",
"tip": "💡 **Tee Tip:** Great chance to pick up a stroke — capitalize."},
{"number": 7, "image": "grays7.jpg", "yardage": 185,
"overview": "📝 **Overview:** Picturesque downhill par 3.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Play 1 club less — elevation is deceptive.",
"approach": "🔍 **Approach Game:** Don’t short-side yourself — favor the fat part of green.",
"tip": "💡 **Tee Tip:** Breathe and enjoy the view before swinging."},
{"number": 8, "image": "grays8.jpg", "yardage": 430,
"overview": "📝 **Overview:** Arguably the toughest par 4 on the front.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor right center off the tee. Left is dead.",
"approach": "🔍 **Approach Game:** Long iron or hybrid in — aim to middle.",
"tip": "💡 **Tee Tip:** Take your bogey and run if needed."},
{"number": 9, "image": "grays9.jpg", "yardage": 535,
"overview": "📝 **Overview:** Sweeping dogleg par 5 that tempts the aggressive play.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor left center — opens angle.",
"approach": "🔍 **Approach Game:** Lay up to wedge range if going for green is risky.",
"tip": "💡 **Tee Tip:** Smart second shot is key to scoring here."},
{"number": 10, "image": "grays10.jpg", "yardage": 400,
"overview": "📝 **Overview:** Fairly straightforward par 4 to begin the back nine.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Fairway wood is enough — keep it in play.",
"approach": "🔍 **Approach Game:** Elevated green makes distance control tricky.",
"tip": "💡 **Tee Tip:** Don’t overswing off the tee."},
{"number": 11, "image": "grays11.jpg", "yardage": 180,
"overview": "📝 **Overview:** Compact par 3 with challenging wind.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Pay attention to tree movement for wind cues.",
"approach": "🔍 **Approach Game:** Get ball pin-high — short leaves tough chip.",
"tip": "💡 **Tee Tip:** Smooth swing — don’t force it."},
{"number": 12, "image": "grays12.jpg", "yardage": 450,
"overview": "📝 **Overview:** Big par 4 with elevation loss off the tee.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Let it rip! Good drive rewards with short iron.",
"approach": "🔍 **Approach Game:** Subtle green slopes — watch pin position.",
"tip": "💡 **Tee Tip:** One of the best chances to gain on par."},
{"number": 13, "image": "grays13.jpg", "yardage": 412,
"overview": "📝 **Overview:** Normally into the prevailing winds, accuracy will be at a premium on this demanding par four that is protected by water from tee to green.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Long and accurate drive to the right-center is required.",
"approach": "🔍 **Approach Game:** Favor short of the pin — green is tough.",
"tip": "💡 **Tee Tip:** Play conservatively and respect the hazard."},
{"number": 14, "image": "grays14.jpg", "yardage": 334,
"overview": "📝 **Overview:** One of the shortest par 4s, this hole invites decision-making.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Layup short of left bunkers or go for green if confident.",
"approach": "🔍 **Approach Game:** Small green demands precise wedge.",
"tip": "💡 **Tee Tip:** Don’t let the yardage fool you — danger lurks."},
{"number": 15, "image": "grays15.jpg", "yardage": 525,
"overview": "📝 **Overview:** Reachable par 5 offering birdie chances with thoughtful play.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor right side — ball feeds left.",
"approach": "🔍 **Approach Game:** Narrow green demands correct club.",
"tip": "💡 **Tee Tip:** Don’t force it — smart play pays."},
{"number": 16, "image": "grays16.jpg", "yardage": 194,
"overview": "📝 **Overview:** Downhill par 3 plays 1–3 clubs shorter.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Use wind and slope to your advantage.",
"approach": "🔍 **Approach Game:** Front of green is safe miss.",
"tip": "💡 **Tee Tip:** Trust your club choice and swing free."},
{"number": 17, "image": "grays17.jpg", "yardage": 354,
"overview": "📝 **Overview:** Tailwind hole with a tricky green.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Avoid blowing through fairway — aim left.",
"approach": "🔍 **Approach Game:** Mid-iron into firm green — control spin.",
"tip": "💡 **Tee Tip:** Stay left for best approach angle."},
{"number": 18, "image": "grays18.jpg", "yardage": 475,
"overview": "📝 **Overview:** Long closing par 5 into prevailing wind.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Right-center of fairway is best.",
"approach": "🔍 **Approach Game:** Layup left to avoid water hazard.",
"tip": "💡 **Tee Tip:** Solid par to finish strong is a win."}
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
