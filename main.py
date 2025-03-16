import re
import csv


def check_file_existence(file_name):
    try:
        file = open(file_name, "r+")
        return file
    except FileNotFoundError:
        raise "File not found"


def validate_test_name(test_name):
    while True:
        validName = True
        for i in test_name:
            if not i.isalpha():
                validName = False

        if not validName:
            print("Invalid test name. Test names should only contain alphabetic characters.")
            test_name = input()
        else:
            break
    return test_name


def check_test_existence(test_name):
    tests = []
    with open("medicalTest.txt", "r+") as file:
        for line in file:
            test = ""
            start = False
            for char in line:
                if char == "(":
                    start = True
                elif char == ")":
                    break
                elif start == True:
                    test += char
            tests.append(test)

    for i in range(len(tests)):
        tests[i] = tests[i].lower()

    while True:
        test_name1 = test_name.lower()
        if test_name1 not in tests:
            print("the test does not exist")
            print("enter a new test name")
            test_name = input()
        else:
            break
    return test_name


def validate_test_result(test_result):
    while True:
        try:
            float(test_result)
            if float(test_result) < 0:
                print("Test result should be a positive number")
                print("enter a new test name")
                test_result = input()
                continue
            break
        except ValueError:
            print("Invalid result")
            print("Please enter a valid result:")
            test_result = input()
    return test_result


def check_range():
    min_result = 0
    max_result = 0
    print("does the test has a minimum normal result?")
    while True:
        answer = input()
        if answer == "yes":
            print("please enter the minimum value of the test result:")
            min_result = input()
            min_result = validate_test_result(min_result)
            print("please enter the maximum value of the test result:")
            max_result = input()
            max_result = validate_test_result(max_result)
            while int(min_result) >= int(max_result):
                print("minimum normal result should be smaller than maximum normal test result.")
                print("please enter the maximum value of the test result:")
                max_result = input()
                max_result = validate_test_result(max_result)
            else:
                break
        elif answer == "no":
            print("please enter the maximum value of the test result:")
            max_result = input()
            break
        else:
            print("please enter yes or no:")
    return min_result, max_result


def validate_turnaround_time(turnaround_time):
    while True:
        # Check if the format is correct: dd-hh-mm
        if (
                len(turnaround_time) == 8 and
                turnaround_time[0:2].isdigit() and
                turnaround_time[2] == '-' and
                turnaround_time[3:5].isdigit() and
                turnaround_time[5] == '-' and
                turnaround_time[6:8].isdigit()
        ):
            break
        else:
            print("Please enter a valid turnaround time of the test (format: dd-hh-mm):")
            turnaround_time = input()
    return turnaround_time


def validate_patient_id(patient_id):
    while True:
        if not patient_id.isnumeric() or len(patient_id) != 7:
            print("Invalid patient id")
            print("enter the new patient id")
            patient_id = input()
        else:
            break
    return patient_id


def validate_test_date(test_date):
    while True:
        if (
                len(test_date) == 10 and
                test_date[0:4].isnumeric() and
                test_date[4] == '-' and
                test_date[5:7].isnumeric() and
                test_date[7] == '-' and
                test_date[8:10].isnumeric()
        ):
            if int(test_date[5:7]) >= 1 and int(test_date[5:7]) <= 12:
                if int(test_date[5:7]) in [1, 3, 5, 7, 8, 10, 12]:
                    if int(test_date[8:10]) >= 1 and int(test_date[8:10]) <= 31:
                        break
                elif int(test_date[5:7]) in [4, 6, 9, 11]:
                    if int(test_date[8:10]) >= 1 and int(test_date[8:10]) <= 30:
                        break
                elif int(test_date[5:7]) == 2:
                    if (int(test_date[0:4]) % 4 == 0 and int(test_date[0:4]) % 100 != 0) or int(
                            test_date[0:4]) % 400 == 0:
                        if int(test_date[8:10]) >= 1 and int(test_date[8:10]) <= 29:
                            break
                    else:
                        if int(test_date[8:10]) >= 1 and int(test_date[8:10]) <= 28:
                            break
        print("the test date is invalid")
        print("Enter the test date in the format YYYY-MM-DD")
        test_date = input()
    return test_date


def validate_test_time(test_time):
    while True:
        if (
                len(test_time) == 5 and
                test_time[0:2].isnumeric() and
                test_time[2] == ':' and
                test_time[3:5].isnumeric()
        ):
            if 0 <= int(test_time[0:2]) <= 23 and 0 <= int(test_time[3:5]) <= 59:
                break
        print("The test time is invalid")
        print("Enter the test time in the format hh:mm")
        test_time = input().strip()
    return test_time


