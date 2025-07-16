import streamlit as st
from PIL import Image
import os

# Set page config for mobile responsiveness
st.set_page_config(
    page_title="Coyote Moon Guide",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("\U0001F33F Coyote Moon Golf Course Guide")
st.subheader("Blue Tees - Hole-by-Hole Strategy")

# Directory containing hole images
IMAGE_DIR = "hole_images"  # Ensure this directory exists with hole1.jpg to hole18.jpg

# Full hole data
hole_data = [
    {"hole": 1, "par": 5, "yardage": 519, "image": "hole1.jpg", "description": "A strong yet scorable opener.", "tee_shot": "Aim left side off the tee to avoid being blocked out. Long hitters can reach in two; otherwise lay up to 115–145 yards.", "approach": "Wedge into a two-tiered green. Wrong tier = tough two-putt.", "tip": "Play it smart. Par is solid, birdie is in play."},
    {"hole": 2, "par": 4, "yardage": 404, "image": "hole2.jpg", "description": "Dogleg right with a narrow landing zone.", "tee_shot": "Favor left-center. Avoid bunker ~277 yds off tee.", "approach": "Short iron into a shallow green. Wind can affect club choice.", "tip": "Hit the fairway, wedge it tight. No need to muscle it."},
    {"hole": 3, "par": 3, "yardage": 186, "image": "hole3.jpg", "description": "Elevated tee makes this play shorter.", "tee_shot": "Club down 1–2 depending on wind.", "approach": "Avoid short left/right; center green is safe.", "tip": "Par is a win here."},
    {"hole": 4, "par": 4, "yardage": 426, "image": "hole4.jpg", "description": "Tough uphill hole with a sloping fairway.", "tee_shot": "Favor left-center to avoid right slope.", "approach": "Mid-iron to a shallow green. Hit the center tier.", "tip": "Avoid missing short or long."},
    {"hole": 5, "par": 4, "yardage": 389, "image": "hole5.jpg", "description": "Dogleg left. Tempting but tricky.", "tee_shot": "Don’t cut corner. 220-230 yd layup ideal.", "approach": "Wedge into a narrow green.", "tip": "Position > distance here."},
    {"hole": 6, "par": 4, "yardage": 377, "image": "hole6.jpg", "description": "Scenic short par 4.", "tee_shot": "Play a draw ~250 yds.", "approach": "Uphill wedge. Avoid short.", "tip": "Don’t chase the green."},
    {"hole": 7, "par": 5, "yardage": 507, "image": "hole7.jpg", "description": "Reachable par 5.", "tee_shot": "Left-center ~280 yds.", "approach": "Go for it or lay up to 130.", "tip": "Middle of green is gold."},
    {"hole": 8, "par": 3, "yardage": 158, "image": "hole8.jpg", "description": "Shortest hole, but no pushover.", "tee_shot": "Plays true. Wind swirls.", "approach": "Avoid right bunker.", "tip": "Order food here!"},
    {"hole": 9, "par": 4, "yardage": 406, "image": "hole9.jpg", "description": "Dogleg right with elevated green.", "tee_shot": "Right-center target.", "approach": "Watch distance control.", "tip": "Be on the right tier."},
    {"hole": 10, "par": 4, "yardage": 408, "image": "hole10.jpg", "description": "Strategic opening to back 9.", "tee_shot": "Fairway wood ~250 yds.", "approach": "Slightly uphill.", "tip": "Short > long here."},
    {"hole": 11, "par": 4, "yardage": 436, "image": "hole11.jpg", "description": "Deceptive downhill drive.", "tee_shot": "Aim just right of bunker.", "approach": "Right side is safest.", "tip": "Take the roll-out into account."},
    {"hole": 12, "par": 5, "yardage": 492, "image": "hole12.jpg", "description": "Favorable par 5.", "tee_shot": "Fade to ~265 yds.", "approach": "Lay up to 130 or go for it.", "tip": "Middle green = birdie chance."},
    {"hole": 13, "par": 3, "yardage": 206, "image": "hole13.jpg", "description": "Dramatic downhill par 3.", "tee_shot": "Plays 1-2 clubs shorter.", "approach": "Don’t chase pins.", "tip": "Take your 3 and run."},
    {"hole": 14, "par": 4, "yardage": 294, "image": "hole14.jpg", "description": "Short, narrow, and dangerous.", "tee_shot": "Hybrid/iron to 230-240.", "approach": "Over Trout Creek.", "tip": "Two smart shots win here."},
    {"hole": 15, "par": 5, "yardage": 567, "image": "hole15.jpg", "description": "Three-shot par 5.", "tee_shot": "Right-center ~280.", "approach": "Lay up left to 110-130.", "tip": "Avoid creek right."},
    {"hole": 16, "par": 3, "yardage": 183, "image": "hole16.jpg", "description": "Over water, into wind.", "tee_shot": "Favor left-center.", "approach": "Take extra club.", "tip": "Trust the yardage."},
    {"hole": 17, "par": 4, "yardage": 434, "image": "hole17.jpg", "description": "Epic elevated tee shot.", "tee_shot": "Right of pine tree.", "approach": "Tiered green slopes left.", "tip": "Middle green, 2 putts."},
    {"hole": 18, "par": 4, "yardage": 312, "image": "hole18.jpg", "description": "Finisher rewards discipline.", "tee_shot": "Hybrid/iron to 230-250.", "approach": "To 3-tier green, avoid bunkers.", "tip": "Walk off smart, not flashy."}
]

# Hole selector
hole_numbers = [f"Hole {hole['hole']}" for hole in hole_data]
selected_hole = st.selectbox("Select Hole", hole_numbers)
hole = next(h for h in hole_data if f"Hole {h['hole']}" == selected_hole)

# Load image
image_path = os.path.join(IMAGE_DIR, hole['image'])
if os.path.exists(image_path):
    st.image(Image.open(image_path), use_column_width=True)
else:
    st.warning("Image not found.")

# Display info
st.markdown(f"**Par {hole['par']} - {hole['yardage']} Yards**")
st.markdown(f"**Overview:** {hole['description']}")
st.markdown(f"**\U0001F3E4 Tee Shot Strategy:** {hole['tee_shot']}")
st.markdown(f"**\U0001F33F Approach Game:** {hole['approach']}")
st.markdown(f"**\U0001F539 Blue Tee Tip:** _{hole['tip']}_")

st.markdown("---")
st.caption("Optimized for mobile by Streamlit")
