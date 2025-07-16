import streamlit as st
from PIL import Image

# Hole data with yardages and strategy
courses = {
    "Coyote Moon": {
        "tee_color": "White Tees",
        "holes": [
            {
                "number": i,
                "image": f"hole{i}.jpg",
                "yardage": yard,
                "overview": ov,
                "tee_shot": ts,
                "approach": ap,
                "tip": tp
            } for i, (yard, ov, ts, ap, tp) in enumerate([
                (485, "Scenic downhill opener with generous landing area.",
                 "Favor the left side to catch the slope.",
                 "Avoid going long — green slopes back to front.",
                 "Use a 3W or hybrid for safety."),
                (365, "Dogleg left through trees.",
                 "Position drive near corner for best angle.",
                 "Green is protected short-left — fly it all the way.",
                 "Mid-iron off tee leaves full wedge."),
                (190, "Uphill par 3 to a narrow green.",
                 "Take one more club due to elevation.",
                 "Avoid right — steep runoff.",
                 "Middle of green is never bad."),
                (410, "Tough par 4 with a blind tee shot.",
                 "Aim at the tree line and trust the fairway opens up.",
                 "Second shot plays slightly uphill.",
                 "Use yardage markers carefully."),
                (330, "Short par 4 with options.",
                 "Lay up with long iron or drive corner with draw.",
                 "Small green with bunkers left.",
                 "Don’t overthink the tee shot."),
                (380, "Par 4 with water left.",
                 "Drive up right side for safest approach.",
                 "Avoid pulling approach into hazard.",
                 "Trust your fade."),
                (195, "Another strong par 3.",
                 "Front bunker catches mishits.",
                 "Middle of green is fine — green slopes back.",
                 "Commit to your number."),
                (540, "Scenic downhill par 5.",
                 "Grip it and rip it — wide landing zone.",
                 "Second shot needs placement for third.",
                 "Avoid going long on approach."),
                (425, "Long uphill par 4.",
                 "Drive must carry ridge.",
                 "Elevated green demands club selection.",
                 "Driver essential — don’t lay back."),
                (365, "Dogleg right with elevated tee.",
                 "Cut the corner with a fade.",
                 "Short wedge in if tee shot is ideal.",
                 "Play aggressive off tee."),
                (185, "Short par 3 over a gorge.",
                 "Do not miss short — it’s jail.",
                 "Take enough club — swirling wind here.",
                 "Club up if unsure."),
                (400, "Tree-lined dogleg left.",
                 "Driver leaves wedge if hit well.",
                 "Green is shallow and firm.",
                 "Middle-left is safe zone."),
                (425, "Straightaway par 4 with slight rise.",
                 "Driver sets up a good mid-iron.",
                 "Avoid right-side trees.",
                 "Play for center of green."),
                (190, "Flat par 3 with tricky green.",
                 "Accuracy is key — bunkers short left.",
                 "Pin front right? Be bold.",
                 "Don’t flirt with long left."),
                (525, "Risk-reward par 5.",
                 "Left side opens up second shot.",
                 "Green is reachable — bunkers short.",
                 "Eagle possible with two perfect shots."),
                (355, "Short par 4 you can drive.",
                 "Go for it or lay back — both work.",
                 "Sloped green defends well.",
                 "Wedge game matters here."),
                (175, "Straightforward par 3.",
                 "Wind can swirl — trust your number.",
                 "Back shelf is hard to hold.",
                 "Middle of green all day."),
                (510, "Great closing hole.",
                 "Big tee shot makes it reachable.",
                 "Second must carry hazard.",
                 "Finish strong — birdie in play.")
            ], start=1)
        ]
    },
    "Grays Crossing": {
        "tee_color": "Stampede (Gold Tees)",
        "holes": [
            {
                "number": i,
                "image": f"grays{i}.jpg",
                "yardage": yard,
                "overview": ov,
                "tee_shot": ts,
                "approach": ap,
                "tip": tp
            } for i, (yard, ov, ts, ap, tp) in enumerate([
                (405, "Opens into prevailing wind — tough start.",
                 "Favor left side to avoid bunkers and open angle.",
                 "Green is guarded right — middle is smart.",
                 "Driver required — commit to line."),
                (375, "Slight dogleg left with tricky fairway bunker.",
                 "Stay short of left bunker off tee.",
                 "Green slopes right with bunkers left.",
                 "Long iron or hybrid off tee works."),
                (585, "Sweeping par 5 downwind.",
                 "Left side ideal — catch fairway slope.",
                 "Wedge in or go for it over last bunker.",
                 "Miss right for safe bounce."),
                (165, "Shortest hole but requires precision.",
                 "Wind in face — club up.",
                 "Aim right — slopes feed left.",
                 "Par is a good score."),
                (420, "Long par 4 with pine backdrop.",
                 "Right side is safer — left tightens approach.",
                 "Downhill into fast green.",
                 "Play short to run it on."),
                (325, "Driveable par 4 — risk/reward.",
                 "Aggressive line over bunkers or safe layup right.",
                 "Green slopes front to back.",
                 "Only go for it if confident."),
                (580, "Par 5 that slopes left to right.",
                 "Left side avoids kick downslope.",
                 "Shallow green demands high shot.",
                 "Don’t miss long."),
                (185, "Downhill par 3 with tricky wind.",
                 "Bunkers right and pond left.",
                 "Plays shorter than number.",
                 "Center hit wins."),
                (455, "Back into wind — long par 4 uphill.",
                 "Drive right side — gets left bounce.",
                 "Club up for elevated green.",
                 "Don’t overclub — steep slope back."),
                (395, "Long par 4 with tough green.",
                 "Split bunkers define landing zone.",
                 "Wind helps — second plays shorter.",
                 "Read pin position carefully."),
                (205, "Medium par 3 with deep green.",
                 "Avoid left bunker — ball feeds left.",
                 "Middle of green best target.",
                 "Use full iron — don’t baby it."),
                (420, "Traditional par 4 with great angle from left.",
                 "Aim left center off tee.",
                 "Green flanked by bunkers both sides.",
                 "Solid iron will reward."),
                (435, "Water all the way on right.",
                 "Keep drive left — huge penalty otherwise.",
                 "Green guarded and firm.",
                 "Play safe and avoid hero shot."),
                (340, "Short par 4 with small green.",
                 "Drive over bunkers or lay back.",
                 "Wedge must be precise.",
                 "Eagle or bogey — choose wisely."),
                (535, "Birdie chance if thought out.",
                 "Right side for bounce left.",
                 "Final wedge must stick a shallow green.",
                 "Club control crucial."),
                (175, "Deceptive par 3 downhill.",
                 "1–3 clubs less depending on wind.",
                 "Front miss is okay.",
                 "Trust your swing."),
                (410, "Tough green to hold with wind at back.",
                 "Avoid driving through fairway.",
                 "Aim over left edge of bunker.",
                 "High iron best to stop ball."),
                (555, "Strong finisher with split fairway.",
                 "Right-center gives best angle unless cutting left.",
                 "Hazard right on second — be smart.",
                 "Birdie if executed well.")
            ], start=1)
        ]
    }
}

