# IDS-706 Data Engineering Assignment
## Mini Project : Polars Descriptive Statistics Script

#### badge

### Requirements
    1. Python script using Polars for descriptive statistics
    2. Read a dataset (CSV or Excel)
    3. Generate summary statistics (mean, median, standard deviation)
    4. Create at least one data visualization

### Deliverables
    1. Python script 
    2. CI/CD with badge
    3. Generated summary report (PDF or markdown) via CI/CD for extra credit or making your own PDF or MD file and pushing it

### Analysis
Dataset : HR.csv (also known as HR Analytics Employee Attrition & Performance)
 - The data used in this analysis was provided by IBM and was originally created to study employee turnover.
 - From the available variables, I specifically focused on the "Age" at retirement.

### Progress
#### Step1. 
Created Github Repository and required files such as Makerfile, requirement.txt, CICD.yml, Dockerfile, devcontainer.json and so on

<YAML> 
![yml](https://github.com/user-attachments/assets/b7a8b0ea-f5b2-4e80-86ef-b76231bb2f33)

<Makerfile>
![Makerfile](https://github.com/user-attachments/assets/87853e79-95bc-447e-9aec-473bfd3e1792)

<Requirements>
![Requirements](https://github.com/user-attachments/assets/705b349f-659d-4061-94f6-9f3da63925ca)

<Devcontainer>
![Devcontainer](https://github.com/user-attachments/assets/13abb4f4-a10c-469d-9251-b8c989dd714e)

<Docker>
![Docker](https://github.com/user-attachments/assets/e4e41cdf-d078-4bb2-8151-210d6d78ca3d)

#### Step2. 
Build a main.py and main_test.py. in 'main.py' this import CSV file(HR.csv) and calculate average, median, and Standard deviation of retired employees. Additionally, plot a histrogram to visualize the age distrubution of the retired employees.

<main.py>
![main](https://github.com/user-attachments/assets/213bba61-2af9-4116-8ea2-d5ebaee3db4f)

<main_test.py>
![test](https://github.com/user-attachments/assets/b3589147-68d2-40e8-a4f2-6545d5f88798)

<Mean, Median, Standard Deviation and Histogram>
![mean, median, std and histogram](https://github.com/user-attachments/assets/061e19eb-a47b-4b7c-b058-03aa1d2f3552

#### Step3. 
Verify if the GitHub Action is working properly
<img width="1094" alt="lint, test, format" src="https://github.com/user-attachments/assets/e262feef-059f-47e7-922f-a5c918fcda3e">



