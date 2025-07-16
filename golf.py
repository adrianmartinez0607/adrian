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

# Directory containing hole images in the root folder
IMAGE_DIR = "."

# Manual hole data for holes 1–18
hole_data = [
    {
        "hole": 1,
        "image": "hole1.jpg",
        "par": 5,
        "yardage": 519,
        "description": "A strong yet scorable opener that demands precision and smart decision-making.",
        "tee_shot": "- Target the left side of the fairway to avoid being blocked by trees.\n- Trees on the right tighten quickly and can ruin your hole.\n- A drive past 278 yards puts you in range to go for the green in two.",
        "approach": "- Ideal lay-up lands in the 146–114 yard range.\n- Avoid the left-side bunkers near the green.\n- Green is two-tiered; landing on the wrong tier means a three-putt is likely.",
        "tip": "Don't get greedy on your second shot if you're not clear of the trees. Par is great, birdie is a bonus."
    },
    {
        "hole": 2,
        "image": "hole2.jpg",
        "par": 4,
        "yardage": 374,
        "description": "A tight par 4 that places a premium on accuracy from the tee and offers birdie chances for strategic players.",
        "tee_shot": "- A fairway wood or long iron is often the play.\n- Aim just right of the fairway bunker.\n- The fairway narrows quickly, and distance control is key.",
        "approach": "- This green is shallow and well protected.\n- Landing short and bouncing on is better than flying the pin.\n- Beware the ridge running through the center.",
        "tip": "Commit to a conservative tee shot; taking driver brings big numbers into play."
    },
    {
        "hole": 3,
        "image": "hole3.jpg",
        "par": 3,
        "yardage": 207,
        "description": "A long, slightly downhill par 3 that plays to a multi-tiered green guarded by bunkers.",
        "tee_shot": "- Choose your club based on wind and pin.\n- Avoid the bunkers left and short.\n- Long and left is safe if you’re between clubs.",
        "approach": "- If you miss, favor the left side for an easier up-and-down.\n- The green slopes back to front with subtle ridges.\n- Putting from the wrong tier is a challenge.",
        "tip": "Focus on finding the green—par is an excellent score here."
    },
    # Holes 4 through 18 placeholder data
] + [
    {
        "hole": i,
        "image": f"hole{i}.jpg",
        "par": 4 if i in [4, 6, 7, 10, 11, 14, 17, 18] else (3 if i in [5, 13, 16] else 5),
        "yardage": 400 + i,  # placeholder yardage for demonstration
        "description": f"Description for hole {i}...",
        "tee_shot": f"- Tee shot strategy for hole {i}.\n- Avoid trouble left/right depending on layout.",
        "approach": f"- Approach game plan for hole {i}.\n- Know where the pin is on the green.",
        "tip": f"Blue tee tip for hole {i}."
    }
    for i in range(4, 19)
]

# Hole selector dropdown
hole_numbers = [f"Hole {hole['hole']}" for hole in hole_data]
selected_hole = st.selectbox("Select Hole", hole_numbers)
hole = next(h for h in hole_data if f"Hole {h['hole']}" == selected_hole)

# Load image and resize to 60% of original
image_path = os.path.join(IMAGE_DIR, hole['image'])
if os.path.exists(image_path):
    image = Image.open(image_path)
    width, height = image.size
    resized_image = image.resize((int(width * 0.6), int(height * 0.6)))
    st.image(resized_image, use_container_width=True)
else:
    st.warning(f"Image not found: {hole['image']}. Make sure it's in the same directory as the script.")

# Display hole data
st.markdown(f"**Par {hole['par']} - {hole['yardage']} Yards**")
st.markdown(f"**Overview:** {hole['description']}")
st.markdown("**\U0001F3E4 Tee Shot Strategy:**")
st.markdown(hole['tee_shot'])
st.markdown("**\U0001F33F Approach Game:**")
st.markdown(hole['approach'])
st.markdown("**\U0001F539 Blue Tee Tip:**")
st.markdown(f"_{hole['tip']}_")

st.markdown("---")
st.caption("Optimized for mobile by Streamlit")
