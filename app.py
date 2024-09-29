import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
import numpy as np
import openai
import seaborn as sns
from matplotlib import pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Medical AI Bias Dashboard",
    page_icon="🩺",
    layout="wide"
)

# Sidebar with logo and project description
st.sidebar.image('assets/logo.png', caption='', use_column_width=True)
st.sidebar.markdown("""
## EquiHealth AI Bias Insight
This dashboard explores and detects bias in AI models used in healthcare, 
and provides educational resources on how to mitigate these biases. 
Analyze datasets, learn about bias in AI, and explore the impact of underrepresentation.
""")

# Embed the CSS for consistent styling
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url('assets/background.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

# Embed other styling
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
* {{
    margin: 0;
    padding: 0;
}}
html, body {{
    overflow-x: hidden;
}}
body {{
    font-family: 'Poppins', sans-serif !important;
}}
p {{
    color: rgb(251, 246, 240) !important;
}}
.btn {{
    font-weight: 600;
    padding: 1rem;
    width: 10rem;
    border-radius: 1.5rem;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    color: rgb(255, 255, 255) !important;
    background: rgba(80, 80, 80, 0.2) !important;
    border: rgb(255, 255, 255) 0.15rem solid !important;
    text-decoration: none;
    transition: all 0.3s ease;
}}
.btn:hover {{
    cursor: pointer;
    background-color: rgb(113, 169, 231) !important;
    transform: scale(1.05);
    box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.5);
}}
.hero {{
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 2rem;
}}
.stats {{
    display: flex;
    justify-content: space-around;
    margin-top: 50px;
}}
.stat {{
    text-align: center;
    width: 30%;
}}
.stat h1 {{
    font-size: 56px;
    color: rgb(251, 246, 240) !important;
    margin-bottom: 10px;
}}
.stat p {{
    font-size: 18px;
    color: rgb(251, 246, 240) !important;
}}
.title {{
    font-size: 3rem;
    text-align: center;
    color: rgb(251, 246, 240) !important;
    margin-top: 2rem;
}}
.subtitle {{
    font-size: 1.75rem;
    text-align: center;
    color: rgb(251, 246, 240) !important;
    margin-bottom: 1rem;
}}
footer {{
    text-align: center;
    margin-top: 80px;
    color: rgb(251, 246, 240) !important;
}}
</style>
""", unsafe_allow_html=True)

# Define tabs with emojis as icons
tabs = st.tabs(["🏠 Home", "🔍 Discover", "📖 Learn", "📊 Analyze", "📝 Quiz"])

# Home tab
with tabs[0]:
    st.markdown("""
        <section id="home">
            <div class="section-container">
                <div class="section__text">
                    <h1 class="title">Medical AI Bias: Striving for Fairness in Healthcare</h1>
                    <p class="subtitle">Explore, understand, and mitigate bias in AI models influencing healthcare outcomes.</p>
                </div>
            </div>
        </section>
        """, unsafe_allow_html=True)


    # Key Statistics Section
    st.markdown("""
        <div class="stats">
            <div class="stat">
                <h1>80%</h1>
                <p>AI models trained with unbalanced datasets</p>
            </div>
            <div class="stat">
                <h1>20%</h1>
                <p>Higher misdiagnosis rates for minorities</p>
            </div>
            <div class="stat">
                <h1>90%</h1>
                <p>Developers unaware of bias in their models</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Generate continuous data for ages 18 to 80 for both male and female participation
    ages = np.linspace(18, 80, 100)  # 100 points between ages 18 to 80
    races = np.arange(5)  # Represent races as 0 to 4 (White, Black, Hispanic, Asian, Other)
    race_labels = ["White", "Black", "Hispanic", "Asian", "Other"]

    # Meshgrid for surface plot
    X, Y = np.meshgrid(ages, races)

    # Simulate male and female participation data (higher for males, lower for females)
    Z_male = np.random.normal(60, 10, (5, 100)) + 20 * (races[:, None] == 0)  # White males higher participation
    Z_female = np.random.normal(40, 10, (5, 100)) + 10 * (races[:, None] == 0)  # White females slightly higher

    col1, col2 = st.columns(2)

    # Create the 3D Surface Plot for Male Participation
    with col1:
        st.markdown("### Male Participation in Medical Research by Race and Age")
        fig_male_surface = go.Figure(data=[go.Surface(z=Z_male, x=X, y=Y, colorscale='Viridis')])

        fig_male_surface.update_layout(
            title="Male Participation (%)",
            scene=dict(
                xaxis_title='Age',
                yaxis=dict(
                    title='Race',
                    tickvals=[0, 1, 2, 3, 4],
                    ticktext=race_labels
                ),
                zaxis_title='Participation (%)'
            )
        )
        st.plotly_chart(fig_male_surface)

    # Create the 3D Surface Plot for Female Participation
    with col2:
        st.markdown("### Female Participation in Medical Research by Race and Age")
        fig_female_surface = go.Figure(data=[go.Surface(z=Z_female, x=X, y=Y, colorscale='Viridis')])

        fig_female_surface.update_layout(
            title="Female Participation (%)",
            scene=dict(
                xaxis_title='Age',
                yaxis=dict(
                    title='Race',
                    tickvals=[0, 1, 2, 3, 4],
                    ticktext=race_labels
                ),
                zaxis_title='Participation (%)'
            )
        )
        st.plotly_chart(fig_female_surface)

    # Sources and Explanation
    st.markdown("""
        ### Sources:
        - **National Institutes of Health (NIH)**: Underrepresentation of minorities and women in medical research and clinical trials [[1]](https://www.nih.gov/news-events/news-releases/nih-issues-new-research-on-inclusion-reporting-clinical-trials).
        - **Sex Bias in Medical Research**: National Center for Biotechnology Information (NCBI) [[2]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7611255/).

        These graphs visualize a hypothetical distribution of participation by race and age, based on trends reported in real-world studies.
        - **White Males** are often overrepresented in clinical trials and medical research.
        - **Black, Hispanic, and Other Minority Females** are often underrepresented, which leads to biases in medical AI systems.
        """)

    # Updated backed-up stats
    st.markdown("""
        ### Backed-Up Statistics:
        - **80%**: AI models trained with unbalanced datasets, leading to systemic biases [[3]](https://journals.sagepub.com/doi/10.1177/0272989X20926364).
        - **20%**: Higher misdiagnosis rates for minorities compared to white patients [[4]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6112349/).
        - **90%**: Developers unaware of bias in their models due to a lack of diverse data [[5]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7320053/).
        """)

