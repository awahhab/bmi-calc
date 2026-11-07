# BMI Calculator

A lightweight Python project that calculates a person’s Body Mass Index (BMI) from their weight and height, then classifies the result into standard health categories.

## ✨ Features

- Calculates BMI using the standard formula
- Validates user input for numbers and positive values
- Displays a BMI category based on the result
- Easy to run from the terminal
- Minimal, beginner-friendly Python project

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

- Python 3.x installed on your system
- A terminal or command prompt

### Run the project

1. Open your terminal in the project directory.
2. Run:

```bash
python app.py
```

If you are using a virtual environment:

```bash
.venv\Scripts\Activate.ps1
python app.py
```

## 🧪 Example

```text
Enter your weight in kilograms: 70
Enter your height in meters: 1.75
Your BMI is:  22.86
You have a normal weight.
```

## 📁 Project Structure

```text
bmi-calc/
├── app.py
├── README.md
└── .venv/
```

## 🛠️ How It Works

The script:

- asks for weight in kilograms
- asks for height in meters
- converts the values to floats
- checks that the values are valid and greater than zero
- calculates the BMI
- prints the result and the corresponding category

## 🤝 Contributing

This project is simple and beginner-friendly. Feel free to improve it by adding:

- a better user interface
- input validation improvements
- a GUI version
- BMI history tracking

## 📜 License

This project is open for personal and educational use.

---

Built with Python to make health tracking simple and accessible.
