import streamlit as st
from PIL import Image

# Define courses and their holes with yardages and tips

courses = {
"Coyote Moon": {
"holes":[
{"number": 1, "image": "hole1.jpg", "yardage": 485,
"overview": "📝 **Overview:** Scenic downhill opener with generous landing area.",
"tee\_shot": "🎯 **Tee Shot Strategy:** Favor the left side to catch the slope.",
"approach": "🔍 **Approach Game:** Avoid going long — green slopes back to front.",
"tip": "💡 **Tee Tip:** Use a 3W or hybrid for safety."},
{"number": 2, "image": "hole2.jpg", "yardage": 365,
        "overview": "📝 **Overview:** Dogleg left through trees.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Position drive near corner for best angle.",
        "approach": "🔍 **Approach Game:** Green is protected short-left — fly it all the way.",
        "tip": "💡 **Tee Tip:** Mid-iron off tee leaves full wedge."},

        {"number": 3, "image": "hole3.jpg", "yardage": 190,
        "overview": "📝 **Overview:** Uphill par 3 to a narrow green.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Take one more club due to elevation.",
        "approach": "🔍 **Approach Game:** Avoid right — steep runoff.",
        "tip": "💡 **Tee Tip:** Middle of green is never bad."},

        {"number": 4, "image": "hole4.jpg", "yardage": 410,
        "overview": "📝 **Overview:** Tough par 4 with a blind tee shot.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Aim at the tree line and trust the fairway opens up.",
        "approach": "🔍 **Approach Game:** Second shot plays slightly uphill.",
        "tip": "💡 **Tee Tip:** Use yardage markers carefully."},

        {"number": 5, "image": "hole5.jpg", "yardage": 330,
        "overview": "📝 **Overview:** Short par 4 with options.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Lay up with long iron or drive corner with draw.",
        "approach": "🔍 **Approach Game:** Small green with bunkers left.",
        "tip": "💡 **Tee Tip:** Don’t overthink the tee shot."},

        {"number": 6, "image": "hole6.jpg", "yardage": 380,
        "overview": "📝 **Overview:** Par 4 with water left.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Drive up right side for safest approach.",
        "approach": "🔍 **Approach Game:** Avoid pulling approach into hazard.",
        "tip": "💡 **Tee Tip:** Trust your fade."},

        {"number": 7, "image": "hole7.jpg", "yardage": 195,
        "overview": "📝 **Overview:** Another strong par 3.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Front bunker catches mishits.",
        "approach": "🔍 **Approach Game:** Middle of green is fine — green slopes back.",
        "tip": "💡 **Tee Tip:** Commit to your number."},

        {"number": 8, "image": "hole8.jpg", "yardage": 540,
        "overview": "📝 **Overview:** Scenic downhill par 5.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Grip it and rip it — wide landing zone.",
        "approach": "🔍 **Approach Game:** Second shot needs placement for third.",
        "tip": "💡 **Tee Tip:** Avoid going long on approach."},

        {"number": 9, "image": "hole9.jpg", "yardage": 425,
        "overview": "📝 **Overview:** Long uphill par 4.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Drive must carry ridge.",
        "approach": "🔍 **Approach Game:** Elevated green demands club selection.",
        "tip": "💡 **Tee Tip:** Driver essential — don’t lay back."},

        {"number": 10, "image": "hole10.jpg", "yardage": 365,
        "overview": "📝 **Overview:** Dogleg right with elevated tee.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Cut the corner with a fade.",
        "approach": "🔍 **Approach Game:** Short wedge in if tee shot is ideal.",
        "tip": "💡 **Tee Tip:** Play aggressive off tee."},

        {"number": 11, "image": "hole11.jpg", "yardage": 185,
        "overview": "📝 **Overview:** Short par 3 over a gorge.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Do not miss short — it’s jail.",
        "approach": "🔍 **Approach Game:** Take enough club — swirling wind here.",
        "tip": "💡 **Tee Tip:** Club up if unsure."},

        {"number": 12, "image": "hole12.jpg", "yardage": 400,
        "overview": "📝 **Overview:** Tree-lined dogleg left.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Driver leaves wedge if hit well.",
        "approach": "🔍 **Approach Game:** Green is shallow and firm.",
        "tip": "💡 **Tee Tip:** Middle-left is safe zone."},

        {"number": 13, "image": "hole13.jpg", "yardage": 425,
        "overview": "📝 **Overview:** Straightaway par 4 with slight rise.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Driver sets up a good mid-iron.",
        "approach": "🔍 **Approach Game:** Avoid right-side trees.",
        "tip": "💡 **Tee Tip:** Play for center of green."},

        {"number": 14, "image": "hole14.jpg", "yardage": 190,
        "overview": "📝 **Overview:** Flat par 3 with tricky green.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Accuracy is key — bunkers short left.",
        "approach": "🔍 **Approach Game:** Pin front right? Be bold.",
        "tip": "💡 **Tee Tip:** Don’t flirt with long left."},

        {"number": 15, "image": "hole15.jpg", "yardage": 525,
        "overview": "📝 **Overview:** Risk-reward par 5.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Left side opens up second shot.",
        "approach": "🔍 **Approach Game:** Green is reachable — bunkers short.",
        "tip": "💡 **Tee Tip:** Eagle possible with two perfect shots."},

        {"number": 16, "image": "hole16.jpg", "yardage": 355,
        "overview": "📝 **Overview:** Short par 4 you can drive.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Go for it or lay back — both work.",
        "approach": "🔍 **Approach Game:** Sloped green defends well.",
        "tip": "💡 **Tee Tip:** Wedge game matters here."},

        {"number": 17, "image": "hole17.jpg", "yardage": 175,
        "overview": "📝 **Overview:** Straightforward par 3.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Wind can swirl — trust your number.",
        "approach": "🔍 **Approach Game:** Back shelf is hard to hold.",
        "tip": "💡 **Tee Tip:** Middle of green all day."},

        {"number": 18, "image": "hole18.jpg", "yardage": 510,
        "overview": "📝 **Overview:** Great closing hole.",
        "tee_shot": "🎯 **Tee Shot Strategy:** Big tee shot makes it reachable.",
        "approach": "🔍 **Approach Game:** Second must carry hazard.",
        "tip": "💡 **Tee Tip:** Finish strong — birdie in play."}
    ]
},
"Grays Crossing": {
    "holes": [
{"number": 1, "image": "grays1.jpg", "yardage": 375,
"overview": "📝 **Overview:** A solid opening par 4 that sets the tone for the round with gentle dogleg right.",
"tee_shot": "🎯 **Tee Shot Strategy:** Favor the left side off the tee to open up your approach. A 240–260 yard drive is ideal.",
"approach": "🔍 **Approach Game:** Slightly elevated green requires a high shot to hold. Watch for bunkers left.",
"tip": "💡 **Tee Tip:** Take one more club than you think into this firm green."},

{"number": 2, "image": "grays2.jpg", "yardage": 405,
"overview": "📝 **Overview:** Challenging par 4 with a tight driving corridor and uphill finish.",
"tee_shot": "🎯 **Tee Shot Strategy:** Keep it straight — fairway narrows beyond 240 yards.",
"approach": "🔍 **Approach Game:** Uphill second plays longer than it looks. Avoid missing right.",
"tip": "💡 **Tee Tip:** Don’t flirt with right-side trees — safe play is to the middle."},

{"number": 3, "image": "grays3.jpg", "yardage": 570,
"overview": "📝 Overview: Long par 5 with a narrowing fairway.",
"tee_shot": "🎯 Tee Shot Strategy: Keep right to avoid trees creeping in.",
"approach": "🔍 Approach Game: Play smart — 3-shot hole for most.",
"tip": "💡 Tee Tip: Avoid bunkers 100 yards in — they’ll trap you."},

{"number": 4, "image": "grays4.jpg", "yardage": 185,
"overview": "📝 Overview: Downhill par 3 with wide green.",
"tee_shot": "🎯 Tee Shot Strategy: Club down and trust the wind.",
"approach": "🔍 Approach Game: Aim center of green — pins are tough.",
"tip": "💡 Tee Tip: Distance control > direction here."},
           
{"number": 5, "image": "grays5.jpg", "yardage": 385,
"overview": "📝 Overview: Narrow fairway with trouble right.",
"tee_shot": "🎯 Tee Shot Strategy: Left center keeps you safe.",
"approach": "🔍 Approach Game: Avoid short — green runs away.",
"tip": "💡 Tee Tip: Play a fade off the tee if you have it."},

{"number": 6, "image": "grays6.jpg", "yardage": 420,
"overview": "📝 Overview: Straight par 4 with demanding approach.",
"tee_shot": "🎯 Tee Shot Strategy: Fire at left edge of fairway bunker.",
"approach": "🔍 Approach Game: Use slopes to feed ball to pin.",
"tip": "💡 Tee Tip: Short is better than long here."},

{"number": 7, "image": "grays7.jpg", "yardage": 200,
"overview": "📝 Overview: Long par 3 guarded by bunkers.",
"tee_shot": "🎯 Tee Shot Strategy: High fade helps hold green.",
"approach": "🔍 Approach Game: Don’t chase back pins.",
"tip": "💡 Tee Tip: Take your par and go."},

{"number": 8, "image": "grays8.jpg", "yardage": 550,
"overview": "📝 Overview: Dogleg right par 5 — reachable in two.",
"tee_shot": "🎯 Tee Shot Strategy: Aim left to open up angle.",
"approach": "🔍 Approach Game: Green is shallow — land it soft.",
"tip": "💡 Tee Tip: 3rd shot is often easier than 2nd here."},

{"number": 9, "image": "grays9.jpg", "yardage": 430,
"overview": "📝 Overview: Strong finishing hole to the front nine.",
"tee_shot": "🎯 Tee Shot Strategy: Center fairway gives best view.",
"approach": "🔍 Approach Game: Uphill again — add 5-10 yards.",
"tip": "💡 Tee Tip: Keep drive out of the rough — approach is tough enough."},

{"number": 10, "image": "grays10.jpg", "yardage": 405,
"overview": "📝 Overview: Risk/reward with a fairway that tightens.",
"tee_shot": "🎯 Tee Shot Strategy: Driver brings trouble — 3W or hybrid safer.",
"approach": "🔍 Approach Game: Green tilts hard right to left.",
"tip": "💡 Tee Tip: Start the back nine with a smart play."},

{"number": 11, "image": "grays11.jpg", "yardage": 350,
"overview": "📝 Overview: Short par 4 with hidden danger.",
"tee_shot": "🎯 Tee Shot Strategy: Hit to 100-yard mark for wedge in.",
"approach": "🔍 Approach Game: Avoid right side near the green.",
"tip": "💡 Tee Tip: Don’t be greedy off the tee."},

{"number": 12, "image": "grays12.jpg", "yardage": 185,
"overview": "📝 Overview: Narrow green tucked behind bunkers.",
"tee_shot": "🎯 Tee Shot Strategy: Play for middle no matter the pin.",
"approach": "🔍 Approach Game: Getting up and down from bunkers is tough.",
"tip": "💡 Tee Tip: Long is dead — trust your number."},

{"number": 13, "image": "grays13.jpg", "yardage": 412,
"overview": "📝 Overview: Water-lined par 4 into prevailing wind.",
"tee_shot": "🎯 Tee Shot Strategy: Favor left side away from water.",
"approach": "🔍 Approach Game: Stay short of pin on slick green.",
"tip": "💡 Tee Tip: Par here is a win."},

{"number": 14, "image": "grays14.jpg", "yardage": 334,
"overview": "📝 Overview: Drivable par 4 with risk.",
"tee_shot": "🎯 Tee Shot Strategy: Lay up right or go for it left.",
"approach": "🔍 Approach Game: Green is tiny and quick.",
"tip": "💡 Tee Tip: A safe birdie hole with smart play."},
           
{"number": 15, "image": "grays15.jpg", "yardage": 525,
"overview": "📝 Overview: Par 5 with right-to-left slope.",
"tee_shot": "🎯 Tee Shot Strategy: Stay right for best lie.",
"approach": "🔍 Approach Game: Think two shots ahead — green is shallow.",
"tip": "💡 Tee Tip: Wedge distance is better than forced second."},

{"number": 16, "image": "grays16.jpg", "yardage": 194,
"overview": "📝 Overview: Downhill par 3 plays short.",
"tee_shot": "🎯 Tee Shot Strategy: 1–3 clubs less depending on wind.",
"approach": "🔍 Approach Game: Avoid spinning off the front.",
"tip": "💡 Tee Tip: Trust your number and commit."},

{"number": 17, "image": "grays17.jpg", "yardage": 354,
"overview": "📝 Overview: Tee shot plays with the wind — danger lurks.",
"tee_shot": "🎯 Tee Shot Strategy: Left edge of bunker ideal.",
"approach": "🔍 Approach Game: Fast green makes holding it tricky.",
"tip": "💡 Tee Tip: Mid-iron in is better than OB right."},

{"number": 18, "image": "grays18.jpg", "yardage": 475,
"overview": "📝 Overview: Three-shot par 5 to end the round.",
"tee_shot": "🎯 Tee Shot Strategy: Right-center avoids trouble.",
"approach": "🔍 Approach Game: 2nd shot left opens up approach.",
"tip": "💡 Tee Tip: Closing birdie is there with smart play."}
]

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

### 🧠 Hole {hole\['number']} – Strategy & Tips

{hole\['overview']}

{hole\['tee\_shot']}

{hole\['approach']}

{hole\['tip']}
""")
    }
    }
