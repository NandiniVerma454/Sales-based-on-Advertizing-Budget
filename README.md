Predicting Sales via Advertising Budget

🚀 Project Description

It is a data science web app that allows users to predict product sales based on advertising budgets allocated across different media channels (TV, Radio, Newspaper).

🚀 Key features:

•	Trained a regression model (Decision Tree Regressor) on an advertising dataset.
•	Built an interactive web app using Streamlit to input budgets and predict sales.
•	Deployed the app on Streamlit Cloud, making it accessible via a web browser.

🚀 Tech stack:

•	Python (Pandas, NumPy, Scikit-learn, Joblib)
•	Streamlit for web app UI
•	GitHub + Streamlit Cloud for deployment

🚀 Machine Learning Model

- Model type: Decision Tree Regressor
- Training: The model was trained on a standard Advertising dataset (features: TV, Radio, Newspaper; target: Sales).
- Persistence: The model is saved as `sales_model.pkl` using `joblib` for easy loading in the app.
  
🚀 Overview

  In this app, you can:
- Input TV, Radio, and Newspaper advertising budgets.
- Get instant predictions of sales based on these budgets.
- Visualize and interact with a clean, user-friendly interface.
  
🚀 LINK:

👉 Dataset :
🔗https://www.kaggle.com/datasets/yasserh/advertising-sales-dataset?utm_source=chatgpt.com

👉 The app is deployed on Streamlit Cloud  
 🔗 https://sales-based-on-advertizing-budget-hk2xj2dzvkiwzvfkbjpeq2.streamlit.app/

🚀 How it was deployed:

1.	Pushed code + `sales_model.pkl` + `requirements.txt` to GitHub  
2.	Connected GitHub repo to Streamlit Cloud  
3.	Streamlit Cloud builds the app using `requirements.txt` and serves it