# Explore Bias tab
with tabs[1]:
    st.markdown("### Explore the Effect of Bias by Changing Input Factors")

    col1, col2 = st.columns(2)

    # Collect user input
    with col1:
        age = st.slider('Patient Age', 18, 100, 50)
        income = st.slider('Patient Income', 20000, 200000, 60000)
        race = st.selectbox('Patient Race', ['White', 'Black', 'Hispanic', 'Asian', 'Other'])
        gender = st.selectbox('Patient Gender', ['Male', 'Female', 'Other'])

        st.write(f"Selected Age: {age}, Income: ${income}, Race: {race}, Gender: {gender}")

    # Define weightings for bias severity based on factors
    race_weights = {'White': 0.1, 'Black': 0.3, 'Hispanic': 0.25, 'Asian': 0.2, 'Other': 0.15}
    gender_weights = {'Male': 0.1, 'Female': 0.25, 'Other': 0.3}

    # Calculate bias score using weighted factors
    race_bias = race_weights[race]
    gender_bias = gender_weights[gender]

    # Use income and age to adjust the bias score
    income_bias = 0.25 if income < 50000 else 0.1  # Lower income tends to increase bias
    age_bias = 0.2 if age > 60 else 0.1  # Older patients tend to experience more bias

    # Final bias score calculation (just a simple weighted sum)
    bias_score = (race_bias + gender_bias + income_bias + age_bias) * 100

    # Display bias severity gauge
    with col2:
        st.markdown("### Bias Severity Gauge")
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=bias_score,
            title={'text': "Bias Severity"},
            gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "red"}}
        ))
        st.plotly_chart(fig)

    # Explanation of the bias score calculation
    st.markdown("""
    ### How is the bias severity calculated?
    The bias severity score is calculated based on several factors:
    - **Race**: Research has shown that racial minorities, especially Black and Hispanic patients, are more likely to experience bias in medical AI models [[1]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7903396/).
    - **Gender**: Female and non-binary patients are often underrepresented in medical data, which can lead to higher rates of bias [[2]](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0184541).
    - **Income**: Lower-income patients tend to have less access to healthcare, which introduces bias when models are trained on more affluent populations [[3]](https://www.healthaffairs.org/doi/full/10.1377/hlthaff.2018.05155).
    - **Age**: Older patients tend to experience more bias, particularly when AI systems are trained on younger populations [[4]](https://jamanetwork.com/journals/jama/fullarticle/2765676).

    The final bias score is a weighted combination of these factors.
    """)