def validate_test_status(test_status):
    status = ['completed', 'reviewed', 'pending']
    test_status = test_status.lower()
    while test_status not in status:
        print("Invalid test status")
        print("Please enter correct test status")
        test_status = input()
    return test_status


def add_medical_tests():
    print("Enter the file name:")
    file_name = input()
    file = check_file_existence(file_name)

    print("Enter the name of the test:")
    test_name = input()
    test_name = validate_test_name(test_name)

    min_value, max_value = check_range()

    print("enter the turnaround time of the test:")
    turnaround_time = input("Enter turnaround time (format: dd-hh-mm): ")
    turnaround_time = validate_turnaround_time(turnaround_time)
    with open(file_name, 'a') as file:  # Open the file in append mode
        if int(min_value) == 0:
            file.write("Name: (" + test_name + "); Range: < " + max_value + "; Unit: mm Hg, " + turnaround_time + "\n")
        else:
            file.write(
                "Name: (" + test_name + "); Range: > " + min_value + ", < " + max_value + "; Unit: mm Hg, " + turnaround_time + "\n"
            )


def add_medical_record():
    print("Enter the file name:")
    file_name = input()
    file = check_file_existence(file_name)

    #medicalRecord.txt
    print("enter the new patient id")
    patient_id = input()
    patient_id = validate_patient_id(patient_id)

    print("enter the test name")
    test_name = input()
    test_name = check_test_existence(test_name)

    print("enter the test date in the format YYYY-MM-DD")
    test_date = input()
    test_date = validate_test_date(test_date)
    test_date1 = test_date.split('-')
    test_year = int(test_date1[0])
    test_month = int(test_date1[1])
    test_day = int(test_date1[2])

    print("enter the test time in the format hh:mm")
    test_time = input()
    test_time = validate_test_time(test_time)
    test_time1 = test_time.strip().split(':')
    test_hour = int(test_time1[0])
    test_minute = int(test_time1[1])

    print("Enter the result for the test")
    test_result = input()
    test_result = validate_test_result(test_result)

    print("enter the test status")
    test_status = input()
    test_status = validate_test_status(test_status)

    if test_status == 'completed':
        with open("medicalTest.txt", "r") as file:  # Open file in read mode
            for line in file:
                if test_name.lower() in line.lower():
                    turnaround_time = line.split(',')[-1].strip()
                    break
        turnaround_time1 = turnaround_time.split('-')
        turnaround_time_days = int(turnaround_time1[0])
        turnaround_time_hour = int(turnaround_time1[1])
        turnaround_time_minute = int(turnaround_time1[2])

        # Adding turnaround time to the test time
        test_minute += turnaround_time_minute
        if test_minute >= 60:
            extra_hours = test_minute // 60
            test_minute %= 60
            test_hour += extra_hours

        test_hour += turnaround_time_hour
        if test_hour >= 24:
            extra_days = test_hour // 24
            test_hour %= 24
            test_day += extra_days

        # Adding days to the test date
        test_day += turnaround_time_days

        # List of days in each month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Adjust for leap years
        if (test_year % 4 == 0 and test_year % 100 != 0) or (test_year % 400 == 0):
            days_in_month[1] = 29  # February has 29 days in a leap year

        # Adjust for overflow in days and months
        while test_day > days_in_month[test_month - 1]:
            test_day -= days_in_month[test_month - 1]
            test_month += 1
            if test_month > 12:
                test_month = 1
                test_year += 1

        test_result_date = f"{test_year:04d}-{test_month:02d}-{test_day:02d}"
        test_result_time = f"{test_hour:02d}:{test_minute:02d}"

    with open(file_name, 'a') as file:  # Open the file in append mode
        if test_status == "completed":
            file.write(
                patient_id + ": " + test_name + ", " + test_date + " " + test_time + ", " + test_result + ", mg/dL, " + test_status + ", " + test_result_date + " " + test_result_time + "\n"
            )
        else:
            file.write(
                patient_id + ": " + test_name + ", " + test_date + " " + test_time + ", " + test_result + ", mg/dL, " + test_status + "\n"
            )


