# 🛒 Walmart Sales Dashboard with Vizro

This project presents a fully interactive and visually appealing dashboard that explores Walmart’s weekly sales data. Built using [Vizro](https://vizro.ai), the dashboard highlights sales patterns over time, across stores, and in relation to economic indicators like temperature, CPI, and unemployment.

---

## 📊 Project Overview

The dashboard helps answer key business questions such as:

* Which stores have the highest weekly sales?
* How do holidays impact Walmart sales?
* What is the relationship between sales and macroeconomic factors?

Using Vizro’s model-based architecture, multiple dashboards are created with a clean and intuitive UI.

---

## ⚙️ Tech Stack

* **Language**: Python 3
* **Libraries**:

  * `pandas`: Data manipulation
  * `vizro`: Declarative dashboards with Plotly and Flask
  * `plotly.express`: Quick, interactive charts

---

## 📁 Dataset

* **Source**: `Walmart_Sales.csv`
* **Fields**:

  * `Store`, `Date`, `Weekly_Sales`
  * `Holiday_Flag`, `Temperature`, `Fuel_Price`
  * `CPI`, `Unemployment`

---

## 📈 Dashboards Created

### 1. **Dashboard-1**

* 📍 *Total Weekly Sales by Store* (Bar chart)
* 📍 *Weekly Sales Over Time* (Line chart)

### 2. **Dashboard-2**

* 📍 *Holiday vs Non-Holiday Sales* (Bar chart)
* 📍 *Temperature vs Weekly Sales* (Scatter plot)

### 3. **Dashboard-3**

* 📍 *CPI vs Weekly Sales* (Scatter plot)
* 📍 *Unemployment vs Weekly Sales* (Line chart)

### 4. **Combined Dashboard**

* 🧩 All 6 charts in a grid layout for unified analysis

---

## 🚀 How to Run

1. **Install dependencies**:

   ```bash
   pip install vizro pandas plotly
   ```

2. **Ensure the dataset is in the same directory**:

   * `Walmart_Sales.csv`

3. **Run the script**:

   ```bash
   python walmart.py
   ```

4. **Your dashboard will open in a browser automatically.**

---

## 📷 Demo

![Capture04](https://github.com/user-attachments/assets/0cbcb053-3501-4e1c-9368-22e57e0add69)

![Capture05](https://github.com/user-attachments/assets/bc988704-df12-43fa-8ecb-64fbad6a7b76)

![Capture06](https://github.com/user-attachments/assets/3c7f6d07-9f8b-499e-bf04-c33a56f0322d)

![Capture03](https://github.com/user-attachments/assets/3b9a250f-478c-4faa-8252-da17b1d462d5)


---

## 🧠 Insights

* Top-performing stores can be identified for promotional strategies.
* Holidays generally see higher or lower average sales — this insight supports inventory planning.
* Negative correlation between unemployment and sales may indicate macroeconomic sensitivity.

---

## 📌 Why Vizro?

* Zero boilerplate for UI.
* Easy to configure complex layouts and navigation.
* Seamlessly integrates with `plotly.express`.

---

## 📬 Feedback & Contributions

Open to feedback, issues, and pull requests. Let’s improve this project together!


