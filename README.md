
# 🎃 PP3

PP3 is a turn-based role-playing game where players take on the role of characters with unique abilities. Characters can range from skilled gunslingers to powerful hell knights. The gameplay revolves around a move-set system with three types of moves:

- Damaging Moves
- Healing Moves
- Stat Boost Moves

Players strategically use their character's moves to gain an advantage over their opponents. While the game is still in early development, it promises an engaging and dynamic experience for fans of turn-based RPGs.

~~If you would like to leave a suggestion join our [Official PP3 Discord Server]()~~

## 🛠️ Building

To build this project into an executable, you will need to have Python and [PyInstaller](https://pypi.org/project/pyinstaller/) installed on your machine.
> It is recommended to use a virtual environment to avoid conflicts with other Python packages.

1. Install PyInstaller using pip:

```bash
pip install pyinstaller
```

1. Navigate to the repo's root directory
2. Run PyInstaller to build the application from the `main.spec`file:

```bash
pyinstaller main.spec
```

After running this command, PyInstaller will create a `dist` directory in the current directory. Inside `dist`, you will find your standalone executable file named `main.exe` (or just main on Unix-based systems).

> [!NOTE] This game probably won't receive any more updates as of now 😔
