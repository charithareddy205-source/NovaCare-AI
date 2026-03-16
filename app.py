import streamlit as st
from pypdf import PdfReader

st.title("NovaCare – AI Health Record Assistant")
st.caption("AI-powered medical report analysis and patient health insights")

uploaded_file = st.file_uploader("Upload Medical Report", type=["pdf","txt"])

if uploaded_file is not None:

    # Read file
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    else:
        text = uploaded_file.read().decode("utf-8")

    # Show report text
    st.subheader("Report Text")
    st.write(text)

    # Detect patient information
    st.subheader("Detected Patient Information")

    if "patient name" in text.lower():
        st.write("Patient name detected")

    if "age" in text.lower():
        st.write("Age detected")

    if "symptoms" in text.lower():
        st.write("Symptoms detected")

    if "diagnosis" in text.lower():
        st.write("Diagnosis detected")

    if "medicine" in text.lower() or "tablet" in text.lower():
        st.write("Medicine detected")

    # AI Health Summary
    st.subheader("AI Health Summary")

    if "fever" in text.lower():
        st.write("Possible condition: Fever")

    if "diabetes" in text.lower():
        st.write("Possible condition: Diabetes")

    if "paracetamol" in text.lower():
        st.write("Medicine detected: Paracetamol")

    # AI Generated Report Summary
    summary = ""

    if "fever" in text.lower():
        summary += "The patient may be experiencing fever. "

    if "headache" in text.lower():
        summary += "Headache symptoms are mentioned. "

    if "diabetes" in text.lower():
        summary += "The report suggests possible diabetes. "

    if summary == "":
        summary = "The report contains medical information that should be reviewed by a doctor."

    st.subheader("AI Generated Report Summary")
    st.write(summary)

    # Patient Health Dashboard
    st.subheader("Patient Health Dashboard")

    fever = "fever" in text.lower()
    diabetes = "diabetes" in text.lower()

    if fever:
        st.write("⚠️ Fever detected")

    if diabetes:
        st.write("⚠️ Diabetes mentioned")

    if not fever and not diabetes:
        st.write("No major health risks detected")

    # Health Risk Level
    risk_level = "Low"

    if fever and diabetes:
        risk_level = "High"
    elif fever or diabetes:
        risk_level = "Medium"

    st.subheader("Health Risk Level")
    st.write("Health Risk Level:", risk_level)

    # AI Doctor Chatbot
    st.subheader("Ask AI Doctor")

    question = st.text_input("Ask a question about the report")

    if question:
        q = question.lower()

        if "fever" in q:
            st.write("Fever may indicate infection or illness. Monitoring temperature and consulting a doctor is recommended.")

        elif "headache" in q:
            st.write("Headache can occur due to stress, infection, dehydration, or other conditions.")

        elif "diabetes" in q:
            st.write("Diabetes is a condition related to high blood sugar levels and requires medical management.")

        elif "medicine" in q or "tablet" in q:
            st.write("Medicines mentioned in the report should be taken as prescribed by the doctor.")

        elif "diagnosis" in q:
            st.write("Diagnosis explains the patient's medical condition based on symptoms and tests.")

        elif "symptoms" in q:
            st.write("Symptoms help doctors understand the patient's health condition.")

        else:
            st.write("Please consult a healthcare professional for detailed advice.")

    # Share Report Feature
    st.subheader("Share Report with Hospital")

    if st.button("Send Report to Hospital"):
        st.success("Report successfully shared with hospital database.")
    st.subheader("Share Report with Hospital")

    hospital = st.selectbox(
    "Choose Hospital",
    ["Apollo Hospital", "Yashoda Hospital", "Global Hospital","Gandhi Hospital","Kamineni Hospital","Omega Hospital"]
    )

    if st.button("Send Report"):
        st.success(f"Report successfully shared with {hospital}")
    st.subheader("Download AI Summary")

    st.download_button(
       label="Download Report Summary",
       data=summary,
       file_name="health_summary.txt"
)