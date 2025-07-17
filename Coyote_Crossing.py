import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="Course Guide", layout="centered")
st.title("⛳ Golf Course Yardage & Strategy")

# Course selector
course = st.selectbox("Select Course", ["Coyote Moon", "Grays Crossing"])

# Course-specific hole data
data = {
    "Coyote Moon": {
        f"Hole {i}": {
            "image": f"hole{i}.jpg",
            "description": desc
        } for i, desc in enumerate([
            "Hole 1 | 379 Yards | A precise tee shot is crucial to avoid the bunkers lining both sides. On your approach, aim to land short and let it release to a back-to-front sloped green.",
            "Hole 2 | 158 Yards | A short par 3 that plays slightly uphill. Club up and stay below the hole — anything long brings bogey into play.",
            "Hole 3 | 500 Yards | Favor the left side off the tee for the best angle in. Play smart with your second and give yourself a wedge into a narrow green guarded front and left.",
            "Hole 4 | 375 Yards | This dogleg right rewards a cut off the tee. Approach shots should favor the left side to avoid bunkers short and right.",
            "Hole 5 | 168 Yards | A downhill par 3 — club down and trust the wind. Missing short is safe; long is jail.",
            "Hole 6 | 524 Yards | Long hitters can reach in two. Safer play is a tee shot to the right, a lay-up left of center, and a wedge in.",
            "Hole 7 | 420 Yards | Trees frame a tight fairway. A high fade works well here. Green slopes hard left — don’t chase pins.",
            "Hole 8 | 391 Yards | A demanding tee shot. Favor right side to avoid bunkers. Mid-iron approach to an undulating green.",
            "Hole 9 | 437 Yards | Into the wind, this plays long. Fairway narrows at 250. Hit a draw to center. Long iron into a shallow green.",
            "Hole 10 | 372 Yards | A tee shot between the bunkers puts you in good position. Second shot plays short with the wind. This green is tough — favor the safe side.",
            "Hole 11 | 152 Yards | Target right side of green. Terrain feeds the ball left. Avoid the deep bunker on the left at all costs.",
            "Hole 12 | 413 Yards | Wide fairway. Aim left off tee for best angle. Approach must carry two bunkers protecting a deep green.",
            "Hole 13 | 412 Yards | Water guards the entire right side. Play safe left, then a conservative approach to the center of the green.",
            "Hole 14 | 334 Yards | Tempting to drive it, but danger lurks. Safer play: 3-wood to right side, then wedge in.",
            "Hole 15 | 525 Yards | A birdie hole if played smart. Stay right on drive and lay-up. Third shot requires a precise wedge to a firm green.",
            "Hole 16 | 194 Yards | Downhill par 3 plays 1–3 clubs short. Focus on solid contact and distance control.",
            "Hole 17 | 354 Yards | Wind helps. Don’t overshoot fairway. A precise approach is needed to a slick green.",
            "Hole 18 | 475 Yards | Tough closer. Play center-right off tee. Lay up short left for best angle. Big hitters can cut right fairway for eagle chance."
        ], 1)
    },
    "Grays Crossing": {
        f"Hole {i}": {
            "image": f"grays{i}.jpg",
            "description": desc
        } for i, desc in enumerate([
            "Hole 1 | 405 Yards | A straightaway par four with trees tight left and bunkers right. Drive center-left and attack a wide, flat green.",
            "Hole 2 | 175 Yards | Par three with a narrow green tucked left. Play center or right edge and let the slope feed it.",
            "Hole 3 | 410 Yards | Avoid left off the tee. Approach plays slightly uphill into a green sloping back to front.",
            "Hole 4 | 389 Yards | Tee shot should favor left side. Green has two tiers — know the pin placement.",
            "Hole 5 | 550 Yards | Long par five. Favor left off the tee and right on lay-up. Avoid bunkers left of green.",
            "Hole 6 | 182 Yards | Elevated tee. Club down and watch the wind. Don’t miss short left.",
            "Hole 7 | 443 Yards | A dogleg right with trees everywhere. Drive must cut corner. Play approach to front-right.",
            "Hole 8 | 388 Yards | Strategic hole. Hybrid or 3-wood off tee, then wedge in. Stay below hole.",
            "Hole 9 | 502 Yards | Reachable in two. Risk-reward par five. Water lurks right. Left side is safer.",
            "Hole 10 | 372 Yards | Drive between right bunkers. Wind helps on approach — stay center.",
            "Hole 11 | 152 Yards | Pin-point par 3. Left bunker is jail. Right side will feed toward green center.",
            "Hole 12 | 413 Yards | Best angle is from left side. Green is guarded tight — take your time.",
            "Hole 13 | 412 Yards | Water all the way. Fairway is tight. Safe play is always best.",
            "Hole 14 | 334 Yards | Go for it if confident. Or lay up to right center. Trickiest green on the course.",
            "Hole 15 | 525 Yards | Play smart: right fairway, right lay-up, wedge it close. Short green demands precision.",
            "Hole 16 | 194 Yards | Plays 1–3 clubs short downhill. Middle of green is golden.",
            "Hole 17 | 354 Yards | Wind helps. Lay up short of bunker. Toughest green to hold.",
            "Hole 18 | 475 Yards | Long finish. Aim right off tee, lay-up left. Big hitter? Go across to right fairway."
        ], 1)
    }
}

# Hole selector
selected_hole = st.selectbox("Select Hole", list(data[course].keys()))
hole_info = data[course][selected_hole]

# Hole image and description
st.image(hole_info["image"], use_container_width=True)
st.markdown(f"**{hole_info['description']}**")
