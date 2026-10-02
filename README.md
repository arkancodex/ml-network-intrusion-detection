# AI-NIDS --- Network Intrusion Detection System

> **Practical No. 10 --- Data Security Lab**\
> **Machine Learning Based Intrusion Detection System**

A Python and Flask based Network Intrusion Detection System (NIDS) that
uses machine learning to analyse network-traffic records and classify
them as **Normal** or different categories of network attacks. The
system provides a real-time dashboard for monitoring analysed records,
detected alerts, traffic classification, confidence values, and model
activity.

------------------------------------------------------------------------

## 📌 Practical Information

  -----------------------------------------------------------------------
  Item                                Details
  ----------------------------------- -----------------------------------
  **Practical No.**                   10

  **Title**                           To develop an Intrusion Detection
                                      System using Machine Learning
                                      Algorithms


  **System Type**                     Network-based Intrusion Detection
                                      System (NIDS)

  **Dataset**                         NSL-KDD

  **Primary ML Algorithm**            Random Forest

  **Backend**                         Python, Flask

  **ML/Data Libraries**               Scikit-learn, Pandas, NumPy

  **Frontend**                        HTML, CSS, JavaScript

  **Execution Mode**                  Local web application with
                                      simulated/replayed network traffic
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 👥 Team:
Student name      Roll no 
1. Arkan Shaikh   54
2. Ammar Shaikh   53
3. Pratik Yadav   66
**Department:** Computer Science and Engineering --- Data Science\
**Subject:** Employability Enhancement Program-IV (Data Security Lab)

------------------------------------------------------------------------

# 1. Abstract

An Intrusion Detection System (IDS) is a cybersecurity mechanism used to
identify suspicious or malicious activity in a computer network or
system.

This project implements an educational **Machine Learning based Network
Intrusion Detection System** using the **NSL-KDD dataset**. Network
connection records are preprocessed and supplied to a trained **Random
Forest classifier**. The model classifies traffic into categories such
as **Normal, DoS, Probe, R2L, and U2R**.

A Flask-based web application provides a real-time monitoring dashboard.
The dashboard displays the number of analysed records, detected alerts,
normal traffic, detection rate, live traffic records, attack categories,
confidence values, and an activity pulse.

The project demonstrates the complete basic workflow of an ML-assisted
IDS:

**Dataset → Preprocessing → Feature Transformation → ML Model →
Prediction → Classification → Alert → Dashboard**

The current implementation uses replayed NSL-KDD records to simulate a
continuous traffic stream. Therefore, it is intended as an academic
demonstration rather than a production network packet-capture system.

------------------------------------------------------------------------

# 2. Aim

To study and develop a **Machine Learning based Intrusion Detection
System** capable of analysing network traffic records and identifying
normal and potentially malicious network activity.

------------------------------------------------------------------------

# 3. Objectives

The main objectives of this practical are:

-   To understand the concept and purpose of an Intrusion Detection
    System.
-   To study the characteristics of network traffic used for intrusion
    detection.
-   To understand the NSL-KDD intrusion detection dataset.
-   To preprocess numerical and categorical network features.
-   To convert categorical information into machine-learning-compatible
    representations.
-   To train a Random Forest classification model.
-   To classify network records into normal and attack categories.
-   To generate alerts for detected malicious traffic.
-   To display predictions through a web-based monitoring dashboard.
-   To understand the role of machine learning in cybersecurity.
-   To evaluate the behaviour of an ML-based intrusion detection
    workflow.

------------------------------------------------------------------------

# 4. Introduction

Modern computer networks continuously exchange large amounts of data.
Along with legitimate traffic, networks may also experience malicious
activities such as denial-of-service attempts, network scanning,
unauthorised access attempts, and privilege escalation.

An **Intrusion Detection System** monitors activity and identifies
events that may indicate a security threat.

Traditional IDS approaches commonly rely on predefined signatures or
rules. Such systems can be effective against known attack patterns, but
they require signatures to be maintained and updated.

