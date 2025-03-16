## **Medical Test Management System**

This Python script (`main.py`) manages medical test records, including adding, updating, filtering, and exporting/importing test data.

---

### **Overview**
The system stores and retrieves patient test results efficiently. It ensures accuracy, validation, and easy access to records.

---

### **Key Functionalities**

#### **1. Adding a New Medical Test**
- Accepts a test name and its normal range.
- Saves test details in `medicalTest.txt`.
- Requires a turnaround time in `dd-hh-mm` format.

#### **2. Adding a New Medical Test Record**
- Collects patient details:
  - Patient ID (7-digit number)
  - Test name (validated)
  - Test date/time (`YYYY-MM-DD hh:mm`)
  - Test result and unit
  - Test status (Pending, Completed, Reviewed)
- Calculates result time if status is `completed`.

#### **3. Updating Medical Records**
- Allows updating test details for a patient.
- Ensures valid formats for updated values.

#### **4. Updating Medical Tests**
- Modifies test details in `medicalTest.txt`.
- Prevents invalid ranges (e.g., min > max).

#### **5. Filtering Medical Tests**
- Retrieves test records based on:
  - Patient ID
  - Test Name
  - Abnormal test results
  - Test status
  - Date range
  - Turnaround time range

#### **6. Generating Summary Reports**
- Computes:
  - **Minimum, maximum, and average** test values.
  - **Minimum, maximum, and average** turnaround times.

### **Example Output:**
#### Main Menu
Upon running the program, the user is presented with the following menu:
```
Medical Test Management System
1. Add a new medical test
2. Add a new medical test record
3. Update patient records
4. Update medical tests
5. Filter medical tests
6. Generate textual summary reports
7. Export medical records to CSV
8. Import medical records from CSV
9. Exit
Enter your choice (1-9):
```

### 1. Add a New Medical Test
```
Enter the file name:
medicalTest.txt
Enter the name of the test:
BGT
Does the test have a minimum normal result? (yes/no):
yes
Enter the minimum value of the test result:
20
Enter the maximum value of the test result:
100
Enter the turnaround time of the test (format: dd-hh-mm):
30-20-10
```

### 2. Add a New Medical Test Record
```
Enter the file name:
medicalRecord.txt
Enter the new patient ID:
1300500
Enter the test name:
myTest
Enter the test date (YYYY-MM-DD):
2024-03-01
Enter the test time (hh:mm):
08:00
Enter the result for the test:
30
Enter the test status:
reviewed
```

### 3. Update Patient Records
```
Enter patient ID:
1300520
Choose a test to update:
4
Enter the new test name:
LDL
Enter the new test date (YYYY-MM-DD):
2024-07-09
Enter the new test time (hh:mm):
08:30
Enter the new result for the test:
40
Enter the new test status:
reviewed
```

### 5. Filter Medical Tests
```
Do you want to filter the medical records based on one or two criteria? (1 or 2):
2
Choose filtering criteria:
1- Patient ID
2- Test Name
3- Abnormal Tests
4- Test added within a specific period
5- Test status
6- Test turnaround time within a period
Enter first criteria:
1
Enter second criteria:
2
Enter patient ID:
1234567
Enter the test name:
hgb
Filtered Results:
1234567: hgb, 2022-12-31 23:55, 15 mg/dL, completed, 2023-02-01 06:25
1234567: hgb, 2022-12-30 23:30, 15 mg/dL, completed, 2023-01-31 06:00
```

### 6. Generate Summary Reports
```
Minimum Test Value: 15.0
Maximum Test Value: 15.0
Average Test Value: 15.00
Minimum Turnaround Time: 31 days 6 hours 30 minutes
Maximum Turnaround Time: 31 days 6 hours 30 minutes
Average Turnaround Time: 31 days 6 hours 30 minutes
```

### 7. Export to CSV
```
Records have been successfully exported to medical_records.csv
```


#### 8. Import from CSV
```plaintext
Records have been successfully imported from medical_records.csv

['1234567', 'ldl', '2022-12-12', '20:20', '12', 'mg/dL', 'reviewed', '', '']
['1300500', 'LDL', '2024-03-01', '05:20', '13.5', 'mg/dL', 'completed', '2024-03-01', '05:22']
['1300500', 'BGT', '2024-03-01', '06:00', '14.0', 'mg/dL', 'completed', '2024-03-01', '06:10']
['1300501', 'LDL', '2024-03-01', '06:30', '110', 'mg/dL', 'pending', '', '']
['1300501', 'BGT', '2024-03-01', '07:00', '13.8', 'mg/dL', 'completed', '2024-03-01', '07:15']
['1300511', 'LDL', '2024-03-02', '07:30', '110', 'mg/dL', 'pending', '', '']
['1300511', 'Systole', '2024-03-02', '08:00', '120', 'mm Hg', 'completed', '2024-03-02', '08:20']
['1300520', 'BGT', '2024-03-04', '04:40', '13.7', 'mg/dL', 'completed', '2024-03-04', '04:55']
['1300520', 'Systole', '2024-03-04', '05:00', '115', 'mm Hg', 'completed', '2024-03-04', '05:15']
['1300520', 'Diastole', '2024-03-04', '05:30', '75', 'mm Hg', 'completed', '2024-03-04', '05:45']
['1300520', 'LDL', '2024-03-04', '06:00', '108', 'mg/dL', 'pending', '', '']
['1300520', 'BGT', '2024-03-04', '06:30', '14.2', 'mg/dL', 'completed', '2024-03-04', '06:45']
['1234567', 'hgb', '2022-12-31', '23:55', '15', 'mg/dL', 'completed', '2023-02-01', '06:25']
['1234567', 'hgb', '2022-12-30', '23:30', '15', 'mg/dL', 'completed', '2023-01-31', '06:00']
['1234567', 'bgt', '2022-12-12', '20:20', '15', 'mg/dL', 'reviewed', '', '']
['1234595', 'bgt', '2022-11-11', '20:20', '12', 'mg/dL', 'completed', '2022-11-12', '08:26']
['1234567', 'ggg', '2022-12-12', '22:22', '14', 'mg/dL', 'pending', '', '']
['1234567', 'myTest', '2022-03-03', '23:23', '34', 'mg/dL', 'completed', '2022-03-04', '00:53']
['1300500', 'myTest', '2024-03-01', '08:00', '30', 'mg/dL', 'reviewed', '', '']

```





