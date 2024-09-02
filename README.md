# Cognitive-Disorder-Detection

## Overview

**Cognitive-Disorder-Detection** is a Python 3.10 project designed to detect the likelihood of a cognitive disorder in patients based on their drawings. The project utilizes a machine learning model, specifically a Support Vector Machine (SVM), which has been trained on image data to achieve a precision of 73%. The primary focus is on detecting cognitive impairment, such as Mild Cognitive Impairment (MCI) or other neurodegenerative disorders, using drawings analyzed through the MoCA (Montreal Cognitive Assessment) scoring system.

## MoCA Scores

The **Montreal Cognitive Assessment (MoCA)** is a widely used cognitive screening test designed to assist in the detection of mild cognitive impairment. The MoCA test assesses several cognitive domains, including memory, attention, language, visuospatial skills, and executive function. A score of 26 or higher is generally considered normal, while lower scores may indicate cognitive impairment.

In this project, the MoCA scores are inferred based on patients' drawings, such as clock drawings, which are evaluated by the trained SVM model.

## Dataset

The images used for training and testing the model in this project are obtained from the following repository:

[https://github.com/cccnlab/MCI-multiple-drawings/tree/main](https://github.com/cccnlab/MCI-multiple-drawings/tree/main)

This dataset includes multiple drawings that have been used to assess cognitive impairment in patients.

## Requirements

To run this project, you will need:

- Python 3.* or later (recommended 3.10)
- pip (Python package installer)

## Setup

1. Clone the repository and navigate to the project directory.
2. Ensure you have Python 3.* or later and pip installed on your system.
3. Run the setup script to prepare the environment:

   ```bash
   ./scripts/setup.sh
   ```
4. After setting up the environment, start the application by running:

   ```bash
   ./scripts/start.sh
   ```

## How It Works

- The project creates a virtual environment, installs the required dependencies, and sets up the necessary directories for saving the trained model and scaler.
- The SVM model is trained on the provided dataset and saved for later use.
- The main application includes a simple user interface (UI) that allows users to upload drawings and receive a prediction on whether the patient may have a cognitive disorder, based on the MoCA scoring criteria.