# Sidebar: Course and Hole selection
st.set_page_config(page_title="Golf Course Guide", layout="centered")
st.sidebar.title("🏌️ Golf Course Guide")
selected_course = st.sidebar.selectbox("Select Course", list(courses.keys()))
hole_options = [f"Hole {h['number']}" for h in courses[selected_course]["holes"]]
selected_hole_index = st.sidebar.selectbox("Select Hole", hole_options, index=0)
hole = courses[selected_course]["holes"][int(selected_hole_index.split()[1]) - 1]

# Display hole content
st.title(f"{selected_course} – Hole {hole['number']}")
st.markdown(f"**Tee Box:** {courses[selected_course]['tee_color']}")
st.markdown(f"**Yardage:** {hole['yardage']} yards")

# Show image
try:
    img = Image.open(hole["image"])
    st.image(img, caption=f"{selected_course} Hole {hole['number']}", use_column_width=True)
except:
    st.warning("Image not found.")

# Display Strategy
st.subheader("⛳ Strategy & Tips")
st.markdown(f"**Overview:** {hole['overview']}")
st.markdown(f"**Tee Shot Strategy:** {hole['tee_shot']}")
st.markdown(f"**Approach Game:** {hole['approach']}")
st.markdown(f"**Tee Tip:** {hole['tip']}")