def update_test_record():
    newLine = []
    print("Enter patient ID:")
    while True:
        patient_id = input().strip()  # Strip any extra spaces from input
        patient_id = validate_patient_id(patient_id)
        patient_tests = []
        with open("medicalRecord.txt", "r") as file:  # Open file in read mode
            found = False
            for line in file:
                if patient_id in line:  # Strip any extra spaces from line
                    patient_tests.append(line.strip())
                    found = True

            if not found:
                print("Patient ID not found in the file.")
                print("Enter the patient ID")
            else:
                break

    line_number = 1
    for patient_test in patient_tests:
        print(str(line_number) + "- " + patient_test)
        line_number += 1

    print("choose a test")
    test_line = input()
    while True:
        if int(test_line) < 1 or int(test_line) > len(patient_tests):
            print("please choose an existing test")
            test_line = input()
        else:
            break

    testInfo = patient_tests[int(test_line) - 1].split(':', 1)[1].split(',')
    patient_old_test_name = testInfo[0].strip()
    newLine.append(patient_old_test_name)
    patient_old_test_date_time = testInfo[1].strip().split(' ')
    patient_old_test_date = patient_old_test_date_time[0].strip()
    newLine.append(patient_old_test_date)
    patient_old_test_time = patient_old_test_date_time[1].strip()
    newLine.append(patient_old_test_time)
    patient_old_test_result = testInfo[2].strip()
    newLine.append(patient_old_test_result)
    patient_old_test_status = testInfo[4].strip()
    newLine.append(patient_old_test_status)

    patient_old_test_status = patient_old_test_status.lower()
    if patient_old_test_status == 'completed':
        patient_old_result_date_time = testInfo[5].strip().split(' ')
        patient_old_result_date = patient_old_result_date_time[0].strip()
        newLine.append(patient_old_result_date)
        patient_old_result_time = patient_old_result_date_time[1].strip()
        newLine.append(patient_old_result_time)
    else :
        newLine.append("")
        newLine.append("")


    print("enter the new test name")
    new_test_name = input()
    new_test_name = check_test_existence(new_test_name)
    newLine[0] = new_test_name

    print("enter the new test date in the format YYYY-MM-DD")
    new_test_date = input()
    new_test_date = validate_test_date(new_test_date)
    newLine[1] = new_test_date
    test_date1 = new_test_date.split('-')
    test_year = int(test_date1[0])
    test_month = int(test_date1[1])
    test_day = int(test_date1[2])

    print("enter the new test time in the format hh:mm")
    new_test_time = input()
    new_test_time = validate_test_time(new_test_time)
    newLine[2] = new_test_time
    test_time1 = new_test_time.strip().split(':')
    test_hour = int(test_time1[0])
    test_minute = int(test_time1[1])

    print("Enter the new result for the test")
    new_test_result = input()
    new_test_result = validate_test_result(new_test_result)
    newLine[3] = new_test_result

    print("enter the new test status")
    new_test_status = input()
    new_test_status = validate_test_status(new_test_status)
    newLine[4] = new_test_status

    if new_test_status == 'completed':
        with open("medicalTest.txt", "r") as file:  # Open file in read mode
            for line in file:
                if new_test_name.lower() in line.lower():
                    turnaround_time = line.split(',')[-1].strip()
                    break
        turnaround_time1 = turnaround_time.split('-')
        turnaround_time_days = int(turnaround_time1[0])
        turnaround_time_hour = int(turnaround_time1[1])
        turnaround_time_minute = int(turnaround_time1[2])

        # Adding turnaround time to the test time
        test_minute += turnaround_time_minute
        if test_minute >= 60:
            extra_hours = test_minute // 60
            test_minute %= 60
            test_hour += extra_hours

        test_hour += turnaround_time_hour
        if test_hour >= 24:
            extra_days = test_hour // 24
            test_hour %= 24
            test_day += extra_days

        # Adding days to the test date
        test_day += turnaround_time_days

        # List of days in each month
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Adjust for leap years
        if (test_year % 4 == 0 and test_year % 100 != 0) or (test_year % 400 == 0):
            days_in_month[1] = 29  # February has 29 days in a leap year

        # Adjust for overflow in days and months
        while test_day > days_in_month[test_month - 1]:
            test_day -= days_in_month[test_month - 1]
            test_month += 1
            if test_month > 12:
                test_month = 1
                test_year += 1

        test_result_date = f"{test_year:04d}-{test_month:02d}-{test_day:02d}"
        newLine[5] = test_result_date
        test_result_time = f"{test_hour:02d}:{test_minute:02d}"
        newLine[6] = test_result_time

    if new_test_status == 'completed':
        newLine1 = patient_id + ": " + newLine[0] + ", " + newLine[1] + " " + newLine[2] + ", " + newLine[
            3] + ", mg/dL, " + newLine[4] + ", " + newLine[5] + " " + newLine[6] + "\n"
    else:
        newLine1 = patient_id + ": " + newLine[0] + ", " + newLine[1] + " " + newLine[2] + ", " + newLine[
            3] + ", mg/dL, " + newLine[4] + "\n"

    print("the new test Info : " + newLine1)

    with open("medicalRecord.txt", "r") as file:
        lines = file.readlines()

    with open("medicalRecord.txt", "w") as file:
        for line in lines:
            if line.strip() == patient_tests[int(test_line) - 1].strip():
                file.write(newLine1 + '\n')
            else:
                file.write(line)


