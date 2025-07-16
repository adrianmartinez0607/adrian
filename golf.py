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
    {
        "hole": 4,
        "image": "hole4.jpg",
        "par": 4,
        "yardage": 437,
        "description": "A scenic but demanding hole requiring a solid tee shot and precise approach to a shallow green.",
        "tee_shot": "- Favor the left center of the fairway for a flatter stance.\n- A fade off the tee works well with the shape of the hole.\n- Avoid the trees lining both sides.",
        "approach": "- The green is narrow and elevated, demanding accuracy.\n- Play for the center regardless of pin location.\n- Missing short leaves a manageable chip.",
        "tip": "Play it like a two-part puzzle—hit the fairway, then focus on distance control."
    },
    {
        "hole": 5,
        "image": "hole5.jpg",
        "par": 3,
        "yardage": 183,
        "description": "A beautiful par 3 framed by towering trees and bunkers surrounding the green.",
        "tee_shot": "- Club selection is crucial—green is deep but tight.\n- Avoid right-side bunkers.\n- Favor a draw to hold the green.",
        "approach": "- If you miss left, a soft chip uphill gives a chance to save par.\n- Bunker shots from the right are delicate due to green slope.\n- Watch for back pin locations.",
        "tip": "Trust your number and don’t overswing—precision trumps power here."
    },
    {
        "hole": 6,
        "image": "hole6.jpg",
        "par": 5,
        "yardage": 550,
        "description": "A true three-shot par 5 with elevation changes and a heavily protected green.",
        "tee_shot": "- Favor the right center for best angle to lay up.\n- Avoid the fairway bunkers on the left.\n- Downhill tee shot plays shorter than the yardage.",
        "approach": "- Lay up to your favorite yardage before the creek.\n- Avoid going long on the third shot—green slopes back to front.\n- Pick the correct tier.",
        "tip": "Three good shots earn a great birdie look—don't force an aggressive second."
    },
    {
        "hole": 7,
        "image": "hole7.jpg",
        "par": 4,
        "yardage": 395,
        "description": "An intimidating par 4 with water left and trees right—shot placement is everything.",
        "tee_shot": "- Aim just right of the center bunker.\n- Take less than driver if you're accurate with a 3-wood.\n- Water hazard sneaks in more than it appears.",
        "approach": "- Slightly uphill—take an extra club.\n- Avoid short left; it's a tough up-and-down.\n- Green is deeper than it looks.",
        "tip": "Take a deep breath on the tee—mental focus pays dividends here."
    },
    {
        "hole": 8,
        "image": "hole8.jpg",
        "par": 5,
        "yardage": 580,
        "description": "A risk-reward par 5 with an intimidating tee shot and a green tucked behind a creek.",
        "tee_shot": "- Favor the right side to open up the layup zone.\n- Avoid the fairway bunker on the left.\n- Big hitters may reach in two but must carry water.",
        "approach": "- Lay up to about 100–120 yards to stay short of the hazard.\n- Precision wedge needed to a sloped green.\n- Green is narrow with runoff left.\n",
        "tip": "Stay disciplined—take the layup unless you have a perfect number."
    },
    {
        "hole": 9,
        "image": "hole9.jpg",
        "par": 4,
        "yardage": 422,
        "description": "A strong finishing hole on the front with a creek down the left and OB right.",
        "tee_shot": "- Aim at the right edge of the left bunker.\n- Driver brings risk, but may be necessary.\n- Wind often swirls near the clubhouse.",
        "approach": "- Uphill into a two-tiered green.\n- Short is better than long.\n- Green is firm and plays fast.",
        "tip": "Play for par and walk away happy—bogey is easy if you're offline."
    },
    {
        "hole": 10,
        "image": "hole10.jpg",
        "par": 4,
        "yardage": 404,
        "description": "A sharp dogleg right that rewards a well-shaped tee ball.",
        "tee_shot": "- A fade off the tee is ideal.\n- Keep it under 260 yards to avoid running through the fairway.\n- Trees block the right if you're too aggressive.",
        "approach": "- Elevated green slopes left to right.\n- Middle of the green is safe on all pin locations.\n- Stay below the hole.",
        "tip": "Trust a 3-wood or hybrid off the tee—position matters more than distance."
    },
    {
        "hole": 11,
        "image": "hole11.jpg",
        "par": 4,
        "yardage": 428,
        "description": "A long par 4 with a slight uphill finish and a challenging green.",
        "tee_shot": "- Favor the left center for a flatter lie.\n- Avoid the trees right.\n- Fairway bunker is in play for longer hitters.",
        "approach": "- Play one extra club uphill.\n- Landing short and bouncing on works well.\n- Green slopes severely front to back.",
        "tip": "Bogey is okay here—be realistic and manage expectations."
    },
    {
        "hole": 12,
        "image": "hole12.jpg",
        "par": 5,
        "yardage": 561,
        "description": "A reachable par 5 if you can navigate the trees and creek.",
        "tee_shot": "- Favor the left to open up the angle.\n- Avoid right-side rough and hazard.\n- A draw works best off the tee.",
        "approach": "- Second shot must clear a creek if going for it.\n- Safer play is a lay-up to 100–120 yards.\n- Green is guarded by deep bunkers.",
        "tip": "Don’t chase eagle—play for birdie with a smart second shot."
    },
    {
        "hole": 13,
        "image": "hole13.jpg",
        "par": 3,
        "yardage": 173,
        "description": "A scenic par 3 with water short and bunkers long.",
        "tee_shot": "- Carry the water but don’t go long.\n- Aim for the center of the green.\n- Crosswind is common and deceptive.",
        "approach": "- Long miss brings double into play.\n- Better to be on the fringe short.\n- Stay calm and swing smooth.",
        "tip": "Middle of the green is always the right answer."
    },
    {
        "hole": 14,
        "image": "hole14.jpg",
        "par": 4,
        "yardage": 415,
        "description": "A tight driving hole with a tough green to hold.",
        "tee_shot": "- Use a fairway wood or hybrid.\n- Stay left of the tree line.\n- Fairway slopes toward trouble right.",
        "approach": "- Elevated green with false front.\n- Must carry to the middle tier.\n- Ball will release toward the back.",
        "tip": "Trust your distance—don't flirt with the front edge."
    },
    {
        "hole": 15,
        "image": "hole15.jpg",
        "par": 5,
        "yardage": 585,
        "description": "A classic par 5 with elevation changes and tree trouble throughout.",
        "tee_shot": "- Hit a high draw to follow the shape of the fairway.\n- Stay short of the corner bunker.\n- Trees right kick balls into no-man’s land.",
        "approach": "- Lay up to the flat area near 100 yards.\n- Third shot plays uphill.\n- Green is narrow and fast.",
        "tip": "Three smart shots beat two heroic ones—play it in parts."
    },
    {
        "hole": 16,
        "image": "hole16.jpg",
        "par": 3,
        "yardage": 189,
        "description": "A tough par 3 with a long carry and swirling winds.",
        "tee_shot": "- Club up to handle elevation.\n- Favor the right side.\n- Avoid short left at all costs.",
        "approach": "- Miss right gives the best angle to chip.\n- Sloped green rejects poor shots.\n- Stay focused—it's late in the round.",
        "tip": "Commit to your number and trust your swing."
    },
    {
        "hole": 17,
        "image": "hole17.jpg",
        "par": 4,
        "yardage": 401,
        "description": "A short but strategic par 4 that rewards creativity off the tee.",
        "tee_shot": "- Iron or hybrid to about 240 yards.\n- Avoid the bunkers left and long.\n- Shape your shot to fit the dogleg.",
        "approach": "- Short iron into a small green.\n- Stay below the hole.\n- Putts from above are treacherous.",
        "tip": "Keep your foot on the gas—this is a scoring hole."
    },
    {
        "hole": 18,
        "image": "hole18.jpg",
        "par": 4,
        "yardage": 432,
        "description": "A dramatic finishing hole with danger left and deep bunkers around the green.",
        "tee_shot": "- Favor the right side off the tee.\n- Avoid the left hazard at all costs.\n- Wind often swirls around the trees.",
        "approach": "- Mid-iron into a well-protected green.\n- Better to be long than short.\n- Take an extra breath—it’s your last swing.",
        "tip": "Finish strong—par is a great score here."
    }
]

# Hole selector dropdown
hole_numbers = [f"Hole {hole['hole']}" for hole in hole_data]
selected_hole = st.selectbox("Select Hole", hole_numbers)
hole = next(h for h in hole_data if f"Hole {h['hole']}" == selected_hole)

# Load image and resize to 40% of original
image_path = os.path.join(IMAGE_DIR, hole['image'])
if os.path.exists(image_path):
    image = Image.open(image_path)
    width, height = image.size
    resized_image = image.resize((int(width * 0.4), int(height * 0.4)))
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
