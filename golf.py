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
        "yardage": 404,
        "description": "A tight and beautiful par 4 framed by pines with a postcard view of Mt. Rose.",
        "tee_shot": "- Aim just left of the pine tree on the right side of the fairway.\n- A 277-yard drive reaches the fairway bunker — consider clubbing down.\n- Trees right and bunker left make the fairway your only option.",
        "approach": "- Short wedge approach of 130–86 yards.\n- Swirling winds can confuse club selection.\n- Green is only 28 yards deep — long is dead.",
        "tip": "Play safe to the front portion of the green. Two smart shots here beat a gamble."
    },
    {
        "hole": 3,
        "image": "hole3.jpg",
        "par": 3,
        "yardage": 186,
        "description": "A picturesque par 3 with elevation and swirling winds — looks simple, plays sneaky tough.",
        "tee_shot": "- Plays slightly shorter due to elevation.\n- Wind can swirl — commit to your club and line.\n- Miss short right for a better chance at an up-and-down.",
        "approach": "- Green is 33 yards deep with soft back-to-front slope.\n- Better to be short than long — long leaves a brutal chip.\n- Middle green is always a safe target.",
        "tip": "Par is a win here. Trust your number and swing smooth."
    },
    {
        "hole": 4,
        "image": "hole4.jpg",
        "par": 4,
        "yardage": 426,
        "description": "A true test of ball striking. Two precise shots required — and uphill all the way.",
        "tee_shot": "- Aim left-center. The fairway slopes right and can kick balls into trouble.\n- 271 yards from blue tees lands near the start of the uphill slope.",
        "approach": "- Mid-iron uphill to a shallow 21-yard green.\n- Take an extra club — short leaves a tough chip.\n- Long is no good — chip back is slick.",
        "tip": "Respect the slope. Play your approach to the middle and keep it below the hole."
    },
    {
        "hole": 5,
        "image": "hole5.jpg",
        "par": 4,
        "yardage": 389,
        "description": "A classic risk-reward dogleg left that punishes greed and rewards precision.",
        "tee_shot": "- Play to left-center. Don’t cut the corner unless confident.\n- 218–232 yard drive puts you in perfect wedge range.",
        "approach": "- 85–125 yard approach into a green 39 yards wide.\n- Green is guarded right by a bunker.\n- Favor center-left.",
        "tip": "Two smart shots get you a birdie chance. Don’t force it off the tee."
    },
    {
        "hole": 6,
        "image": "hole6.jpg",
        "par": 4,
        "yardage": 377,
        "description": "A picturesque dogleg left with water, trees, and one of the tightest approach angles on the course.",
        "tee_shot": "- Slight draw around the corner sets you up well.\n- 251–266 yards puts you at the corner.\n- Right side leaves blocked approach.",
        "approach": "- Short pitch of 85–125 yards over Trout Creek.\n- Green is 33 yards deep with guarded edges.\n- Avoid chasing back pins.",
        "tip": "Rewarding hole if positioned properly. Play to the corner, pitch it up, and avoid the sucker pins."
    },
    {
        "hole": 7,
        "image": "hole7.jpg",
        "par": 5,
        "yardage": 507,
        "description": "A reachable par 5 with a risk-reward second shot. Birdie is in play — but only if you earn it.",
        "tee_shot": "- Target left-center of the fairway.\n- 281–305 yard drive gives you a green light to go.\n- Fairway is generous but bordered by trees.",
        "approach": "- Go for it? You’ll need 215–230 yards uphill.\n- Lay up to 130–150 yard range for full wedge.\n- Green is narrow and guarded.",
        "tip": "Don’t force the hero shot. Lay up smartly if lie or angle is poor — wedge it close."
    },
    {
        "hole": 8,
        "image": "hole8.jpg",
        "par": 3,
        "yardage": 158,
        "description": "The shortest hole on the course, but don’t sleep on it — distance control is everything.",
        "tee_shot": "- Plays true but wind swirls.\n- Pick a target that splits the green.\n- Bunker front-right in play.",
        "approach": "- 36-yard deep green — pin placement affects club choice.\n- Short is safer than long.",
        "tip": "Don’t chase. Center of the green is a win. Use the call box to order food!"
    },
    {
        "hole": 9,
        "image": "hole9.jpg",
        "par": 4,
        "yardage": 406,
        "description": "Finishing the front nine with a classic Tahoe-style dogleg right.",
        "tee_shot": "- Right-center is ideal.\n- 286–300 yard drive sets up a downhill second.\n- Avoid bailing right. More room left than it seems.",
        "approach": "- 110–130 yards to a two-tier green 36 yards deep.\n- Distance control is crucial.\n- Wrong tier = difficult two-putt.",
        "tip": "Dial back off the tee for position. Wedge it close and finish the front strong."
    }
    # Add holes 10–18 here in the same format...
]

# Hole selector dropdown
hole_numbers = [f"Hole {hole['hole']}" for hole in hole_data]
selected_hole = st.selectbox("Select Hole", hole_numbers)
hole = next(h for h in hole_data if f"Hole {h['hole']}" == selected_hole)

# Load image
image_path = os.path.join(IMAGE_DIR, hole['image'])
if os.path.exists(image_path):
    st.image(Image.open(image_path), use_column_width=True)
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
