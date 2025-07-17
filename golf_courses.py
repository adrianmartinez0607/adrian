import streamlit as st
from PIL import Image

# Hole data — tips + yardages from white tees
hole_data = {
    1:  {"Par": 5, "Yardage": 469, "Tips": "Favor the left side off the tee. Lay up to 146–114 yds short of bunkers for a wedge into a two-tiered green."},
    2:  {"Par": 4, "Yardage": 382, "Tips": "Aim left of the right pine. Approach plays best from 130–110 yds. Stay short — long is dead."},
    3:  {"Par": 3, "Yardage": 156, "Tips": "Elevated tee — plays shorter. Favor center or left. Par is a good score."},
    4:  {"Par": 4, "Yardage": 408, "Tips": "Left-center tee shot sets up a mid-iron approach. Uphill shot — stay short of back slope."},
    5:  {"Par": 4, "Yardage": 369, "Tips": "Dogleg left — don’t cut corner. Aim left center. Approach is 150–120 yds and wind-sensitive."},
    6:  {"Par": 4, "Yardage": 354, "Tips": "Play a draw around corner to ~215. Wedge in to deceptive green — short is safe."},
    7:  {"Par": 5, "Yardage": 478, "Tips": "Good drive gives green-light for two. Otherwise lay up to 110 yds. Water right and short."},
    8:  {"Par": 3, "Yardage": 127, "Tips": "Check wind. Green slopes right. Stay center or left — short or right brings bogey."},
    9:  {"Par": 4, "Yardage": 377, "Tips": "Aim right-center. You’ll face 130–140 yds downhill. Green is two-tiered — dial in distance."},
    10: {"Par": 4, "Yardage": 389, "Tips": "Use long iron/fairway wood to right-center. Approach is 120–140 yds into well-guarded green."},
    11: {"Par": 4, "Yardage": 407, "Tips": "Use hybrid/3W off tee — you'll roll out. Approach favors right side. Expect 130–150 yds in."},
    12: {"Par": 5, "Yardage": 458, "Tips": "Favorable for birdies. Left-to-right tee shot preferred. Go for it or lay up to 100–120. Green slopes hard back-to-front."},
    13: {"Par": 3, "Yardage": 187, "Tips": "Elevated tee — subtract 1–3 clubs. Aim center. Bunkers both sides make misses costly."},
    14: {"Par": 4, "Yardage": 243, "Tips": "Lay up short of pine (~165). Approach crosses creek to a shallow, undulating green."},
    15: {"Par": 5, "Yardage": 541, "Tips": "Three-shot hole. Tee to right center, second to left. Mid/short iron into two-tier green."},
    16: {"Par": 3, "Yardage": 161, "Tips": "Usually into wind — add a club. Avoid short/right. Plenty of space left."},
    17: {"Par": 4, "Yardage": 412, "Tips": "From elevated tee, aim right of pine. Approach from right side into a sloped green."},
    18: {"Par": 4, "Yardage": 293, "Tips": "Fairway wood to left-center (~230). Uphill approach to a three-tiered green. Avoid bunkers short."},
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
