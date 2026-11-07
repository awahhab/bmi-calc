# BMI Calculator

A lightweight Python project that calculates a person’s Body Mass Index (BMI) from their weight and height, then classifies the result into standard health categories.

## ✨ Features

- Calculates BMI using the standard formula
- Validates user input for valid numeric values and positive numbers
- Classifies BMI into standard health categories
- Includes a clean CLI entry point for interactive use
- Includes automated tests for core BMI behavior
- Beginner-friendly and easy to extend

## 📐 BMI Formula

BMI is calculated as:

$$
BMI = \frac{weight\_kg}{height\_m^2}
$$

## 🏷️ BMI Categories

| BMI Range | Category |
| --- | --- |
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal weight |
| 25.0 - 29.9 | Overweight |
| 30.0 and above | Obesity |

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- A terminal or command prompt

### 1) Create a virtual environment

```bash
python -m venv .venv
```

### 2) Activate it

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run the project

```bash
python app.py
```

## 🧪 Running Tests

This project includes automated tests for the BMI logic.

```bash
pytest -q
```

## 📁 Project Structure

```text
bmi-calc/
├── app.py
├── tests/
│   └── test_app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .venv/
```

## 🛠️ How It Works

The script:

- asks for weight in kilograms
- asks for height in meters
- converts values to floats
- rejects invalid or non-positive input
- calculates BMI using the formula
- prints the BMI and its category

The app logic is separated from the CLI entry point so it can be imported and tested cleanly.

## 🧪 Example

```text
Enter your weight in kilograms: 70
Enter your height in meters: 1.75
Your BMI is: 22.86
You have a normal weight.
```

## 🤝 Contributing

This project is simple and beginner-friendly. You can extend it by adding:

- a better user interface
- improved validation messages
- GUI support
- BMI history tracking
- unit tests for extra edge cases

## 📜 License

This project is open for personal and educational use.

---

Built with Python to make health tracking simple and accessible.
