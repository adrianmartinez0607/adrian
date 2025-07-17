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
            "tee": tee,
            "approach": approach,
            "tip": tip
        } for i, (tee, approach, tip) in enumerate([
            ("Favor the left side off the tee.", "Wedge approach into a two-tier green.", "Precision off the tee sets up birdie."),
            ("Club up slightly on this uphill par 3.", "Aim for center of green.", "Avoid going long — par is solid."),
            ("Drive left side for angle.", "Lay up or go for it.", "Smart second shot gives wedge in."),
            ("Cut the corner with a fade.", "Favor left side of green.", "Avoid bunkers short and right."),
            ("Club down on downhill par 3.", "Short is safe.", "Don't chase back pins."),
            ("Tee shot to right side.", "Lay up left center.", "Wedge it close from 100 yards."),
            ("Tight fairway — aim high fade.", "Left side of green is safe.", "Don’t short-side yourself."),
            ("Favor right side to avoid bunkers.", "Mid-iron to undulating green.", "Smart tee shot gives great birdie chance."),
            ("Draw to center.", "Long iron into shallow green.", "Par is a strong finish."),
            ("Between bunkers is perfect.", "Wind helps approach play short.", "Green is tricky — stay safe side."),
            ("Favor right — terrain helps.", "Avoid deep left bunker.", "Aim center and spin it."),
            ("Wide landing — aim left.", "Carry bunkers to center green.", "Premium on accuracy from fairway."),
            ("Accuracy over power.", "Play to middle.", "Stay dry and smart."),
            ("3W or hybrid to right side.", "Wedge in to tricky green.", "Great birdie chance if smart."),
            ("Right fairway gives slope.", "Lay up or go.", "Third shot must be sharp."),
            ("Club down 1–3.", "High, soft landing.", "Middle of green is safe."),
            ("Don’t blow it past fairway.", "Hard green to hold.", "Control spin and height."),
            ("Aim right-center.", "Lay up left or cut right fairway.", "Strong finish if managed well.")
        ], 1)
    },
    "Grays Crossing": {
        f"Hole {i}": {
            "image": f"grays{i}.jpg",
            "tee": tee,
            "approach": approach,
            "tip": tip
        } for i, (tee, approach, tip) in enumerate([
            ("Play into the wind, favor left side.", "Medium iron to green with right bunkers.", "Positional tee shot sets up par or better."),
            ("Club to stay short of left bunker.", "Short to mid-iron to sloped green.", "Smart tee placement opens up birdie look."),
            ("Tee it high downwind, favor left.", "Medium iron avoiding left bunkers.", "Wedge in or go for green over last bunker."),
            ("Watch wind, club up.", "Favor right side.", "Par is a good score here."),
            ("Right side safe, tall pine is riskier.", "Downhill, downwind — plays short.", "Play front of green, long is dead."),
            ("Carry right bunkers for eagle chance.", "Green slopes hard front/back + right/left.", "Pick your risk: drive or wedge."),
            ("Downwind — long hitters attack in 2.", "Favor left side — slope right.", "Precision into shallow green required."),
            ("Quartering wind right-to-left.", "Avoid pond left + bunkers right.", "Trust yardage. Par is solid."),
            ("Tee down right — bounce left.", "Uphill approach — extra club.", "Green slopes hard back-to-front."),
            ("Between right bunkers ideal.", "Wind helps — plays short.", "Tough green. Favor safe side."),
            ("Aim right — slope feeds left.", "Avoid deep left bunker.", "Accurate iron sets up birdie chance."),
            ("Generous fairway — aim left.", "Deep bunkers guard both sides.", "Hit the fairway and strike a solid approach."),
            ("Prevailing wind, accuracy crucial.", "Water guards green.", "Par requires two confident shots."),
            ("Long hitters may go green.", "Wedge from right fairway.", "Safest route: lay up and wedge close."),
            ("Favor right — slope helps.", "Lay up right.", "Third shot to shallow green must be precise."),
            ("Downhill — 1–3 clubs less.", "Middle of green is smart.", "Control distance and trajectory."),
            ("Wind at back — fairway runs out.", "Mid-iron to fast, firm green.", "Play safe tee, precise second."),
            ("Right-center tee best.", "Lay up left or go right fairway.", "Three-shot hole unless you're elite."),
        ], 1)
    }
}

# Hole selector
selected_hole = st.selectbox("Select Hole", list(data[course].keys()))
hole_info = data[course][selected_hole]

# Hole image
st.image(hole_info["image"], use_container_width=True)

# Tips & Strategy
st.markdown("## Tips & Strategy")
st.markdown(f"""
**<span style='font-size:18px'>Tee Shot:</span>** <span style='font-size:16px'>{hole_info['tee']}</span><br><br>
**<span style='font-size:18px'>Approach:</span>** <span style='font-size:16px'>{hole_info['approach']}</span><br><br>
**<span style='font-size:18px'>Overall:</span>** <span style='font-size:16px'>{hole_info['tip']}</span>
""", unsafe_allow_html=True)