def update_medicalTest():
    print("enter the test name")
    test_name = input()
    test_name = check_test_existence(test_name)
    min_value = 0
    with open("medicalTest.txt", "r") as file:  # Open file in read mode
        for line in file:
            if test_name.lower() in line.lower():
                test = line.strip()
                parts = line.split(';')
                test_range = parts[1].replace('Range: ', '').strip()
                turnaround_time = line.split(',')[-1].strip()
                if '>' in test_range:
                    range_parts = test_range.split(',')
                    min_value = range_parts[0].replace('>', '').strip()
                    max_value = range_parts[1].replace('<', '').strip()
                else:
                    max_value = test_range.replace('<', '').strip()

    print("Enter the new turnaround time in the format dd-hh-mm")
    new_turnaround_time = input()
    new_turnaround_time = validate_turnaround_time(new_turnaround_time)
    newLine = re.sub(f"{turnaround_time}", f"{new_turnaround_time}", test)

    if min_value:
        print("enter the new minimum range value")
        new_min_value = input()
        print("enter the new maximum range value")
        new_max_value = input()
        while new_max_value <= new_min_value:
            print("the new maximum range value must be greater than the minimum range value")
            print("enter the new maximum range value")
            new_max_value = input()

        newLine = re.sub(f"{min_value}", f"{new_min_value}", newLine)
        newLine = re.sub(f"{max_value}", f"{new_max_value}", newLine)

    else:
        print("enter the new maximum range value")
        new_max_value = input()
        newLine = re.sub(f"{max_value}", f"{new_max_value}", newLine)

    print(newLine)

    with open("medicalTest.txt", "r") as file:
        lines = file.readlines()

    with open("medicalTest.txt", "w") as file:
        for line in lines:
            if line.strip() == test.strip():
                file.write(newLine + '\n')
            else:
                file.write(line)


def filter_tests_basedOn_range(place):
    results_list = []
    for line in place:
        testInfo = line.split(':', 1)[1].split(',')
        test_name = testInfo[0].strip()
        test_result = testInfo[2].strip()
        min_value = 0
        with open("medicalTest.txt", "r") as file:  # Open file in read mode
            for line1 in file:
                if test_name.lower() in line1.lower():
                    parts = line1.split(';')
                    test_range = parts[1].replace('Range: ', '').strip()
                    if '>' in test_range:
                        range_parts = test_range.split(',')
                        min_value = range_parts[0].replace('>', '').strip()
                        max_value = range_parts[1].replace('<', '').strip()
                    else:
                        max_value = test_range.replace('<', '').strip()
            if min_value:
                if float(test_result) < float(min_value) or float(test_result) > float(max_value):
                    results_list.append(line)
            else:
                if float(test_result) > float(max_value):
                    results_list.append(line)
    return results_list


def filtered_tests_basedOn_id_and_name_and_status(place, value):
    results_list = []
    for line in place:
        if value.lower() in line.lower():
            #    print(line.strip())
            results_list.append(line)

    return results_list


def filtered_tests_basedOn_dates(place, start_date, end_date):
    results_list = []
    start_date_year = int(start_date.split('-')[0])
    end_date_year = int(end_date.split('-')[0])
    start_date_month = int(start_date.split('-')[1])
    end_date_month = int(end_date.split('-')[1])
    start_date_day = int(start_date.split('-')[2])
    end_date_day = int(end_date.split('-')[2])
    for line in place:
        testInfo = line.split(':', 1)[1].split(',')
        patient_test_date_time = testInfo[1].strip().split(' ')
        patient_test_date = patient_test_date_time[0].strip()
        patient_test_date_year = int(patient_test_date.split('-')[0])
        patient_test_date_month = int(patient_test_date.split('-')[1])
        patient_test_date_day = int(patient_test_date.split('-')[2])
        if (start_date_year < patient_test_date_year) or (
                start_date_year == patient_test_date_year and start_date_month < patient_test_date_month) or (
                start_date_year == patient_test_date_year and start_date_month == patient_test_date_month and start_date_day <= patient_test_date_day):
            if (end_date_year > patient_test_date_year) or (
                    patient_test_date_year == end_date_year and end_date_month > patient_test_date_month) or (
                    patient_test_date_year == end_date_year and end_date_month == patient_test_date_month and end_date_day >= patient_test_date_day):
                results_list.append(line)
    return results_list


