import streamlit as st
import json

# Sidebar: Course and Hole selection
st.sidebar.title("🏌️ Golf Course Guide")
selected_course = st.sidebar.selectbox("Select Course", list(courses.keys()))
hole_numbers = [f"Hole {h['number']}" for h in courses[selected_course]["holes"]]
selected_hole_label = st.sidebar.selectbox("Select Hole", hole_numbers)
selected_hole_index = hole_numbers.index(selected_hole_label)
hole = courses[selected_course]["holes"][selected_hole_index]

# Main Display
st.title(f"{selected_course} - Hole {hole['number']}")
st.image(hole["image"], use_column_width=True)
st.markdown(f"**Yardage:** {hole['yardage']} yards")
st.markdown(hole["overview"])
st.markdown(hole["tee_shot"])
st.markdown(hole["approach"])
st.markdown(hole["tip"])

# Yardage Summary (Optional)
with st.expander("📊 View Yardage Summary"):
    total_yardage = sum(h["yardage"] for h in courses[selected_course]["holes"])
    st.markdown(f"**Total Yardage:** {total_yardage} yards")
    st.markdown("### Hole-by-Hole Yardage")
    for h in courses[selected_course]["holes"]:
        st.markdown(f"- Hole {h['number']}: {h['yardage']} yards")

courses = {
    "Coyote Moon": {
        "holes": [
            {"number": 1, "image": "hole1.jpg", "yardage": 485,
            "overview": "📝 **Overview:** Scenic downhill opener with generous landing area.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Favor the left side to catch the slope.",
            "approach": "🔍 **Approach Game:** Avoid going long — green slopes back to front.",
            "tip": "💡 **Tee Tip:** Use a 3W or hybrid for safety."},
            {"number": 2, "image": "hole2.jpg", "yardage": 365,
            "overview": "📝 **Overview:** Dogleg left through trees.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Position drive near corner for best angle.",
            "approach": "🔍 **Approach Game:** Green is protected short-left — fly it all the way.",
            "tip": "💡 **Tee Tip:** Mid-iron off tee leaves full wedge."},
            {"number": 3, "image": "hole3.jpg", "yardage": 190,
            "overview": "📝 **Overview:** Uphill par 3 to a narrow green.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Take one more club due to elevation.",
            "approach": "🔍 **Approach Game:** Avoid right — steep runoff.",
            "tip": "💡 **Tee Tip:** Middle of green is never bad."},
            {"number": 4, "image": "hole4.jpg", "yardage": 410,
            "overview": "📝 **Overview:** Tough par 4 with a blind tee shot.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Aim at the tree line and trust the fairway opens up.",
            "approach": "🔍 **Approach Game:** Second shot plays slightly uphill.",
            "tip": "💡 **Tee Tip:** Use yardage markers carefully."},
            {"number": 5, "image": "hole5.jpg", "yardage": 330,
            "overview": "📝 **Overview:** Short par 4 with options.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Lay up with long iron or drive corner with draw.",
            "approach": "🔍 **Approach Game:** Small green with bunkers left.",
            "tip": "💡 **Tee Tip:** Don’t overthink the tee shot."},
            {"number": 6, "image": "hole6.jpg", "yardage": 380,
            "overview": "📝 **Overview:** Par 4 with water left.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Drive up right side for safest approach.",
            "approach": "🔍 **Approach Game:** Avoid pulling approach into hazard.",
            "tip": "💡 **Tee Tip:** Trust your fade."},
            {"number": 7, "image": "hole7.jpg", "yardage": 195,
            "overview": "📝 **Overview:** Another strong par 3.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Front bunker catches mishits.",
            "approach": "🔍 **Approach Game:** Middle of green is fine — green slopes back.",
            "tip": "💡 **Tee Tip:** Commit to your number."},
            {"number": 8, "image": "hole8.jpg", "yardage": 540,
            "overview": "📝 **Overview:** Scenic downhill par 5.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Grip it and rip it — wide landing zone.",
            "approach": "🔍 **Approach Game:** Second shot needs placement for third.",
            "tip": "💡 **Tee Tip:** Avoid going long on approach."},
            {"number": 9, "image": "hole9.jpg", "yardage": 425,
            "overview": "📝 **Overview:** Long uphill par 4.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Drive must carry ridge.",
            "approach": "🔍 **Approach Game:** Elevated green demands club selection.",
            "tip": "💡 **Tee Tip:** Driver essential — don’t lay back."},
            {"number": 10, "image": "hole10.jpg", "yardage": 365,
            "overview": "📝 **Overview:** Dogleg right with elevated tee.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Cut the corner with a fade.",
            "approach": "🔍 **Approach Game:** Short wedge in if tee shot is ideal.",
            "tip": "💡 **Tee Tip:** Play aggressive off tee."},
            {"number": 11, "image": "hole11.jpg", "yardage": 185,
            "overview": "📝 **Overview:** Short par 3 over a gorge.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Do not miss short — it’s jail.",
            "approach": "🔍 **Approach Game:** Take enough club — swirling wind here.",
            "tip": "💡 **Tee Tip:** Club up if unsure."},
            {"number": 12, "image": "hole12.jpg", "yardage": 400,
            "overview": "📝 **Overview:** Tree-lined dogleg left.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Driver leaves wedge if hit well.",
            "approach": "🔍 **Approach Game:** Green is shallow and firm.",
            "tip": "💡 **Tee Tip:** Middle-left is safe zone."},
            {"number": 13, "image": "hole13.jpg", "yardage": 425,
            "overview": "📝 **Overview:** Straightaway par 4 with slight rise.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Driver sets up a good mid-iron.",
            "approach": "🔍 **Approach Game:** Avoid right-side trees.",
            "tip": "💡 **Tee Tip:** Play for center of green."},
            {"number": 14, "image": "hole14.jpg", "yardage": 190,
            "overview": "📝 **Overview:** Flat par 3 with tricky green.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Accuracy is key — bunkers short left.",
            "approach": "🔍 **Approach Game:** Pin front right? Be bold.",
            "tip": "💡 **Tee Tip:** Don’t flirt with long left."},
            {"number": 15, "image": "hole15.jpg", "yardage": 525,
            "overview": "📝 **Overview:** Risk-reward par 5.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Left side opens up second shot.",
            "approach": "🔍 **Approach Game:** Green is reachable — bunkers short.",
            "tip": "💡 **Tee Tip:** Eagle possible with two perfect shots."},
            {"number": 16, "image": "hole16.jpg", "yardage": 355,
            "overview": "📝 **Overview:** Short par 4 you can drive.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Go for it or lay back — both work.",
            "approach": "🔍 **Approach Game:** Sloped green defends well.",
            "tip": "💡 **Tee Tip:** Wedge game matters here."},
            {"number": 17, "image": "hole17.jpg", "yardage": 175,
            "overview": "📝 **Overview:** Straightforward par 3.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Wind can swirl — trust your number.",
            "approach": "🔍 **Approach Game:** Back shelf is hard to hold.",
            "tip": "💡 **Tee Tip:** Middle of green all day."},
            {"number": 18, "image": "hole18.jpg", "yardage": 510,
            "overview": "📝 **Overview:** Great closing hole.",
            "tee_shot": "🎯 **Tee Shot Strategy:** Big tee shot makes it reachable.",
            "approach": "🔍 **Approach Game:** Second must carry hazard.",
            "tip": "💡 **Tee Tip:** Finish strong — birdie in play."}
        ]
    }
}
