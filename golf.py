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

# Full hole data (expanded with full descriptions)
hole_data = [
    {
        "hole": 1,
        "par": 5,
        "yardage": 519,
        "image": "hole1.jpg",
        "description": "A strong yet scorable opener that demands precision and smart decision-making.",
        "tee_shot": "\n- Target the left side of the fairway to avoid being blocked by trees.\n- Trees on the right tighten quickly and can ruin your hole.\n- A drive past 278 yards puts you in range to go for the green in two.",
        "approach": "\n- Ideal lay-up lands in the 146–114 yard range.\n- Avoid the left-side bunkers near the green.\n- Green is two-tiered; landing on the wrong tier means a three-putt is likely.",
        "tip": "Don't get greedy on your second shot if you're not clear of the trees. Par is great, birdie is a bonus."
    },
    {
        "hole": 2,
        "par": 4,
        "yardage": 404,
        "image": "hole2.jpg",
        "description": "A tight and beautiful par 4 framed by pines with a postcard view of Mt. Rose.",
        "tee_shot": "\n- Aim just left of the pine tree on the right side of the fairway.\n- A 277-yard drive reaches the fairway bunker — consider clubbing down.\n- Trees right and bunker left make the fairway your only option.",
        "approach": "\n- Short wedge approach of 130–86 yards.\n- Swirling winds can confuse club selection.\n- Green is only 28 yards deep — long is dead.",
        "tip": "Play safe to the front portion of the green. Two smart shots here beat a gamble."
    },
    {
        "hole": 3,
        "par": 3,
        "yardage": 186,
        "image": "hole3.jpg",
        "description": "A picturesque par 3 with elevation and swirling winds — looks simple, plays sneaky tough.",
        "tee_shot": "
- Plays slightly shorter due to elevation.
- Wind can swirl — commit to your club and line.
- Miss short right for a better chance at an up-and-down.",
        "approach": "
- Green is 33 yards deep with soft back-to-front slope.
- Better to be short than long — long leaves a brutal chip.
- Middle green is always a safe target.",
        "tip": "This hole looks like a breather, but par is a great score. Trust your number and swing smooth."
    },
    {
        "hole": 4,
        "par": 4,
        "yardage": 426,
        "image": "hole4.jpg",
        "description": "A true test of ball striking. Two precise shots required — and uphill all the way.",
        "tee_shot": "
- Aim left-center. The fairway slopes right and can kick balls into trouble.
- 271 yards from blue tees lands near the start of the uphill slope.",
        "approach": "
- Mid-iron uphill to a shallow 21-yard green.
- Take an extra club — short leaves a tough chip.
- Long is no good — chip back is slick.",
        "tip": "Respect the slope. Play your approach to the middle and keep it below the hole."
    },
    {
        "hole": 5,
        "par": 4,
        "yardage": 389,
        "image": "hole5.jpg",
        "description": "A classic risk-reward dogleg left that punishes greed and rewards precision.",
        "tee_shot": "
- Play to left-center. Don’t cut the corner unless confident.
- 218–232 yard drive puts you in perfect wedge range.",
        "approach": "
- 85–125 yard approach into a green 39 yards wide.
- Green is guarded right by a bunker.
- Favor center-left.",
        "tip": "Two smart shots get you a birdie chance. Don’t force it off the tee."
    },
    {
        "hole": 6,
        "par": 4,
        "yardage": 377,
        "image": "hole6.jpg",
        "description": "A picturesque dogleg left with water, trees, and one of the tightest approach angles on the course.",
        "tee_shot": "
- Slight draw around the corner sets you up well.
- 251–266 yards puts you at the corner.
- Right side leaves blocked approach.",
        "approach": "
- Short pitch of 85–125 yards over Trout Creek.
- Green is 33 yards deep with guarded edges.
- Avoid chasing back pins.",
        "tip": "Rewarding hole if positioned properly. Play to the corner, pitch it up, and avoid the sucker pins."
    },
    {
        "hole": 7,
        "par": 5,
        "yardage": 507,
        "image": "hole7.jpg",
        "description": "A reachable par 5 with a risk-reward second shot. Birdie is in play — but only if you earn it.",
        "tee_shot": "
- Target left-center of the fairway.
- 281–305 yard drive gives you a green light to go.
- Fairway is generous but bordered by trees."
        ,
        "approach": "
- Go for it? You’ll need 215–230 yards uphill.
- Lay up to 130–150 yard range for full wedge.
- Green is narrow and guarded.",
        "tip": "Don’t force the hero shot. Lay up smartly if lie or angle is poor — wedge it close."
    },
    {
        "hole": 8,
        "par": 3,
        "yardage": 158,
        "image": "hole8.jpg",
        "description": "The shortest hole on the course, but don’t sleep on it — distance control is everything.",
        "tee_shot": "
- Plays true but wind swirls.
- Pick a target that splits the green.
- Bunker front-right in play.",
        "approach": "
- 36-yard deep green — pin placement affects club choice.
- Short is safer than long.",
        "tip": "Don’t chase. Center of the green is a win. Use the call box to order food!"
    },
    {
        "hole": 9,
        "par": 4,
        "yardage": 406,
        "image": "hole9.jpg",
        "description": "Finishing the front nine with a classic Tahoe-style dogleg right.",
        "tee_shot": "
- Right-center is ideal.
- 286–300 yard drive sets up a downhill second.
- Avoid bailing right. More room left than it seems.",
        "approach": "
- 110–130 yards to a two-tier green 36 yards deep.
- Distance control is crucial.
- Wrong tier = difficult two-putt.",
        "tip": "Dial back off the tee for position. Wedge it close and finish the front strong."
    },
    # Holes 10-18 will be added similarly

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
    st.warning(f"Image not found: {hole['image']}. Make sure it's in the 'hole_images' folder.")

# Display info
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