Machine Learning provides a data-driven approach. Instead of manually
defining every possible traffic pattern, a classification model can
learn relationships between network features and known traffic classes
from labelled training data.

In this project, network connection records from NSL-KDD are processed
and classified using a Random Forest model. The predictions are then
exposed through a Flask web application and visualised in a monitoring
dashboard.

------------------------------------------------------------------------

# 5. Problem Statement

Develop a machine-learning-based Network Intrusion Detection System that
analyses network traffic records and classifies them as **normal or
malicious activity**, while providing a clear interface for monitoring
predictions and security alerts.

------------------------------------------------------------------------

# 6. Dataset --- NSL-KDD

The project uses the **NSL-KDD** dataset, a widely used dataset for
educational experiments in network intrusion detection.

The dataset contains network connection records represented using
numerical and categorical attributes.

Examples of feature groups include:

  Feature Type   Examples
  -------------- --------------------------------------
  Numerical      `duration`, `src_bytes`, `dst_bytes`
  Categorical    `protocol_type`, `service`, `flag`
  Target         Normal / Attack category

The implementation uses the available NSL-KDD training and testing
records as the basis for model training and traffic replay.

### Attack Categories

The project represents the major attack groups as:

  -----------------------------------------------------------------------
  Category                            Description
  ----------------------------------- -----------------------------------
  **Normal**                          Legitimate network activity

  **DoS**                             Denial of Service attacks that
                                      attempt to disrupt availability

  **Probe**                           Network scanning or reconnaissance
                                      activity

  **R2L**                             Remote-to-Local attacks involving
                                      unauthorised access

  **U2R**                             User-to-Root attacks involving
                                      privilege escalation
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 7. Machine Learning Approach

## Random Forest

The primary classifier used by the implementation is **Random Forest**.

Random Forest is an ensemble learning algorithm that combines multiple
decision trees. Each tree produces a prediction and the ensemble
combines the individual predictions to obtain the final classification.

### Why Random Forest is suitable for this project

-   Handles non-linear relationships between features.
-   Works well with a mixture of traffic characteristics after
    preprocessing.
-   Provides robust classification through multiple decision trees.
-   Is relatively easy to train and use for an educational
    classification project.
-   Can handle a large number of transformed features.

------------------------------------------------------------------------

# 8. System Architecture

The overall system follows this workflow:

``` text
                ┌──────────────────────┐
                │      NSL-KDD         │
                │      Dataset         │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    Preprocessing     │
                │ Cleaning / Encoding  │
                │ Feature Preparation  │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Random Forest      │
                │   ML Classifier      │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │      Prediction      │
                │ Normal / DoS / Probe │
                │ R2L / U2R            │
                └──────────┬───────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
   ┌──────────────────┐        ┌──────────────────┐
   │ Detection Engine │        │     Logger       │
   │ Classification   │        │ JSONL Records    │
   └────────┬─────────┘        └──────────────────┘
            │
            ▼
   ┌──────────────────────┐
   │     Flask API        │
   │ Stats / Activity /   │
   │ Alerts / Controls    │
   └──────────┬───────────┘
              │
              ▼
   ┌────────────────────────────┐
   │       Web Dashboard        │
   │ KPI Cards                  │
   │ Live Traffic               │
   │ Alert Feed                 │
   │ Activity Pulse             │
   └────────────────────────────┘
```

------------------------------------------------------------------------

# 9. Working Methodology

## Step 1 --- Dataset Preparation

The NSL-KDD records are loaded into the application.

The dataset contains both numerical and categorical network attributes.

## Step 2 --- Preprocessing

The input features are prepared for machine learning.

The preprocessing stage handles the transformation of categorical and
numerical information into a representation suitable for the classifier.

## Step 3 --- Model Training

The Random Forest classifier is trained using the prepared training
data.

The trained model is stored so that it can be reused by the application.

## Step 4 --- Traffic Replay

For the live demonstration, records from the test data are replayed as a
simulated stream.

The simulator allows the web dashboard to continuously receive traffic
records without requiring a physical network packet-capture environment.

