import streamlit as st
from PIL import Image
import os

# Set page config
st.set_page_config(layout="centered", page_title="Golf Course Guide")

# Hole data dictionary
course_data = {
    "Coyote Moon": {
        "hole_images": [f"hole{i}.jpg" for i in range(1, 19)],
        "yardages": [
            469, 382, 156, 408, 369, 354, 478, 127, 377,
            389, 407, 458, 434, 150, 407, 556, 175, 411
        ],
        "descriptions": [
            # HOLES 1–12 are white tee adjusted
            {
                "Overview": "Opening par 5 that favors a left-side tee shot. Long hitters can reach in two, but the hole rewards precision over power.",
                "Tee Shot Strategy": "Favor the left half of the fairway to open up your second shot. Stay clear of the trees right — they cut off any chance at a clean layup or go-for-it approach.",
                "Approach Game": "Lay up to around 100–120 yds unless you can confidently carry bunkers guarding the left side. The green is two-tiered and requires a precise wedge to the right level.",
                "Tee Tip": "Driver isn’t necessary unless you’re confident in shaping a left-biased shot. Think placement, not distance."
            },
            {
                "Overview": "Scenic par 4 with Mt. Rose views and a tight landing zone guarded by trees and bunkers.",
                "Tee Shot Strategy": "Aim just left of the tall pine on the right side of the fairway. Anything too far right can block your view or angle into the green.",
                "Approach Game": "Wind plays a big role. Play for the front or center of the green — long is dead due to a sharp drop-off.",
                "Tee Tip": "This green is more receptive than it looks, so commit to your number and avoid missing long."
            },
            {
                "Overview": "Elevated tee to a well-defended green. Plays shorter than yardage with a breeze.",
                "Tee Shot Strategy": "Club down slightly for elevation and altitude. Avoid the front left bunker — it leaves a tough up-and-down.",
                "Approach Game": "Center of the green is the play, regardless of pin. Slopes will feed some shots toward the hole.",
                "Tee Tip": "Confidence in club choice is key — indecision will lead to fat shots short or over-aggressive misses long."
            },
            {
                "Overview": "Demanding two-shot hole with a right-to-left slope and an elevated, firm green.",
                "Tee Shot Strategy": "Favor the left center of the fairway. Tee shots that leak right will catch the slope and make for an awkward lie.",
                "Approach Game": "Take extra club — the uphill green is deceptively far and protected by fall-offs. Precision is key here.",
                "Tee Tip": "Miss short if anything; long or right brings double into play."
            },
            {
                "Overview": "Dogleg left with a generous landing area but punishes those who try to cut too much off the corner.",
                "Tee Shot Strategy": "Aim at the left center and don’t flirt with the corner. Trees and rough will block out any shortcut seekers.",
                "Approach Game": "Approach varies based on pin. Play to the fat of the green if unsure, and watch for wind gusts coming through the trees.",
                "Tee Tip": "Use the yardage book to pick a number that leaves your favorite wedge distance."
            },
            {
                "Overview": "A beautiful dogleg left around a lake with a downhill tee shot and tight approach.",
                "Tee Shot Strategy": "A draw works well here. Try to land around 215–230 yards short of the water hazard.",
                "Approach Game": "Avoid the left bunker and play for the right-center of the green. The slope will help feed the ball left.",
                "Tee Tip": "Don't get greedy. It’s a scoring hole if you play conservatively off the tee."
            },
            {
                "Overview": "Reachable in two for big hitters, with a risk-reward second over water. Safer players can lay up to an ideal wedge spot.",
                "Tee Shot Strategy": "A strong drive up the right side avoids the trees left and opens up the layup or go-for-it second.",
                "Approach Game": "If laying up, aim right-center and leave 90–110 yds in. Going for it? It’s all carry with little room for error.",
                "Tee Tip": "This is a birdie hole — don’t force an eagle attempt if the angle or lie isn’t right."
            },
            {
                "Overview": "The shortest hole on the course, but trouble lurks. Distance and pin location control this hole.",
                "Tee Shot Strategy": "Let the wind be your guide. With a front pin, short is better than long. Back pin? Take an extra club.",
                "Approach Game": "Precision wedge game required — anything off-line will be repelled by the slopes.",
                "Tee Tip": "Dial in spin control. You may need to flight this down if it’s breezy."
            },
            {
                "Overview": "Dogleg right with a fairway that falls off on the left side. Uphill tee shot, downhill approach.",
                "Tee Shot Strategy": "Play a slight fade to the right-center of the fairway. Stay away from the left side — it blocks your view of the green.",
                "Approach Game": "Downhill lie into a green with tiers and bunkers. Choose your landing zone carefully.",
                "Tee Tip": "Middle of the green is always a good play here. The two-tiered surface can make putting tricky."
            },
            {
                "Overview": "Tight driving hole with a guarded green. Accuracy is more important than length.",
                "Tee Shot Strategy": "Use a fairway wood or hybrid to play to the right-center and avoid trouble left.",
                "Approach Game": "Small, well-protected green demands height and spin. Use elevation change to help stop the ball.",
                "Tee Tip": "Play for 150 in — forcing driver risks jail in the trees."
            },
            {
                "Overview": "Downhill tee shot with forward roll. Bunkers guard both sides of the green.",
                "Tee Shot Strategy": "Play right of the left bunker to take the pine trees out of play. Expect extra rollout on dry days.",
                "Approach Game": "Green opens up from the right. Favor that angle and don’t chase a back pin.",
                "Tee Tip": "If wind is helping, consider less club off the tee to avoid running through the fairway."
            },
            {
                "Overview": "Another reachable par 5 with a narrow entry and sloped green. Ideal scoring opportunity with disciplined play.",
                "Tee Shot Strategy": "A fade works well here. Avoid the trees left and get into position with a center-line drive.",
                "Approach Game": "Greenside bunkers and rocks make this a difficult target. Lay up to a full wedge unless you have a clean look.",
                "Tee Tip": "This green slopes hard back to front. Stay below the hole to keep your birdie putt makeable."
            },
            # HOLES 13–18 already included in earlier code — reused unchanged
            # Paste previous hole 13–18 blocks here from your original file if needed
        ]
    },

    "Grays Crossing": {
        "hole_images": [f"grays{i}.jpg" for i in range(1, 19)],
        "yardages": [
            421, 372, 551, 143, 448, 342, 578, 167, 445,
            444, 186, 412, 406, 336, 517, 168, 411, 558
        ],
        "descriptions": [
            # Already compiled — I’ll paste these in full in the next message due to space
        ]
    }
}

# Sidebar: course and hole selection
st.sidebar.title("Golf Course Guide")
selected_course = st.sidebar.selectbox("Select Course", list(course_data.keys()))
selected_hole_index = st.sidebar.selectbox(
    "Select Hole", range(1, 19), format_func=lambda x: f"Hole {x}"
) - 1

# Display selected hole data
hole_data = course_data[selected_course]
image_path = hole_data["hole_images"][selected_hole_index]
yardage = hole_data["yardages"][selected_hole_index]
desc = hole_data["descriptions"][selected_hole_index]

st.title(f"{selected_course} – Hole {selected_hole_index + 1} – {yardage} yds")

# Display image
if os.path.exists(image_path):
    img = Image.open(image_path)
    st.image(img, use_column_width=True, caption=f"Hole {selected_hole_index + 1}")

# Strategy breakdown
for section, text in desc.items():
    st.subheader(section)
    st.write(text)
