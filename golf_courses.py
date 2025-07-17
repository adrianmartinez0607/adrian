import streamlit as st
from PIL import Image

# Hole data — tips + yardages from white tees
hole_data = {
    "1": {
        "Par": 5,
        "Yardage": 469,
        "Tips": "**Tee Shot:** Favor the left side to open up the fairway. Avoid the trees on the right.\n\n**Approach:** Long hitters may go for it in two (~245 carry), but the safe play is to lay up to 114\u2013146 yards, short of left bunkers.\n\n**Overall:** Play for position. A wedge into the two-tiered green gives a great birdie chance."
    },
    "2": {
        "Par": 4,
        "Yardage": 382,
        "Tips": "**Tee Shot:** Aim just left of the lone pine on the right. That line gives a clear approach.\n\n**Approach:** Wind can affect this shot from ~110\u2013130 yards. Green slopes back-to-front \u2014 do not go long.\n\n**Overall:** Controlled tee and smart club on approach = par or birdie."
    },
    "3": {
        "Par": 3,
        "Yardage": 156,
        "Tips": "**Tee Shot:** Elevated tee makes it play shorter. Knock off 1 club in calm or tailwind conditions.\n\n**Green:** Wide but narrow front-to-back. Avoid the bunker short left.\n\n**Overall:** Safe play is center of green \u2014 par is a solid score."
    },
    "4": {
        "Par": 4,
        "Yardage": 408,
        "Tips": "**Tee Shot:** Hit to the left-center of the sloped fairway. Avoid drifting right.\n\n**Approach:** Mid-iron uphill from 130\u2013150 yds. Take extra club but don\u2019t overshoot \u2014 the green slopes back to front.\n\n**Overall:** Precision off the tee and a confident uphill iron will give you a look at birdie."
    },
    "5": {
        "Par": 4,
        "Yardage": 369,
        "Tips": "**Tee Shot:** Dogleg left \u2014 aim at the left-center of fairway. Don\u2019t try to cut the corner.\n\n**Approach:** From ~150 yds, trust your club. Green shape and wind can make it tricky.\n\n**Overall:** Safe drive + smart club = great birdie hole."
    },
    "6": {
        "Par": 4,
        "Yardage": 354,
        "Tips": "**Tee Shot:** Slight draw around the corner is ideal. 215 yds puts you in wedge range.\n\n**Approach:** Elevated green \u2014 go middle. Don\u2019t attack tricky pins.\n\n**Overall:** Play for a short pitch and leave below the hole."
    },
    "7": {
        "Par": 5,
        "Yardage": 478,
        "Tips": "**Tee Shot:** Find the fairway. Favor the right-center to set up the second.\n\n**Second Shot:** Aggressive line requires 250+ carry over water. Lay up to ~110 is safer.\n\n**Overall:** Pick your battle. Layup route still leaves a wedge to a tight green."
    },
    "8": {
        "Par": 3,
        "Yardage": 127,
        "Tips": "**Tee Shot:** Wind and pin position dictate everything. Bunker guards the right.\n\n**Green:** Sloped and narrow. Play center and spin it.\n\n**Overall:** Don\u2019t chase pins \u2014 center is always safe."
    },
    "9": {
        "Par": 4,
        "Yardage": 377,
        "Tips": "**Tee Shot:** Slight dogleg right. Best line is right-center fairway.\n\n**Approach:** Downhill shot from 130\u2013140 yds. Green is guarded, so land soft.\n\n**Overall:** Great scoring hole if you control trajectory on approach."
    },
    "10": {
        "Par": 4,
        "Yardage": 389,
        "Tips": "**Tee Shot:** Use long iron or hybrid to right-center. Driver brings trouble.\n\n**Approach:** 120\u2013140 yds to a tight, elevated green. Be mindful of bunkers.\n\n**Overall:** Play smart off the tee, commit on the uphill second."
    },
    "11": {
        "Par": 4,
        "Yardage": 407,
        "Tips": "**Tee Shot:** Drop in elevation. Hit 3W or hybrid just right of fairway bunker.\n\n**Approach:** From 130\u2013150 yds. Green has movement, so stay right.\n\n**Overall:** Let the tee ball run, then play a controlled second."
    },
    "12": {
        "Par": 5,
        "Yardage": 458,
        "Tips": "**Tee Shot:** Favor a fade. Left miss is jail.\n\n**Second Shot:** Can go for it, but smart layup to 100\u2013120 yds avoids all trouble.\n\n**Overall:** This is a birdie hole \u2014 but only if you avoid the bunkers short right."
    },
    "13": {
        "Par": 3,
        "Yardage": 187,
        "Tips": "**Tee Shot:** Plays 1\u20133 clubs less downhill. Factor in wind.\n\n**Green:** Wide but shallow. Choose center regardless of pin.\n\n**Overall:** Commit to your club \u2014 this one\u2019s all about distance."
    },
    "14": {
        "Par": 4,
        "Yardage": 243,
        "Tips": "**Tee Shot:** Tight and short. Lay up to ~165 short of pine.\n\n**Approach:** Wedge over Trout Creek to shallow green. Tough pin positions.\n\n**Overall:** Smart tee shot + crisp wedge = par or better."
    },
    "15": {
        "Par": 5,
        "Yardage": 541,
        "Tips": "**Tee Shot:** Drive to right-center. Lots of room long.\n\n**Second Shot:** Lay up left side, avoiding right hazard.\n\n**Approach:** Into a two-tiered green \u2014 must carry the front.\n\n**Overall:** A true 3-shot hole. Don\u2019t get greedy."
    },
    "16": {
        "Par": 3,
        "Yardage": 161,
        "Tips": "**Tee Shot:** Usually into wind. Avoid short/right (water and bunker).\n\n**Green:** Plenty of space left. Middle is the safest spot.\n\n**Overall:** Play the wind \u2014 par is a win."
    },
    "17": {
        "Par": 4,
        "Yardage": 412,
        "Tips": "**Tee Shot:** Elevated tee. Aim just right of pine \u2014 breeze helps.\n\n**Approach:** From 130\u2013150 yds. Best angle is from right.\n\n**Overall:** Left side slopes hard \u2014 bail right if in doubt."
    },
    "18": {
        "Par": 4,
        "Yardage": 293,
        "Tips": "**Tee Shot:** Hybrid or FW to left-center (~230). Avoid fairway bunkers.\n\n**Approach:** Uphill into 3-tiered green. Know your pin.\n\n**Overall:** Final test. Choose your tier wisely and take your par."
    }
}

# Streamlit setup
st.set_page_config(page_title="Coyote Moon Course Guide", layout="wide")
st.title("⛳ Coyote Moon Golf Course Guide")
st.markdown("White Tee Yardages & Strategy")

# Hole selection
hole_number = st.sidebar.selectbox("Select Hole", list(range(1, 19)))
image_file = f"hole{hole_number}.jpg"

# Hole info display
st.subheader(f"Hole {hole_number} - Par {hole_data[hole_number]['Par']} - {hole_data[hole_number]['Yardage']} yds (White Tees)")

# Image display
try:
    img = Image.open(image_file)
    st.image(img, use_column_width=True)
except FileNotFoundError:
    st.warning(f"Image for Hole {hole_number} not found: `{image_file}` missing.")

# Tips
st.markdown("**Tips & Strategy:**")
st.markdown(hole_data[hole_number]["Tips"])

# Footer
st.markdown("---")
st.caption("Mobile-optimized | Designed for on-course use.")
