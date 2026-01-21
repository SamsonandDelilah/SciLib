## SciLib - Precision Angle Conversion Library

**Unified single Source-of-Truth (SOT) conversion for ALL input formats with automatic validation!**

## 🚀 Motivation ##

**Problem:** Every library handles angle systems differently:

numpy.deg2rad("180°20'")     → Error
math.radians("180.57degree")   → Error  
scipy.invalid_input("2g")    → Error


**SciLib solves it:** **1 API → all formats** with precision checking!

## 📦 Installation

```Powershel or bash
pip install git+https://github.com/SamsonandDelilah/SciLab.git#subdirectory=python
```

## 💻 Usage ##

```python
from scilib import DegreeToRadians, RadiansToDegree

# Safe usage with validation
result = DegreeToRadians("N 180°")                # will generate error, displays the error
if result is not None:                            # and provides a 'None' value
    s = result * 34
else:
    print("Calculation cannot be performed.")

# Broad format spectrum
print("\nDegrees → Radians:")
print(DegreeToRadians(180.57))                    # Decimal degrees example
print(DegreeToRadians("180.57"))                  # Decimal degrees example
print(DegreeToRadians("180°"))                    # DMS
print(DegreeToRadians("180°40'13''"))             # DMS example
print(DegreeToRadians("180°68'10''"))             # incorrect DMS example
print(DegreeToRadians(2.3456e1))                  # Scientific notation example
print(DegreeToRadians("2.3456e1"))                # Scientific notation example
print(DegreeToRadians(mpfr("181.57")))            # mpfr decimal degrees example
print(DegreeToRadians(mpfr("N 181.57")))          # incorrect mpfr decimal degrees example
print(DegreeToRadians(mpfr("1.89°")))             # incorrect mpfr decimal degrees example

print("\nRadians → Degrees:")
print(RadiansToDegree(3.14))  
print(RadiansToDegree("3.14"))  
print(RadiansToDegree(np.pi))                     # π → 180° (mpfr)
print(RadiansToDegree(mpfr('3.14159535', 128)))   # High precision
print(RadiansToDegree("1.234e1"))                 # Scientific → Degrees
print(RadiansToDegree("0.40938442"))              # DMS → Degrees (direct)
```

## 🎯 Supported Formats

| Type | Examples |
|------|----------|
| Decimal degree | `180.57` |
| DMS | `"180°20'13''"`  |
| Scientific | `"1.234e2"` |
| High-Precision | `mpfr("3.14159", 256)` |

Supported types are integer, float, decimal and BigFloat (with mfpr string format).

## 🛠 Roadmap

```
SciLab (Monorepo)
├── python/     → pip install scilib
├── rust/       → cargo add scilib
└── cpp/        → #include <scilib-cpp>
```

It ist indented to expand this SciLib continously (fully supporting a simple SOT approach only), help is welcome - I am a beginner.

## 🤝 Feedback Welcome!

I would love to hear from you, what you think about or how I can help or how you possible would like to help me.

https://github.com/SamsonandDelilah/SciLab/issues

**For 3D Graphics, Physics, Astronomy and more!** ⭐