def filtered_tests_basedOn_turnaround_time(place, min_turnaround, max_turnaround):
    results_list = []
    for line in place:
        testInfo = line.split(':', 1)[1].split(',')
        test_name = testInfo[0].strip()
        with open("medicalTest.txt", "r") as file:
            for line1 in file:
                if test_name.lower() in line1.lower():
                    turnaround_time = line1.split(',')[-1].strip()

        min_turnaround_days = int(min_turnaround.split('-')[0])
        max_turnaround_days = int(max_turnaround.split('-')[0])
        min_turnaround_hours = int(min_turnaround.split('-')[1])
        max_turnaround_hours = int(max_turnaround.split('-')[1])
        min_turnaround_minutes = int(min_turnaround.split('-')[2])
        max_turnaround_minutes = int(max_turnaround.split('-')[2])

        turnaround_days = int(turnaround_time.split('-')[0])
        turnaround_hours = int(turnaround_time.split('-')[1])
        turnaround_minutes = int(turnaround_time.split('-')[2])

        if ((min_turnaround_days < turnaround_days or
             (min_turnaround_days == turnaround_days and min_turnaround_hours < turnaround_hours) or
             (
                     min_turnaround_days == turnaround_days and min_turnaround_hours == turnaround_hours and min_turnaround_minutes <= turnaround_minutes)) and
                (turnaround_days < max_turnaround_days or
                 (turnaround_days == max_turnaround_days and turnaround_hours < max_turnaround_hours) or
                 (
                         turnaround_days == max_turnaround_days and turnaround_hours == max_turnaround_hours and turnaround_minutes <= max_turnaround_minutes))):
            results_list.append(line)

    return results_list


