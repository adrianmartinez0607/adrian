import streamlit as st
from PIL import Image

st.set_page_config(layout="centered")

# Course definitions
courses = {
    "Coyote Moon": {
        "tees": "White",
        "holes": [
            {"number": i, "image": f"hole{i}.jpg", "yardage": y}
            for i, y in enumerate(
                [485, 365, 190, 410, 330, 380, 195, 540, 425,
                 365, 185, 400, 425, 190, 525, 355, 175, 510], start=1)
        ]
    },
    "Grays Crossing": {
        "tees": "Stampede (Gold)",
        "holes": [
            {"number": i, "image": f"grays{i}.jpg", "yardage": y}
            for i, y in enumerate(
                [405, 375, 585, 165, 420, 325, 580, 185, 455,
                 395, 205, 420, 435, 340, 535, 175, 410, 555], start=1)
        ]
    }
}

# Strategy content (partial example — fill in all holes)
strategy = {
    ("Coyote Moon", 1): {
        "overview": "Short par 5 from the white tees, reachable in two for many. Ideal opener for confident strikers.",
        "tee_shot": "Left side of fairway gives the best angle. Avoid the right trees which close off the second shot.",
        "approach": "Lay up short of the bunker cluster unless you're going for it. Green has depth and slope.",
        "tip": "Use a 3-wood or hybrid if your driver is unreliable — position matters more than distance."
    },
    ("Grays Crossing", 1): {
        "overview": "A challenging start into the prevailing wind with a gentle dogleg right.",
        "tee_shot": "Favor the left side of the fairway to open up the angle. Long hitters can try cutting the corner.",
        "approach": "Aim left of the right-side bunker. A mid-iron shot usually remains.",
        "tip": "Use a 3-wood or hybrid off the tee for control unless you’re confident in shaping a driver."
    },
    # Continue adding entries for all 36 holes
}

# Sidebar layout
st.sidebar.title("Golf Yardage & Strategy")
selected_course = st.sidebar.selectbox("Select Course", list(courses.keys()))
selected_hole_num = st.sidebar.selectbox("Select Hole", range(1, 19))
hole = courses[selected_course]["holes"][selected_hole_num - 1]

# Main content
st.title(f"{selected_course} – Hole {hole['number']}")
st.markdown(f"**Tee Box:** {courses[selected_course]['tees']}")
st.markdown(f"**Yardage:** {hole['yardage']} yards")

# Image
try:
    img = Image.open(hole['image'])
    st.image(img, use_column_width=True)
except:
    st.warning("Image not found for this hole.")

# Strategy Section
key = (selected_course, hole['number'])
if key in strategy:
    st.markdown("### Strategy & Tips")
    st.markdown(f"**Overview:** {strategy[key]['overview']}")
    st.markdown(f"**Tee Shot Strategy:** {strategy[key]['tee_shot']}")
    st.markdown(f"**Approach Game:** {strategy[key]['approach']}")
    st.markdown(f"**Tee Tip:** {strategy[key]['tip']}")
else:
    st.info("Strategy tips not available for this hole yet.")
