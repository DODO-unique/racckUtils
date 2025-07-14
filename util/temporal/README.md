# 🕰️ Imperium Time Format

A Python utility for converting between standard UNIX epoch time and a custom format called **Imperium**—a six-digit compressed datetime system with built-in validation, leap year support, and some wild walrus operator magic.

Built for projects that need compact, readable, version-stable timestamps in logs or IDs.

---

## 📦 Features

- 🔁 **epoch_to_imperium(seconds)**: Converts a UNIX epoch to Imperium format  
  - Example: `1982729107` → `240527_194147` (`yyMMdd_HHmmss`)
- 🔁 **imperium_to_epoch(imperium)**: Converts an Imperium string back to epoch  
  - Example: `240527_194147` → `1982729107`
- 🧠 Leap year handling (Gregorian accurate)
- 🧹 Internal validation (invalid month/day catches)
- 🦘 Walrus operator used for in-line reverse slicing

---

## 🧠 What is Imperium Format?

A compressed datetime structure derived from:

```
yyMMdd\_HHmmss
││││││ └── seconds
│││││└──── minutes
││││└───── hours
│││└────── day
││└─────── month
│└──────── year (from 1970)

```

**Example:**  
Epoch: `1982729107`  
→ Imperium: `240527_194147`  
→ Meaning: 2024, May 27, 19:41:47

---

## 📘 Usage

```python
r = Routine()

r.epoch_to_imperium(1982729107)
# '240527_194147'

r.imperium_to_epoch(240527194147)
# 1982729107

r.epoch_to_imperium(0, detailed=True)
# {
#   'yy': 0, 'm': 1, 'd': 1, 'h': 0, 'min': 0, 'sec': 0,
#   'ir': '000101_000000'
# }
```

---

## 🔥 Internals (Short Summary)

### `Maths.isLeap(year)`

Classic leap year checker.

### `Routine.epoch_to_imperium(seconds)`

* Iteratively reduces `seconds` to year, month, day, hour, minute, second
* Returns formatted string or a dict if `detailed=True`

### `Routine.imperium_to_epoch(imperium)`

* Uses a dictionary comprehension + walrus to unpack digits
* Validates date range before summing epoch time

---

## ⚠️ Notes

* Currently supports years **1970–9999**
* Out-of-bounds or malformed input will return descriptive errors
* `Routine.day()` not implemented (reserved for future extension like weekday extraction)

---

## 🧪 Built For

* Log timestamping in projects like **DimeSim**
* Filename-safe datetime IDs
* Future calendar utilities (like the *Centurian* or *Chronicle* modules)

---

## 🐾 Author Note

Built during an irrationally determined session where I decided Unix time wasn’t weird enough.

MIT licensed.
Built by a raccoon, for raccoons.