def filterData():
    with open("medicalRecord.txt", "r") as file:
        lines = file.readlines()

    with open("medicalTest.txt", "r") as file:
        lines1 = file.readlines()
    filtered_results = []

    print("Do you want to filter the medical records based one or two criteria? Enter 1 or 2")
    choice = input()
    if choice == "1":
        print("enter the criteria you want to filter the records based on :\n1-patient Id \n2-Test Name\n3-Abnormal "
              "tests\n4-Test added to the system within a specific period (start and end dates)\n5-Test status\n6-Test "
              "turnaround time within a period (minimum and maximum turnaround time)")
        criteria = input()
        if criteria == "1":
            print("enter the patient ID")
            patient_id = input()
            patient_id = validate_patient_id(patient_id)
            filtered_results = filtered_tests_basedOn_id_and_name_and_status(lines, patient_id)

        elif criteria == "2":
            print("enter the test name")
            test_name = input()
            test_name = check_test_existence(test_name)
            filtered_results = filtered_tests_basedOn_id_and_name_and_status(lines, test_name)

        elif criteria == "3":
            filtered_results = filter_tests_basedOn_range(lines)

        elif criteria == "4":
            print("enter the start date")
            start_date = input()
            start_date = validate_test_date(start_date)
            while True:
                print("Enter the end date (YYYY-MM-DD):")
                end_date = input()
                end_date = validate_test_date(end_date)
                end_date_parts = end_date.split('-')
                end_date_year = int(end_date_parts[0])
                end_date_month = int(end_date_parts[1])
                end_date_day = int(end_date_parts[2])

                start_date_parts = start_date.split('-')
                start_date_year = int(start_date_parts[0])
                start_date_month = int(start_date_parts[1])
                start_date_day = int(start_date_parts[2])

                if (end_date_year < start_date_year or
                        (end_date_year == start_date_year and end_date_month < start_date_month) or
                        (
                                end_date_year == start_date_year and end_date_month == start_date_month and end_date_day < start_date_day)):
                    print("The end date should be greater than the start date.")
                else:
                    break

            filtered_results = filtered_tests_basedOn_dates(lines, start_date, end_date)

        elif criteria == "5":
            print("enter the test status")
            test_status = input()
            test_status = validate_test_status(test_status)
            filtered_results = filtered_tests_basedOn_id_and_name_and_status(lines, test_status)

        elif criteria == "6":
            print("Enter the minimum turnaround time (format YYYY-MM-DD):")
            min_turnaround_time = input()
            min_turnaround_time = validate_turnaround_time(min_turnaround_time)
            min_turnaround_time1 = min_turnaround_time.split('-')
            min_turnaround_time_year = int(min_turnaround_time1[0])
            min_turnaround_time_month = int(min_turnaround_time1[1])
            min_turnaround_time_day = int(min_turnaround_time1[2])

            while True:
                print("Enter the maximum turnaround time (format YYYY-MM-DD):")
                max_turnaround_time = input()
                max_turnaround_time = validate_turnaround_time(max_turnaround_time)
                max_turnaround_time1 = max_turnaround_time.split('-')
                max_turnaround_time_year = int(max_turnaround_time1[0])
                max_turnaround_time_month = int(max_turnaround_time1[1])
                max_turnaround_time_day = int(max_turnaround_time1[2])

                if (max_turnaround_time_year < min_turnaround_time_year or
                        (
                                max_turnaround_time_year == min_turnaround_time_year and max_turnaround_time_month < min_turnaround_time_month) or
                        (
                                max_turnaround_time_year == min_turnaround_time_year and max_turnaround_time_month == min_turnaround_time_month and max_turnaround_time_day < min_turnaround_time_day)):
                    print("The maximum turnaround time should be greater than the minimum turnaround time.")
                else:
                    break

            filtered_results = filtered_tests_basedOn_turnaround_time(lines, min_turnaround_time,
                                                                      max_turnaround_time)

    if choice == "2":
        print("enter 2 criteria you want to filter the records based on :\n1-patient Id \n2-Test Name\n3-Abnormal "
              "tests\n4-Test added to the system within a specific period (start and end dates)\n5-Test status\n6-Test "
              "turnaround time within a period (minimum and maximum turnaround time)")
        print("enter the first criteria you want to filter the records based on :")
        criteria1 = input()
        print("enter the second criteria you want to filter the records based on :")
        criteria2 = input()
        if criteria1 == "1":
            print("enter the patient ID")
            patient_id = input()
            patient_id = validate_patient_id(patient_id)
            filtered_results = filtered_tests_basedOn_id_and_name_and_status(lines, patient_id)
        elif criteria1 == "2":
            print("enter the test name")
            test_name = input()
            test_name = check_test_existence(test_name)
            filtered_results = filtered_tests_basedOn_id_and_name_and_status(lines, test_name)
        elif criteria1 == "3":
            filtered_results = filter_tests_basedOn_range(lines)
        elif criteria1 == "4":
            print("enter the start date")
            start_date = input()
            start_date = validate_test_date(start_date)
            while True:
                print("Enter the end date (YYYY-MM-DD):")
                end_date = input()
                end_date = validate_test_date(end_date)
                end_date_parts = end_date.split('-')
                end_date_year = int(end_date_parts[0])
                end_date_month = int(end_date_parts[1])
                end_date_day = int(end_date_parts[2])

                start_date_parts = start_date.split('-')
                start_date_year = int(start_date_parts[0])
                start_date_month = int(start_date_parts[1])
                start_date_day = int(start_date_parts[2])

                if (end_date_year < start_date_year or
                        (end_date_year == start_date_year and end_date_month < start_date_month) or
                        (
                                end_date_year == start_date_year and end_date_month == start_date_month and end_date_day < start_date_day)):
                    print("The end date should be greater than the start date.")
                else:
                    break

            filtered_results = filtered_tests_basedOn_dates(lines, start_date, end_date)

        elif criteria1 == "5":
            print("enter the test status")
            test_status = input()
            test_status = validate_test_status(test_status)
            filtered_results = filtered_tests_basedOn_id_and_name_and_status(lines, test_status)

        elif criteria1 == "6":
            print("Enter the minimum turnaround time (format YYYY-MM-DD):")
            min_turnaround_time = input()
            min_turnaround_time = validate_turnaround_time(min_turnaround_time)
            min_turnaround_time1 = min_turnaround_time.split('-')
            min_turnaround_time_year = int(min_turnaround_time1[0])
            min_turnaround_time_month = int(min_turnaround_time1[1])
            min_turnaround_time_day = int(min_turnaround_time1[2])

            while True:
                print("Enter the maximum turnaround time (format YYYY-MM-DD):")
                max_turnaround_time = input()
                max_turnaround_time = validate_turnaround_time(max_turnaround_time)
                max_turnaround_time1 = max_turnaround_time.split('-')
                max_turnaround_time_year = int(max_turnaround_time1[0])
                max_turnaround_time_month = int(max_turnaround_time1[1])
                max_turnaround_time_day = int(max_turnaround_time1[2])

                if (max_turnaround_time_year < min_turnaround_time_year or
                        (
                                max_turnaround_time_year == min_turnaround_time_year and max_turnaround_time_month < min_turnaround_time_month) or
                        (
                                max_turnaround_time_year == min_turnaround_time_year and max_turnaround_time_month == min_turnaround_time_month and max_turnaround_time_day < min_turnaround_time_day)):
                    print("The maximum turnaround time should be greater than the minimum turnaround time.")
                else:
                    break

            filtered_results = filtered_tests_basedOn_turnaround_time(lines, min_turnaround_time,
                                                                      max_turnaround_time)

        if criteria2 == "1":
            print("enter the patient ID")
            patient_id = input()
            patient_id = validate_patient_id(patient_id)
            filtered_results = filtered_tests_basedOn_id_and_name_and_status(filtered_results, patient_id)


        elif criteria2 == "2":
            print("enter the test name")
            test_name = input()
            test_name = check_test_existence(test_name)
            filtered_results = filtered_tests_basedOn_id_and_name_and_status(filtered_results, test_name)

        elif criteria2 == "3":
            filtered_results = filter_tests_basedOn_range(filtered_results)

        elif criteria2 == "4":
            print("enter the start date")
            start_date = input()
            start_date = validate_test_date(start_date)
            while True:
                print("Enter the end date (YYYY-MM-DD):")
                end_date = input()
                end_date = validate_test_date(end_date)
                end_date_parts = end_date.split('-')
                end_date_year = int(end_date_parts[0])
                end_date_month = int(end_date_parts[1])
                end_date_day = int(end_date_parts[2])

                start_date_parts = start_date.split('-')
                start_date_year = int(start_date_parts[0])
                start_date_month = int(start_date_parts[1])
                start_date_day = int(start_date_parts[2])

                if (end_date_year < start_date_year or
                        (end_date_year == start_date_year and end_date_month < start_date_month) or
                        (
                                end_date_year == start_date_year and end_date_month == start_date_month and end_date_day < start_date_day)):
                    print("The end date should be greater than the start date.")
                else:
                    break

            filtered_results = filtered_tests_basedOn_dates(filtered_results, start_date, end_date)

        elif criteria2 == "5":
            print("enter the test status")
            test_status = input()
            test_status = validate_test_status(test_status)
            filtered_results = filtered_tests_basedOn_id_and_name_and_status(filtered_results, test_status)

        elif criteria2 == "6":
            print("Enter the minimum turnaround time (format YYYY-MM-DD):")
            min_turnaround_time = input()
            min_turnaround_time = validate_turnaround_time(min_turnaround_time)
            min_turnaround_time1 = min_turnaround_time.split('-')
            min_turnaround_time_year = int(min_turnaround_time1[0])
            min_turnaround_time_month = int(min_turnaround_time1[1])
            min_turnaround_time_day = int(min_turnaround_time1[2])

            while True:
                print("Enter the maximum turnaround time (format YYYY-MM-DD):")
                max_turnaround_time = input()
                max_turnaround_time = validate_turnaround_time(max_turnaround_time)
                max_turnaround_time1 = max_turnaround_time.split('-')
                max_turnaround_time_year = int(max_turnaround_time1[0])
                max_turnaround_time_month = int(max_turnaround_time1[1])
                max_turnaround_time_day = int(max_turnaround_time1[2])

                if (max_turnaround_time_year < min_turnaround_time_year or
                        (
                                max_turnaround_time_year == min_turnaround_time_year and max_turnaround_time_month < min_turnaround_time_month) or
                        (
                                max_turnaround_time_year == min_turnaround_time_year and max_turnaround_time_month == min_turnaround_time_month and max_turnaround_time_day < min_turnaround_time_day)):
                    print("The maximum turnaround time should be greater than the minimum turnaround time.")
                else:
                    break

            filtered_results = filtered_tests_basedOn_turnaround_time(filtered_results, min_turnaround_time,
                                                                      max_turnaround_time)

    return filtered_results


