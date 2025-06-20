# Build Your Own Database (Key-Value Store)

This project implements a lightweight, JSON-backed database using a Python class. It mimics the structure of systems like Redis or early document stores and demonstrates the logic behind Create/Read/Update/Delete operations and persistent storage.

---

## What It Does

- Stores records as a dictionary in memory
- Persists to a `.json` file on disk
- Includes basic methods:
  - `create(key, value)`
  - `read(key)`
  - `update(key, value)`
  - `delete(key)`
- Loads automatically on startup

---

## Healthcare System Context

**Digital Twin Example:**  
Running a brain perfusion simulation and want to log:

```json
{
  "brain_R1": {"perfusion": 45, "oxygen": 88, "risk_score": 0.35},
  "brain_R2": {"perfusion": 22, "oxygen": 74, "risk_score": 0.92}
}
```

This mini-DB helps you:
- Store real-time simulation outputs
- Track ML model predictions
- Prototype EHR logic without relying on external databases

---

## How to Use

```bash
cd src/
python main.py
```

Can run and test operations like:
- Create two records
- Read/update/delete them
- View stored values in `data.json`

---

## File Structure

- `src/main.py`: Database logic and sample usage
- `data.json`: Auto-created file that stores all records
- `assets/`: Optional architecture diagrams or flowcharts
- `NOTES.md`: Your implementation journal

---

## Author

**Ihunna Amugo**  
DDS Candidate | MHA | MS | REHS | PhD(c) Computational Engineering  
GitHub: [@ihunnamatata](https://github.com/ihunnamatata)