# Learn tab
with tabs[2]:
    st.title("Learn About Bias in AI")

    # Introduction to Bias in AI
    st.markdown("""
        ## What is Bias in AI?
        Bias in AI refers to the systematic favoritism or prejudice shown in AI models due to skewed training data, algorithms, or both.
        It can result in unequal treatment of certain groups, leading to real-world consequences in areas like healthcare, finance, and law enforcement.
        """)

    # Types of Bias in AI
    st.markdown("""
        ## Types of Bias in AI
        1. **Selection Bias**: Occurs when the sample data isn't representative of the population it serves.
        2. **Confirmation Bias**: Favoring information that confirms existing beliefs or stereotypes.
        3. **Algorithmic Bias**: Arises when algorithms make decisions that systematically disadvantage certain groups.
        4. **Reporting Bias**: Involves reporting only certain types of outcomes, which skews data and algorithms.
        """)
 # Hero Section with Call-to-Action Buttons
    st.markdown("""
        <div class="hero">
            <a href="#" class="btn">Explore Bias</a>
            <a href="#" class="btn">Learn More</a>
            <a href="#" class="btn">Analyze Your Data</a>
        </div>
        """, unsafe_allow_html=True)

# Analyze Data tab (Tab 3)
with tabs[3]:
    st.title("Analyze Your Data for Bias")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload Medical Study CSV", type="csv")


    # Function to call ChatGPT and get bias analysis
    def detect_bias(data):
        # Convert the DataFrame to CSV format (as a string) for easier transmission to ChatGPT
        csv_data = data.to_csv(index=False)

        # Send the dataset to ChatGPT for analysis
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in medical studies. Analyze this study's dataset and summarize it."
                },
                {
                    "role": "user",
                    "content": f"""
                        Here is the dataset in CSV format:
                        ```
                        {csv_data}
                        ```                    
                        Summarize the results, focusing on bias detection and analysis.
                    """
                }
            ]
        )

        # Parse ChatGPT response
        chat_response = response['choices'][0]['message']['content']
        return chat_response


    # Function to analyze bias in the dataset
    def analyze_bias(data):
        flags = []

        # Check for demographics columns
        demographics = {
            "Race": "Race" in data.columns,
            "Age": "Age" in data.columns,
            "Gender": "Gender" in data.columns
        }

        # Bias detection logic
        if not demographics["Race"]:
            flags.append("No race demographic information is available.")
        if not demographics["Age"]:
            flags.append("No age demographic information is available.")
        if not demographics["Gender"]:
            flags.append("No gender demographic information is available.")

        # Check for over/underrepresentation in race
        if demographics["Race"]:
            race_counts = data["Race"].value_counts(normalize=True) * 100
            for race, percentage in race_counts.items():
                if percentage > 60:
                    flags.append(f"{race} participants are overrepresented ({percentage:.2f}%).")
                elif percentage < 10:
                    flags.append(f"{race} participants are underrepresented ({percentage:.2f}%).")

        # Check for over/underrepresentation in age
        if demographics["Age"]:
            age_counts = data["Age"].value_counts(normalize=True) * 100
            for age, percentage in age_counts.items():
                if percentage > 60:
                    flags.append(f"Age group {age} participants are overrepresented ({percentage:.2f}%).")
                elif percentage < 10:
                    flags.append(f"Age group {age} participants are underrepresented ({percentage:.2f}%).")

        # Check for over/underrepresentation in gender
        if demographics["Gender"]:
            gender_counts = data["Gender"].value_counts(normalize=True) * 100
            for gender, percentage in gender_counts.items():
                if percentage > 60:
                    flags.append(f"{gender} participants are overrepresented ({percentage:.2f}%).")
                elif percentage < 10:
                    flags.append(f"{gender} participants are underrepresented ({percentage:.2f}%).")

        return flags


    # Process CSV file and detect bias
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded data preview:")
        st.write(data.head())

        # Call the bias detection function
        with st.spinner("Analyzing data for possible bias..."):
            bias_report = detect_bias(data)

        st.subheader("Bias Report")

        # Step 1: Bias report
        bias_flags = analyze_bias(data)
        if len(bias_flags) == 0:
            st.button("No Bias detected.")
        else:
            st.button("Possible bias detected.")

        st.subheader("Flags")
        for idx, flag in enumerate(bias_flags, start=1):
            st.write(f"{idx}. {flag}")

        # Step 2: Demographics information
        st.subheader("Demographics Information")
        st.write(f"Race demographics: {'Present' if 'Race' in data.columns else 'Not Detected'}")
        st.write(f"Age demographics: {'Present' if 'Age' in data.columns else 'Not Detected'}")
        st.write(f"Gender demographics: {'Present' if 'Gender' in data.columns else 'Not Detected'}")

        # Step 3: GPT API for bias flag
        st.subheader("Dataset Summary")
        st.write(bias_report)

        # 2x2 Dashboard setup using Matplotlib for Streamlit

        st.subheader("Bias Report Results")

        # Set up the figure for Streamlit
        fig, axs = plt.subplots(2, 2, figsize=(15, 12))

        # Gender Distribution (Pie chart)
        gender_distribution_data = data['Gender'].value_counts()
        axs[0, 0].pie(gender_distribution_data, labels=gender_distribution_data.index, autopct='%1.1f%%',
                      colors=['#66b3ff', '#99ff99'])
        axs[0, 0].set_title('Gender Distribution')

        # Age Group Distribution (Bar chart)
        age_distribution_data = data['Age'].value_counts()
        sns.barplot(x=age_distribution_data.index, y=age_distribution_data.values, ax=axs[0, 1], palette='Set2')
        axs[0, 1].set_title('Age Group Distribution')
        axs[0, 1].set_xlabel('Age Group')
        axs[0, 1].set_ylabel('Count')

        # Response Rate by Gender (Stacked bar chart)
        response_by_gender = data.groupby(['Gender', 'Response']).size().reset_index(name='Count')
        sns.barplot(x='Gender', y='Count', hue='Response', data=response_by_gender, ax=axs[1, 0], palette='coolwarm')
        axs[1, 0].set_title('Response Rate by Gender')
        axs[1, 0].set_ylabel('Count')

        # Time on Medication by Age Group (Box plot)
        sns.boxplot(x='Age', y='Time taking medication', data=data, hue='Gender', ax=axs[1, 1], palette='pastel')
        axs[1, 1].set_title('Time on Medication by Age Group')
        axs[1, 1].set_ylabel('Years on Medication')

        # Adjust layout
        plt.tight_layout()

        # Render the dashboard in Streamlit
        st.pyplot(fig)