def generate_report(filtered_data):
    minimum_test_value = float('inf')
    maximum_test_value = float('-inf')
    total_test_value = 0
    completed_test_count = 0

    minimum_turnaround_time = float('inf')
    maximum_turnaround_time = float('-inf')
    total_turnaround_time = 0

    for test in filtered_data:
        testInfo = test.split(':', 1)[1].split(',')
        testName = testInfo[0].strip()
        patient_test_result = float(testInfo[2].strip())
        maximum_test_value = max(maximum_test_value, patient_test_result)
        minimum_test_value = min(minimum_test_value, patient_test_result)
        total_test_value += patient_test_result
        completed_test_count += 1

        # Find the turnaround time for the current test
        with open("medicalTest.txt", "r") as file:
            for line1 in file:
                if testName.lower() in line1.lower():
                    turnaround_time = line1.split(',')[-1].strip()
                    break  # Exit loop once the relevant turnaround time is found

        turnaround_days = int(turnaround_time.split('-')[0])
        turnaround_hours = int(turnaround_time.split('-')[1])
        turnaround_minutes = int(turnaround_time.split('-')[2])

        # Convert turnaround time to total minutes for easier comparison
        total_minutes = turnaround_days * 24 * 60 + turnaround_hours * 60 + turnaround_minutes
        minimum_turnaround_time = min(minimum_turnaround_time, total_minutes)
        maximum_turnaround_time = max(maximum_turnaround_time, total_minutes)
        total_turnaround_time += total_minutes

    avg_test_value = total_test_value / completed_test_count
    avg_turnaround_time = total_turnaround_time / completed_test_count / 60  # Convert to hours

    print(f"Minimum Test Value: {minimum_test_value}")
    print(f"Maximum Test Value: {maximum_test_value}")
    print(f"Average Test Value: {avg_test_value:.2f}")

    min_days = minimum_turnaround_time // (24 * 60)
    min_hours = (minimum_turnaround_time % (24 * 60)) // 60
    min_minutes = minimum_turnaround_time % 60
    print(f"Minimum Turnaround Time: {min_days} days {min_hours} hours {min_minutes} minutes")

    max_days = maximum_turnaround_time // (24 * 60)
    max_hours = (maximum_turnaround_time % (24 * 60)) // 60
    max_minutes = maximum_turnaround_time % 60
    print(f"Maximum Turnaround Time: {max_days} days {max_hours} hours {max_minutes} minutes")

    avg_days = avg_turnaround_time // 24
    avg_hours = avg_turnaround_time % 24
    avg_minutes = (avg_turnaround_time * 60) % 60
    print(f"Average Turnaround Time: {avg_days:.0f} days {avg_hours:.0f} hours {avg_minutes:.0f} minutes")




