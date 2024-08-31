# Medicine Management Application

## Overview

A Tkinter-based medicine management app with Firebase Firestore integration. Features include adding medicines, viewing details, logging intake, and restocking. Designed for easy tracking of medication usage and management.

## Features

- **Add Medicine**: Enter details about new medicines including name, frequency, food relation, and number of strips remaining.
- **View Medicines**: Display all medicines with their remaining tablets. Click on a medicine to see detailed information.
- **Log Medicine Intake**: Reduce remaining tablets by one and get notified if the medicine is running low.
- **Restock Medicines**: Add new strips to restock medicines and update tablet counts.

## Technologies Used

- **Python**: Programming language for the application.
- **Tkinter**: GUI library for the interface.
- **Firebase Firestore**: Cloud database for storing medicine data.

## Directory Structure

Medicine_Monitoring_App/
│
├── main.py                # Entry point of the application
├── firebase_config.py     # Firebase initialization
├── add_medicine.py        # Functionality to add new medicines
├── view_medicine.py       # Functionality to view medicine details
├── log_intake.py          # Functionality to log medicine intake
└── restock_medicine.py    # Functionality to restock medicines
