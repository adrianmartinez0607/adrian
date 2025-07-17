import streamlit as st

st.set_page_config(page_title="Grays Crossing Golf Guide", layout="centered")
st.title("\U000026F3 Grays Crossing Golf Course Guide")
st.markdown("### Gold Tees Yardage & Strategy")

# Hole selection
selected_hole = st.selectbox("Select Hole", [f"Hole {i}" for i in range(1, 19)])

def render_hole(image_file, hole_title, tips):
    st.image(image_file, use_container_width=True)
    st.markdown(f"### {hole_title}")
    st.markdown(tips)

if selected_hole == "Hole 1":
    render_hole("grays1.jpg", "Hole 1 – 405 Yards", """
    **Tee Shot:** Favor the left side of the fairway to avoid the trees on the right and give yourself a clear angle in.

    **Approach:** A mid to short iron will leave you a solid chance for birdie—watch the pin as the green slopes back to front.

    **Overall Tip:** Stay focused off the tee, this opening hole rewards precision over power.
    """)

elif selected_hole == "Hole 2":
    render_hole("grays2.jpg", "Hole 2 – 178 Yards", """
    **Tee Shot:** Choose your club carefully and aim for the center of the green. Avoid the bunker left.

    **Approach:** Better to be long than short here—short shots may roll back off the front.

    **Overall Tip:** Trust your number and commit. Birdie chance with a confident swing.
    """)

elif selected_hole == "Hole 3":
    render_hole("grays3.jpg", "Hole 3 – 515 Yards", """
    **Tee Shot:** A drive to the right side opens up the fairway for a layup or a go at the green in two.

    **Approach:** Consider laying up left for a better angle in—green is narrow and guarded.

    **Overall Tip:** Don't force the eagle look. Smart play will leave a good birdie chance.
    """)

elif selected_hole == "Hole 4":
    render_hole("grays4.jpg", "Hole 4 – 431 Yards", """
    **Tee Shot:** Position tee shot favoring the left to open up your view of the green.

    **Approach:** Requires a long iron or hybrid. Don’t miss right—trouble lurks there.

    **Overall Tip:** Par is a great score here. Play conservative unless you’re confident.
    """)

elif selected_hole == "Hole 5":
    render_hole("grays5.jpg", "Hole 5 – 195 Yards", """
    **Tee Shot:** A precise mid-iron is needed here. The left side of the green feeds nicely.

    **Approach:** Watch the wind—shots can easily drift short and right into the bunker.

    **Overall Tip:** Play for the center and walk away happy.
    """)

elif selected_hole == "Hole 6":
    render_hole("grays6.jpg", "Hole 6 – 368 Yards", """
    **Tee Shot:** Place tee shot short of bunkers for a wedge approach.

    **Approach:** The green is protected short-right, so take enough club.

    **Overall Tip:** Great birdie chance with solid placement.
    """)

elif selected_hole == "Hole 7":
    render_hole("grays7.jpg", "Hole 7 – 537 Yards", """
    **Tee Shot:** Favor the left side—this opens the hole.

    **Approach:** Lay up to your ideal wedge yardage unless you're going for it.

    **Overall Tip:** Long and winding—play smart and avoid the fairway traps.
    """)

elif selected_hole == "Hole 8":
    render_hole("grays8.jpg", "Hole 8 – 396 Yards", """
    **Tee Shot:** Accurate drive essential—narrow fairway.

    **Approach:** Short iron to slightly elevated green. Keep it below the hole.

    **Overall Tip:** Precision matters here—play to your strengths.
    """)

elif selected_hole == "Hole 9":
    render_hole("grays9.jpg", "Hole 9 – 448 Yards", """
    **Tee Shot:** Favor the left-center of the fairway to avoid tree trouble.

    **Approach:** A long second shot—consider playing for the fat part of the green.

    **Overall Tip:** A tough finisher to the front nine—take par and run.
    """)

elif selected_hole == "Hole 10":
    render_hole("grays10.jpg", "Hole 10 – 372 Yards", """
    **Tee Shot:** Aim between the right-side bunkers for a great angle.

    **Approach:** Wind helps, so trust your short club. Mind the tricky green contours.

    **Overall Tip:** One of the tougher greens—prioritize distance control.
    """)

elif selected_hole == "Hole 11":
    render_hole("grays11.jpg", "Hole 11 – 152 Yards", """
    **Tee Shot:** Favor right side—terrain funnels left. Avoid the deep bunker.

    **Approach:** Commit to your line. Green is narrow and deep.

    **Overall Tip:** Accuracy wins here.
    """)

elif selected_hole == "Hole 12":
    render_hole("grays12.jpg", "Hole 12 – 413 Yards", """
    **Tee Shot:** Generous fairway—favor left for best angle.

    **Approach:** Deep bunkers guard both sides—aim center.

    **Overall Tip:** A classic risk-reward par four—take what it gives.
    """)

elif selected_hole == "Hole 13":
    render_hole("grays13.jpg", "Hole 13 – 412 Yards", """
    **Tee Shot:** Water lurks. Accuracy over distance. Keep it straight.

    **Approach:** Well-protected green—play to the middle.

    **Overall Tip:** Stay dry, stay smart.
    """)

elif selected_hole == "Hole 14":
    render_hole("grays14.jpg", "Hole 14 – 334 Yards", """
    **Tee Shot:** Tempting to go for it, but fairway play sets up a great wedge.

    **Approach:** Tiny green—must be sharp. Right miss is better than left.

    **Overall Tip:** Think through your tee shot—birdie is there.
    """)

elif selected_hole == "Hole 15":
    render_hole("grays15.jpg", "Hole 15 – 525 Yards", """
    **Tee Shot:** Play to the right side to take advantage of the slope.

    **Approach:** Ball feeds right to left—aim accordingly.

    **Overall Tip:** Manage your way to birdie—avoid big misses.
    """)

elif selected_hole == "Hole 16":
    render_hole("grays16.jpg", "Hole 16 – 194 Yards", """
    **Tee Shot:** Plays shorter due to elevation—1 to 3 clubs less.

    **Approach:** Hit it high and soft. Green won’t hold low shots.

    **Overall Tip:** Trust your club and commit.
    """)

elif selected_hole == "Hole 17":
    render_hole("grays17.jpg", "Hole 17 – 354 Yards", """
    **Tee Shot:** Don’t blow it through the fairway with wind at your back. Aim over the left bunker.

    **Approach:** High shot needed—firm green hard to hold.

    **Overall Tip:** Focus on spin and trajectory.
    """)

elif selected_hole == "Hole 18":
    render_hole("grays18.jpg", "Hole 18 – 475 Yards", """
    **Tee Shot:** Favor right-center to avoid trees.

    **Second Shot:** Most will lay up left—big hitters can challenge the right.

    **Approach:** Don’t go long. This green is tricky.

    **Overall Tip:** Play smart and close strong.
    """)
