```markdown
# SciLib - Precision Angle Conversion Library

**Einheitliche SOT-Konvertierung für alle Eingabeformate mit automatischer Validierung!**

## 🚀 Motivation

**Problem:** Jede Bibliothek behandelt Winkelsysteme anders:
```
numpy.deg2rad("180°20'")     → Error
math.radians("180.57grad")   → Error  
scipy.invalid_input("2g")    → Error
```

**SciLib:** 1 API → alle Formate mit Präzisionsprüfung!

## 📦 Installation

```bash
pip install git+https://github.com/SamsonandDelilah/SciLab.git#subdirectory=python
```

## 💻 Verwendung

```python
from scilib import GradToRadians, RadiansToGrad

# Sichere Verwendung mit Validierung
result = GradToRadians("180")
if result is not None:
    s = result * 34
else:
    print("Berechnung kann nicht durchgeführt werden.")

# Breites Format-Spektrum
print(GradToRadians(180.57))                    # Dezimalgrad
print(GradToRadians("180°20'13''"))             # DMS
print(GradToRadians("2.3456e1"))                # Wissenschaftlich
print(GradToRadians(mpfr("180.57")))           # High-Precision

print("\nRadians → Grad:")
print(RadiansToGrad(np.pi))                     # π → 180°
print(RadiansToGrad(mpfr('3.1415926535', 128))) # 128-bit
print(RadiansToGrad("1.234e1"))                 # Wissenschaftlich
```

## 🎯 Unterstützte Formate

| Typ | Beispiele |
|-----|-----------|
| Dezimal | `180.57`, `"180.57grad"` |
| DMS | `"180°20'13''"`, `"N 48°12'30''"` |
| Wissenschaftlich | `"1.234e2"`, `"2.3456E1grad"` |
| High-Precision | `mpfr("3.14159", 256)` |

## 🛠 Roadmap

```
SciLab (Monorepo)
├── python/     → pip install scilib
├── rust/       → cargo add scilib
└── cpp/        → #include <scilib-cpp>
```

## 🤝 Feedback

https://github.com/SamsonandDelilah/SciLab/issues

**Für 3D Graphics, Physik, Astronomie!** ⭐
```

**Speichern:**
```powershell
cd I:\Git\scilib
notepad README.md
# Inhalt kopieren
git add README.md
git commit -m "Add README.md"
git push
```