def export_records_to_csv(data):
    filename = "medical_records.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Define the headers for the CSV file
        fieldnames = ['patient Id', 'test_name', 'test_date', 'test_time', 'test_result', 'test_unit', 'test_status',
                      'result_date', 'result_time']

        # Write the header row
        writer.writerow(fieldnames)

        for record in data:
            # Assuming 'record' contains 'patient Id' at the start, which isn't shown in the provided code snippet.
            # You might need to split the record further if 'patient Id' is part of the same line as testInfo.
            patient_id, test_details = record.split(':', 1)
            patient_id = patient_id.strip()

            testInfo = test_details.split(',')
            test_name = testInfo[0].strip()
            test_date_time = testInfo[1].strip().split(' ')
            test_date = test_date_time[0].strip()
            test_time = test_date_time[1].strip()
            test_result = testInfo[2].strip()
            test_unit = testInfo[3].strip()
            test_status = testInfo[4].strip()

            result_date = ''
            result_time = ''
            if test_status == 'completed':
                result_date_time = testInfo[5].strip().split(' ')
                result_date = result_date_time[0].strip()
                result_time = result_date_time[1].strip()

            # Write the data row
            writer.writerow(
                [patient_id, test_name, test_date, test_time, test_result, test_unit, test_status, result_date,
                 result_time])

    print(f"Records have been successfully exported to {filename}")


def import_records_from_csv():
    # Specify the filename for the CSV file
    filename = "medical_records.csv"

    imported_data = []

    # Open the file in read mode
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)

            # Skip the header row (if there is one)
            next(reader, None)

            # Read each row from the CSV file and add it to the list
            for row in reader:
                imported_data.append(row)

        print(f"Records have been successfully imported from {filename}")
        return imported_data

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []


def menu():
    filtered_data = []  # List to store filtered data
    data_filtered = False  # Flag to track if data has been filtered

    while True:
        print("\nMedical Test Management System")
        print("1. Add a new medical test")
        print("2. Add a new medical test record")
        print("3. Update patient records")
        print("4. Update medical tests")
        print("5. Filter medical tests")
        print("6. Generate textual summary reports")
        print("7. Export medical records to CSV")
        print("8. Import medical records from CSV")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            add_medical_tests()
        elif choice == "2":
            add_medical_record()
        elif choice == "3":
            update_test_record()
        elif choice == "4":
            update_medicalTest()
        elif choice == "5":
            filtered_data = filterData()
            if len(filtered_data):
                for test in filtered_data:
                    print(test.strip())
            data_filtered = True  # Set flag to True after filtering
        elif choice == "6":
            if data_filtered:
                generate_report(filtered_data)

            else:
                print("You must filter the data first (option 5) before generating a report.")
        elif choice == "7":
            with open("medicalRecord.txt", "r") as file:
                lines = file.readlines()
                export_records_to_csv(lines)

        elif choice == "8":
            temp = import_records_from_csv()
            if (len(temp)):
                for record in temp:
                    print(record)

        elif choice == "9":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    menu()
