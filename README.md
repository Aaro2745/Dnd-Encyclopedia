# 🐉 D&D Encyclopedia

A Python-based Dungeons & Dragons encyclopedia that lets users look up information about monsters, spells, classes, races, items, and backgrounds using the D&D 5e API.

## 📖 About

The D&D Encyclopedia is a personal programming project designed to make looking up D&D information easier through a simple, menu-driven interface.

The project uses Python to interact with the D&D 5e API and retrieve information based on the category and name selected by the user.

This is an ongoing project that will grow as I develop my Python skills and add new features.

## ✨ Features

- **Category Selection:** Choose from six categories:
  - Monsters
  - Spells
  - Classes
  - Races
  - Items
  - Backgrounds
- **Name-Based Lookups:** Enter the name of an entry to search for it.
- **API Integration:** Uses the D&D 5e API to request information.
- **Input Validation:** Prompts users again when they select an invalid category.

## 🛠️ Built With

- [Python](https://www.python.org/) — Main programming language.
- [Requests](https://requests.readthedocs.io/) — Sends HTTP requests to the API.
- [D&D 5e API](https://www.dnd5eapi.co/) — Provides D&D game data.
- [GitHub](https://github.com/) — Source control and project hosting.

## 🚀 Getting Started

### Prerequisites

- Python 3
- An internet connection
- The `requests` library

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aaro2745/Dnd-Encyclopedia.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Dnd-Encyclopedia
   ```

3. Install the required dependency:

   ```bash
   python -m pip install requests
   ```

### Running the Program

Run the following command from the project directory:

```bash
python Dnddict.py
```

Depending on your system, you may need to use `python3` instead of `python`.

## 🗺️ Roadmap

- [x] Create a category selection menu.
- [x] Connect to the D&D 5e API.
- [x] Accept entry names from the user.
- [ ] Display the retrieved information in a readable format.
- [ ] Handle entries that cannot be found.
- [ ] Improve input validation and error handling.
- [ ] Add more features as development continues.

## 🎯 Goals

- Build a useful D&D reference tool.
- Improve my Python programming skills.
- Learn more about APIs and HTTP requests.
- Practice writing readable, maintainable code.
- Expand the project over time.

## ⚖️ Disclaimer

Dungeons & Dragons is a trademark of Wizards of the Coast LLC. This project is an unofficial fan-made project and is not affiliated with, endorsed, or sponsored by Wizards of the Coast.

D&D data is retrieved from the [D&D 5e API](https://www.dnd5eapi.co/). Refer to the API's documentation and applicable content licenses for more information.

## 📜 License

No license has been specified yet. Please check this repository for licensing information before reusing or distributing its code.

