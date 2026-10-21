"""
Project Title: eCRF Data Validator
Name: Antonio José Bailén de la Cruz
GitHub Username: abaicru
edX Username: abaicru
City, Country: Córdoba, Spain
Date: October 21, 2026
"""

import csv
import sys

def main():
    # 1. Verificamos que el usuario introduzca el CSV al ejecutar el programa
    if len(sys.argv) != 2:
        sys.exit("Usage: python project.py patients.csv")

    filename = sys.argv[1]
    errors_found = []

    # 2. Abrimos el archivo CSV
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Analizamos paciente a paciente
            for row in reader:
                patient_id = row["patient_id"]

                # Pasamos los datos por tus 3 funciones
                if not check_status(row["status"]):
                    errors_found.append(f"Query in Patient {patient_id}: Invalid Status -> {row['status']}")

                if not check_age(row["age"]):
                    errors_found.append(f"Query in Patient {patient_id}: Invalid Age -> {row['age']}")

                if not check_heart_rate(row["heart_rate"]):
                    errors_found.append(f"Query in Patient {patient_id}: Invalid Heart Rate -> {row['heart_rate']}")

    except FileNotFoundError:
        sys.exit("Error: File not found")

    # 3. Imprimimos el reporte final de validación
    print("--- eCRF VALIDATION REPORT ---")
    if not errors_found:
        print("All data is perfectly clean!")
    else:
        for error in errors_found:
            print(error)


def check_status(status):
    """Devuelve True solo si el estado es exactamente Alive o Dead."""
    if status in ["Alive", "Dead"]:
        return True
    return False


def check_age(age):
    """Devuelve True si la edad es un número entre 0 y 120."""
    try:
        age_int = int(age)
        if 0 <= age_int <= 120:
            return True
        return False
    except ValueError:
        return False


def check_heart_rate(hr):
    """Devuelve True si el pulso es un número entre 30 y 250."""
    try:
        hr_int = int(hr)
        if 30 <= hr_int <= 250:
            return True
        return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