# Quiz tab (replaces recommendations)
with tabs[4]:
    st.title("Bias in AI Quiz")

    # Quiz Questions
    st.markdown("### Question 1: What is Selection Bias?")
    q1 = st.radio("Select the correct answer:",
                  ["Bias due to unrepresentative sample data",
                   "Bias due to favoring existing beliefs",
                   "Bias due to how the algorithm was built"])

    st.markdown("### Question 2: Which strategy is best for preventing Algorithmic Bias?")
    q2 = st.radio("Select the correct answer:",
                  ["Use fairness metrics",
                   "Avoid using AI altogether",
                   "Increase the sample size"])

    st.markdown("### Question 3: Which type of bias involves only reporting certain outcomes?")
    q3 = st.radio("Select the correct answer:",
                  ["Selection Bias",
                   "Reporting Bias",
                   "Confirmation Bias"])

    # Submit and Show Score
    if st.button("Submit Answers"):
        score = 0
        if q1 == "Bias due to unrepresentative sample data":
            score += 1
        if q2 == "Use fairness metrics":
            score += 1
        if q3 == "Reporting Bias":
            score += 1

        st.write(f"Your score: {score}/3")

        if score == 3:
            st.success("Congratulations! You have a strong understanding of bias in AI.")
        elif score == 2:
            st.warning("Good job! But there’s room for improvement.")
        else:
            st.error("You might want to review the material again.")
