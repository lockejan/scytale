# Scytale

## Description

The scytale was used more than 2500 years ago by the Spartans, and is one example of ancient cryptography.
A message gets written on a ribbon which is then wrapped around a stick with a certain diameter (the scytale).

Below is a sample encryption of the plaintext "prove me wrong!" with a scytale of diameter 3.

We write the messagearound the scytale, and then

```
|p|r|o|
 - - -
|v|e| |
 - - -
|m|e| |
 - - -
|w|r|o|
 - - -
|n|g|!|
```

The ciphertext is obtained by reading from top to bottom, left to right.
In this example, the ciphertext is

```
pvmwnreergo  o!
```

## Usage

- `pipenv install` (installs the virtual environment and all given requirements)
- `pipenv shell` (activates and enters the virtual environment)
- `python test_scytale.py` (runs all tests)
- `python scytale.py` (runs the implemented interactive scytale wizard)

![Wizard](scytale-wizard.png)
