import streamlit as st
from PIL import Image
import os

# Set page config for mobile responsiveness
st.set_page_config(
    page_title="Coyote Moon Guide",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("🌿 Coyote Moon Golf Course Guide")
st.subheader("Blue Tees - Hole-by-Hole Strategy")

# Directory containing hole images
IMAGE_DIR = "hole_images"  # Change this to your actual image directory

# Hole data (can be loaded from JSON or API in future)
hole_data = [
    {
        "hole": 1,
        "par": 5,
        "yardage": 519,
        "image": "hole1.jpg",
        "description": "A strong yet scorable opener.",
        "tee_shot": "Aim left side off the tee to avoid being blocked out. Long hitters can reach in two; otherwise lay up to 115–145 yards.",
        "approach": "Wedge into a two-tiered green. Wrong tier = tough two-putt.",
        "tip": "Play it smart. Par is solid, birdie is in play."
    },
    {
        "hole": 2,
        "par": 4,
        "yardage": 404,
        "image": "hole2.jpg",
        "description": "Dogleg right with a narrow landing zone.",
        "tee_shot": "Favor left-center. Avoid bunker ~277 yds off tee.",
        "approach": "Short iron into a shallow green. Wind can affect club choice.",
        "tip": "Hit the fairway, wedge it tight. No need to muscle it."
    },
    # Add holes 3-18 here...
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
st.markdown(f"**🏤 Tee Shot Strategy:** {hole['tee_shot']}")
st.markdown(f"**🌿 Approach Game:** {hole['approach']}")
st.markdown(f"**🔹 Blue Tee Tip:** _{hole['tip']}_")

st.markdown("---")
st.caption("Optimized for mobile by Streamlit")
