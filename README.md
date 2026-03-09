👩‍⚕️ MaRAI: Smart Pregnancy Planning Tool

MaRAI is an AI-driven health assessment tool designed to predict maternal health risk levels. By analyzing key physiological vitals, the system categorizes patients into Low, Mid, or High Risk categories to assist in early clinical decision-making.
 Live Demo

Access the deployed application here: maraihealth.streamlit.app
 Project Overview

This project bridges the gap between machine learning research and practical healthcare delivery.

    Accuracy: 99.6% on validation data.

    Model: Random Forest Classifier.

    Objective: Provide a rapid, data-driven screening tool for maternal health monitoring.

 Tech Stack

    Language: Python 3.x

    Machine Learning: Scikit-Learn, Pandas, NumPy

    Deployment: Streamlit Cloud

    Version Control: GitHub

 Methodology

    Data Engineering: Synthesized a medically-grounded dataset of 1,500 records based on clinical risk indicators (Age, BP, Blood Sugar, Temperature).

    Analysis: Conducted feature importance analysis, identifying Blood Sugar and Systolic BP as the primary predictors of maternal risk.

    Validation: Evaluated performance using a Confusion Matrix to ensure high sensitivity for "High Risk" cases.

    Serialization: Exported the trained model via Pickle for seamless integration into the web interface.
    
    Model Insights & Explainability

    To ensure clinical reliability, the model's decision-making process was audited using Feature Importance Analysis. The results align with medical research regarding gestational health:

    Primary Risk Driver: Blood Sugar (BS): The model correctly identified glucose levels as the strongest predictor of high-risk outcomes (consistent with screening for Gestational Diabetes).

    Secondary Driver: Systolic BP: High blood pressure readings were the second most significant factor in identifying potential pre-eclampsia risks.

    Safety Logic: The system is tuned to be highly sensitive to elevated vitals, ensuring that borderline cases are categorized with appropriate caution.

 Repository Structure

    app.py: The Streamlit web interface and inference logic.

    marai_model.pkl: The serialized Random Forest model.

    MaRAI_Notebook.ipynb: Full research, training, and evaluation history.

    requirements.txt: Environment dependencies.

🤝 Contact: baracatheriaclaire@gmail.com

Catheria-Claire Computer Engineering Student | Antalya Bilim Üniversitesi

Polyglot (5 Languages) | YTB Scholar | Miss Mathématique