## Step 5 --- Prediction

Each incoming/replayed traffic record is passed through the
preprocessing pipeline and Random Forest model.

The model produces:

-   Predicted class
-   Confidence/probability information
-   Normal or attack status

## Step 6 --- Detection and Alerting

If a record is classified as an attack, the detection engine generates
an alert containing relevant information such as:

-   Attack category
-   Source IP
-   Destination IP
-   Timestamp
-   Confidence
-   Network service/protocol information

## Step 7 --- Dashboard Monitoring

The Flask application exposes the current detection information to the
frontend.

The dashboard presents:

-   Records analysed
-   Alerts raised
-   Normal traffic
-   Detection rate
-   Live traffic activity
-   Alert feed
-   Network activity pulse

------------------------------------------------------------------------

# 10. Major Modules

## 10.1 Data Preprocessing

Responsible for preparing raw network records before they are supplied
to the machine-learning model.

Main responsibilities include:

-   Loading data
-   Feature selection
-   Handling categorical attributes
-   Feature transformation
-   Preparing model-compatible input

------------------------------------------------------------------------

## 10.2 Model Training

The training module creates the Random Forest classification model.

Main responsibilities:

-   Loading training data
-   Preparing target labels
-   Training the classifier
-   Saving the trained model and preprocessing information

------------------------------------------------------------------------

## 10.3 Detection Engine

The detection engine acts as the prediction layer.

It receives a network record, prepares the input using the existing
preprocessing pipeline, and obtains a prediction from the trained model.

The result is converted into a readable security classification.

------------------------------------------------------------------------

## 10.4 Traffic Simulator

The simulator provides a continuous stream for the demonstration.

Instead of capturing real packets from a production network, it replays
available test records and presents them as incoming traffic.

This makes the project easy to demonstrate in a controlled college-lab
environment.

------------------------------------------------------------------------

## 10.5 Logger

Detection results are recorded in log files so that analysed activity
can be retained during execution.

The logging layer supports the dashboard's activity and alert
information.

------------------------------------------------------------------------

## 10.6 Flask Web Application

The Flask application acts as the backend server.

It connects the machine-learning pipeline with the web interface.

The dashboard communicates with backend endpoints to retrieve current
statistics, activity records, alerts, and simulator controls.

------------------------------------------------------------------------

## 10.7 Web Dashboard

The dashboard provides a visual monitoring interface.

### Dashboard Components

-   Monitoring status
-   Start / Stop / Reset controls
-   Records analysed
-   Alerts raised
-   Normal traffic
-   Detection rate
-   Live traffic table
-   Alert feed
-   Network activity pulse
-   Dataset and model information
-   Current date and time

------------------------------------------------------------------------

# 11. API Endpoints

The application provides the following dashboard-related routes:

  Method   Endpoint                 Purpose
  -------- ------------------------ ------------------------------------
  `GET`    `/`                      Loads the dashboard
  `GET`    `/api/stats`             Returns current traffic statistics
  `GET`    `/api/activity`          Returns recent network activity
  `GET`    `/api/alerts`            Returns detected alerts
  `POST`   `/api/simulator/start`   Starts traffic simulation
  `POST`   `/api/simulator/stop`    Stops traffic simulation
  `POST`   `/api/clear`             Clears/reset dashboard data

The frontend periodically requests the API data so that the dashboard
can update without manually refreshing the page.

------------------------------------------------------------------------

# 12. Project Structure

``` text
network-intrusion-detection/
│
├── data/
│   ├── KDDTrain+.txt
│   ├── KDDTest+.txt
│   └── other dataset files
│
├── logs/
│   └── runtime detection logs
│
├── models/
│   └── trained model / preprocessing artifacts
│
├── src/
│   ├── app.py
│   ├── columns.py
│   ├── detection_engine.py
│   ├── logger.py
│   ├── preprocessing.py
│   ├── simulator.py
│   └── train_model.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── dashboard.js
│
├── templates/
│   └── dashboard.html
│
├── .gitignore
├── README.md
└── requirements.txt
```

