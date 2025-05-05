import streamlit as st

st.title("My‑Free‑Zoo Breeding Calculator")

# --- User Inputs ---
success_rate = st.slider(
    "Breeding Success Rate (%)", min_value=0, max_value=100, value=50, step=1
) / 100.0

pairs = st.number_input(
    "Number of Breeding Pairs", min_value=1, value=10, step=1
)

twins_pct = st.slider(
    "Twins Chance (%)", min_value=0, max_value=100, value=15, step=1
) / 100.0

triplets_pct = st.slider(
    "Triplets Chance (%)", min_value=0, max_value=100, value=5, step=1
) / 100.0

breed_per_day = st.number_input(
    "Breeding Attempts per Day", min_value=1, value=1, step=1
)

days = st.number_input(
    "Number of Days", min_value=1, value=7, step=1
)

# Validate probabilities
if twins_pct + triplets_pct > 1:
    st.error("Error: Twins% + Triplets% must not exceed 100%.")
else:
    # Calculate expected births per successful breeding
twins_prob = twins_pct
ntrips_prob = triplets_pct
single_prob = 1 - twins_prob - ntrips_prob

avg_births_per_success = (
    single_prob * 1
    + twins_prob * 2
    + ntrips_prob * 3
)

# Expected babies per attempt
daily_per_pair = success_rate * avg_births_per_success

# Total expected newborns
daily_expected_babies = pairs * breed_per_day * daily_per_pair
total_expected_babies = daily_expected_babies * days

# Initial count and final total
initial_animals = pairs * 2
final_expected_animals = initial_animals + total_expected_babies

# Display results
st.subheader("Results")
st.write(f"Initial Animals: **{initial_animals}**")
st.write(f"Expected Newborns: **{total_expected_babies:.1f}**")
st.write(f"Expected Total Animals after {days} days: **{final_expected_animals:.1f}**")

# Optional: show breakdown
with st.expander("Show Calculation Breakdown"):
    st.write(f"Success Rate: {success_rate * 100:.1f}%")
    st.write(f"Avg Births per Success: {avg_births_per_success:.2f}")
    st.write(f"Daily Expected Babies per Pair: {daily_per_pair:.2f}")
    st.write(f"Daily Expected Total Babies: {daily_expected_babies:.2f}")
    st.write(f"Days: {days}")
