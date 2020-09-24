# Bash.md

## Shebangs
```bash#!/usr/bin/bash
#!/usr/bin/env zsh
#!/usr/bin/python
#!/usr/bin/python3
```

## Activate Python Virtualenv
```bash
call C:/Users/dwilliams/projects/sxp/venv/scripts/activate.bat
cd C:/Users/dwilliams/projects/sxp
python run.py
```

## Desktop Launcher
```bash
[Desktop Entry]
Type=Application
Name=Arduino IDE
GenericName=Arduino IDE
Comment=Open-source electronics prototyping platform
Exec=/home/development/arduino-1.8.8/arduino
Icon=arduino-arduinoide
Terminal=false
Categories=Development;IDE;Electronics;
MimeType=text/x-arduino;
Keywords=embedded electronics;electronics;avr;microcontroller;
StartupWMClass=processing-app-Base
```

## Window Batch File

### Pass In Variable

```bash
@echo off
set var1=%1
echo "%var1%"
```

## Scripting

### Example

```bash
#!/usr/bin/env bash
NAME="John"
echo "Hello $NAME!"
```

### Variables
```bash
NAME="John"
echo $NAME
echo "$NAME"
echo "${NAME}"
```

### String Quotes
```bash
NAME="John"
echo "Hi $NAME" #=> Hi John
echo 'Hi $NAME' #=> Hi $Name
```

### Conditional Execution
```bash
git commit &&  git push
git commit || echo "Commit failed"
```

### Functions
```bash
get_name() {
    echo "John"
}

echo "You are $(get_name)"
```