------------------------------------------------------------------------

# 13. Technology Stack

### Programming Language

**Python**

Used for data processing, machine learning, backend logic, simulation,
and logging.

### Machine Learning

**Scikit-learn**

Used to implement the Random Forest classification model and related
preprocessing components.

### Data Processing

**Pandas** and **NumPy**

Used for handling tabular network-traffic data and numerical operations.

### Web Backend

**Flask**

Used to create the local web server and API endpoints.

### Frontend

-   HTML5
-   CSS3
-   JavaScript
-   Responsive dashboard UI

### Dataset

**NSL-KDD**

Used as the network intrusion detection dataset.

------------------------------------------------------------------------

# 14. Installation and Setup

## Prerequisites

Install:

-   Python 3.12 recommended
-   pip
-   Git (optional, for version control)
-   A modern web browser

Python 3.12 is recommended for this project environment to maintain
compatibility with the scientific Python dependencies used by the
application.

------------------------------------------------------------------------

## Step 1 --- Open the Project

``` bash
cd network-intrusion-detection
```

------------------------------------------------------------------------

## Step 2 --- Create a Virtual Environment

Windows:

``` powershell
py -3.12 -m venv venv
```

Activate it:

``` powershell
.\venv\Scripts\activate
```

------------------------------------------------------------------------

## Step 3 --- Install Dependencies

