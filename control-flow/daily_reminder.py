#!/usr/bin/env python3

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        label = "high"
    case "medium":
        label = "medium"
    case "low":
        label = "low"
    case _:
        label = priority

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {label} priority task that requires immediate attention today!")
else:
    print(f"Note: '{task}' is a {label} priority task. Consider completing it when you have free time.")


