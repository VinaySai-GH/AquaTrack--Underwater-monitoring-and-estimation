# 🌊 AquaTrack: Intelligent Groundwater Resource Assessment System

> **A Smart India Hackathon 2025 Project**  
> Developed to revolutionize India's groundwater assessment and management through AI, GIS, and data-driven analytics.

---

## 🧭 Overview

**AquaTrack** is a GIS-based intelligent system designed for the **Assessment of Dynamic Ground Water Resources of India**.  
The project integrates **data analytics**, **AI-powered estimation**, and **interactive visualizations** to enhance the capabilities of the existing **INGRES (India Groundwater Resource Estimation System)**.

Built for the **Central Ground Water Board (CGWB)** and **DoWR, RD & GR, MoJS**, AquaTrack streamlines the estimation, visualization, and reporting of groundwater data across all States and Union Territories of India.

---

## 🚀 Key Features

- 🔹 **AI-Driven Groundwater Estimation** — Predict dynamic groundwater levels using ML-based modeling.
- 🔹 **GIS-Integrated Mapping** — Visualize aquifers, recharge zones, and well data on an interactive map.
- 🔹 **Real-Time Data Analytics** — Monitor, process, and analyze groundwater resources dynamically.
- 🔹 **Centralized Data Hub** — Consolidate multi-state water datasets into one unified platform.
- 🔹 **Interactive Dashboards** — Display statistical insights and time-series analytics for decision-makers.
- 🔹 **Automated Report Generation** — Generate state-wise and basin-wise reports in a single click.

---
## 🏗️ System Architecture

+-------------------+ +------------------------+
| User Interface | <----> | Backend API Services |
| (React / Leaflet) | | (Node.js / Express) |
+-------------------+ +------------------------+
| |
v v
+-------------------+ +------------------------+
| Data Processing | <----> | Database Layer |
| (Python / ML) | | (PostgreSQL + PostGIS) |
+-------------------+ +------------------------+




---

## ⚙️ Tech Stack

| Layer | Technologies Used |
|-------|--------------------|
| 🌐 **Frontend** | React.js, TailwindCSS, Leaflet.js |
| 🧠 **Backend** | Node.js, Express.js |
| 🗄️ **Database** | PostgreSQL, PostGIS |
| 🤖 **Machine Learning** | Python, Scikit-learn, Pandas |
| ☁️ **Deployment** | Docker, Nginx, AWS (optional) |

---

## 📊 Core Modules

| Module | Description |
|--------|-------------|
| 🗺️ **GIS Mapping** | Displays groundwater levels, aquifer boundaries, and recharge zones. |
| 🔍 **AI Estimation Engine** | Predicts dynamic groundwater availability using ML models. |
| 📈 **Data Analytics Dashboard** | Offers trends, comparisons, and performance metrics. |
| 📚 **Report Generator** | Creates downloadable state and basin-level reports. |
| 🔒 **User Authentication** | Role-based access control for admins and engineers. |

---

## 🧩 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AquaTrack.git
cd AquaTrack

####Setup the environment variables

DATABASE_URL=postgresql://postgres:password@localhost:5432/aquatrack
JWT_SECRET=your_jwt_secret
NODE_ENV=development
PORT=5000


####Run the backend

cd backend
npm install
npm start

####Run the frontend
cd frontend
npm install
npm run dev


####Run with the docker
docker-compose up --build

###👨‍💻 Team AquaTrack
| Role                                | Name                     | Responsibility                                                                  |
| ------------------------------------| -------------------------| -------------------------------------------------------------------------------- |
| 💡 **Team Lead / Backend Dev**      | *Karthik Tamarapalli*    | System architecture, API design,database integration,documentation,ppt designing|
| 🧠 **AI & Data Analyst**            | *Vinay Sai myneni*       | Model training, prediction algorithms                                           |
| 🗺️ **Frontend Developer**           | *Sri Varshini *          | UI/UX                                                                           |
| 📊 **Data Visualization & Reports** | *Maneesh Reddy*          | Input and output token recognition and front end integration , chart integration|
| 💬 **Front end visualizer**         | *Siri Chandana*          | Styling of the front end components                                             |
|     **Technical Presenter**         |  *Tamil *                 |Designing of the ppt,integration of backend from frontend side                   |


###🌏 Acknowledgment

Developed for the Smart India Hackathon 2025, under the guidance of
Central Ground Water Board (CGWB) and Ministry of Jal Shakti, Government of India.


###💧 "Sustainable water today ensures life tomorrow."
🏗️ System Architecture