``` powershell
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Step 4 --- Run the Application

``` powershell
python src\app.py
```

The Flask application will start locally.

Open:

``` text
http://127.0.0.1:5000
```

------------------------------------------------------------------------

# 15. Running the Practical Demonstration

After opening the dashboard:

1.  Start the Flask application.
2.  Open the dashboard in the browser.
3.  Start monitoring if the simulator is stopped.
4.  Observe the number of analysed records.
5.  Observe normal and malicious traffic.
6.  Check the alert feed.
7.  Observe attack categories such as DoS and Probe.
8.  Observe confidence values generated for predictions.
9.  Observe the network activity pulse.
10. Use Stop to pause the traffic stream.
11. Use Reset to clear the current monitoring state.

The dashboard is intended to provide a clear visual demonstration of the
ML-based detection workflow.

------------------------------------------------------------------------

# 16. Dashboard Output

The dashboard presents four main security indicators:

### Records Analyzed

Total number of network records processed by the detection system.

### Alerts Raised

Number of analysed records classified as malicious/attack traffic.

### Normal Traffic

Number of analysed records classified as normal.

### Detection Rate

The dashboard's displayed detection-rate metric derived from the
application's current statistics.

The live traffic table additionally shows:

-   Record/time
-   Source IP
-   Destination IP
-   Protocol
-   Service
-   Attack category
-   Confidence
-   Normal/Attack status

------------------------------------------------------------------------

# 17. Example Detection Categories

The dashboard can display classifications such as:

``` text
Normal
DoS
Probe
R2L
U2R
```

For example:

``` text
Source IP       Destination IP       Protocol   Category   Status
214.155.x.x     222.58.x.x           TCP        Normal     NORMAL
81.76.x.x       185.26.x.x           TCP        DoS        ATTACK
25.55.x.x       107.41.x.x           TCP        Probe      ATTACK
```

The exact records and values change during simulation.

------------------------------------------------------------------------

# 18. Advantages

-   Demonstrates the practical application of machine learning in
    cybersecurity.
-   Provides an easy-to-understand web interface.
-   Uses a recognised intrusion-detection dataset.
-   Separates preprocessing, model detection, simulation, logging, and
    presentation layers.
-   Provides continuous traffic replay for demonstration.
-   Displays classification confidence and attack categories.
-   Can be extended with additional models and datasets.
-   Suitable for academic demonstration and ML/cybersecurity learning.

------------------------------------------------------------------------

# 19. Limitations

The current system is an educational prototype and has several
limitations:

-   The live traffic stream is simulated/replayed from dataset records.
-   It does not perform production packet capture from a network
    interface.
-   NSL-KDD is an older benchmark dataset and may not represent all
    modern attack patterns.
-   Model performance depends on the quality and distribution of
    training data.
-   False positives and false negatives can occur.
-   Previously unseen attacks may not be correctly classified.
-   Real-world deployment would require additional network monitoring,
    security, scalability, and model-validation mechanisms.

These limitations should be considered when interpreting the dashboard
results.

------------------------------------------------------------------------

# 20. Future Scope

The project can be extended in several directions:

### Real Network Traffic Capture

Integrate packet-capture technologies such as:

-   Scapy
-   PyShark
-   Zeek
-   Network interface monitoring

This would allow the system to process real network traffic instead of
replayed dataset records.

### Advanced Machine Learning

Additional models could be evaluated, including:

-   Decision Tree
-   Logistic Regression
-   XGBoost
-   Support Vector Machine
-   Neural Networks
-   Deep Learning based classifiers

### Improved Datasets

The system could be evaluated using more recent cybersecurity datasets
containing modern network behaviours and attacks.

### Advanced Alert Management

Future versions could include:

-   Alert severity levels
-   Alert history
-   Search and filtering
-   Exportable security reports
-   Email or messaging notifications

### Security Operations Integration

The system could eventually be connected to:

-   SIEM platforms
-   Security logs
-   Incident-response workflows
-   Threat-intelligence sources

### Production Deployment

A production version would require:

-   Real-time packet ingestion
-   Secure authentication
-   Database-backed storage
-   Model monitoring
-   Periodic retraining
-   High-availability architecture
-   Strong logging and access controls

------------------------------------------------------------------------

# 21. Testing

The following basic tests can be performed during the practical
demonstration:

  Test                 Expected Result
  -------------------- -------------------------------------------
  Launch application   Dashboard loads successfully
  Start monitoring     Traffic records begin appearing
  Stop monitoring      Traffic simulation stops
  Start after Stop     Monitoring resumes
  Reset                Monitoring state/data is reset
  Normal record        Record appears with `NORMAL` status
  Attack record        Record appears with `ATTACK` status
  Alert generation     Malicious record appears in Alert Feed
  Statistics update    KPI values change with incoming records
  Activity pulse       Graph/pulse updates with traffic activity
  Date/time            Dashboard clock updates continuously

------------------------------------------------------------------------

# 22. Result

The developed system successfully demonstrates an educational **Machine
Learning based Network Intrusion Detection System**.

The system is capable of:

-   Processing network-traffic records.
-   Applying preprocessing before prediction.
-   Using a Random Forest classifier for traffic classification.
-   Identifying normal and malicious traffic categories.
-   Generating alerts for detected attack activity.
-   Displaying prediction information through a Flask web application.
-   Continuously updating the monitoring dashboard using simulated
    traffic.

The practical therefore demonstrates the fundamental application of
machine learning to network intrusion detection.

------------------------------------------------------------------------

# 23. Conclusion

This project demonstrates how machine learning can be applied to the
problem of network intrusion detection.

Using the NSL-KDD dataset, network connection records are transformed
into a form suitable for machine learning and classified using a Random
Forest model. The prediction results are connected to a Flask-based
dashboard that provides a real-time visual representation of network
activity and detected alerts.

The project provides a practical understanding of the complete
ML-assisted cybersecurity workflow:

**Data Collection → Preprocessing → Model Training → Prediction →
Detection → Alerting → Visualization**

Although the current implementation uses simulated/replayed traffic and
is intended for academic use, the architecture provides a foundation
that can be extended toward real-time network monitoring and more
advanced cybersecurity applications.

------------------------------------------------------------------------

# 24. References

1.  **NSL-KDD Dataset** --- Network intrusion detection benchmark
    dataset.
2.  **Scikit-learn Documentation** --- Machine learning algorithms and
    preprocessing.
3.  **Python Documentation** --- Python programming language reference.
4.  **Flask Documentation** --- Python web application framework.
5.  General academic literature on machine-learning-based network
    intrusion detection.

