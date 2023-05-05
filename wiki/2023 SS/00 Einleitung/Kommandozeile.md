# Kommandozeile
Die Kommandozeile ist Bestandteil jedes Betriebssystems. Unter Windows heißt das Programm für die Kommandozeile "*Eingabeaufforderung*".

Beim Öffnen der Eingabeaufforderung wird das aktuelle Verzeichnis (`C:\Users\benutzername`) angezeigt.

```powershell
Microsoft Windows [Version 10.0.19045.2846]
(c) Microsoft Corporation. Alle Rechte vorbehalten.

C:\Users\benutzername>
```

## Befehle

In der Kommandozeile können Befehle ausgeführt werden. Zum Beispiel lässt sich mit dem Befehl `python` der Python Interpreter starten.

```powershell
# EINGABE
C:\Users\benutzername> python

# AUSFÜHRUNG DES BEFEHLS "python"
Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print "Hello"
Hello
```

### Befehle abbrechen
Nachdem ein Befehl über die Kommandozeile gestartet wurde, kann er jederzeit abgebrochen werden. Um den gestarteten Python Interpreter wieder zu verlassen, kann die Tastenkombination **`Ctrl C`** verwendet werden.


## Befehle mit Argumenten ausführen
Beim Ausführen eines Befehls können Argumente/Parameter angegeben werden.

Ein weit verbreiteter Parameter, der von vielen Befehlen akzeptiert wird, ist `--help`. Mit ihm können meistens alle möglichen Kommandozeilenparameter eines Befehls ausgegeben werden.

```yaml
# EINGABE MIT ARGUMENT/PARAMETER
C:\Users\benutzername> python --help

# AUSFÜHRUNG DES BEFEHLS "python --help"
usage: C:\...\bin\python.exe [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables)
-b     : issue warnings about comparing bytearray with unicode
         (-bb issue errors)

      ...

-u     : unbuffered binary stdout and stderr; also PYTHONUNBUFFERED=x
         see man page for details on internal buffering relating to '-u'
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
```

Hier wird zum Beispiel das Argument `-V` genannt, um die Python-Version auszugeben.

```yaml
# EINGABE MIT ARGUMENT/PARAMETER
C:\Users\benutzername> python -V

# AUSFÜHRUNG DES BEFEHLS "python -V"
Python 2.7.18
```

In komplexeren Programmen werden teilweise *viele verschiedene Argumente* in einen einzelnen Befehlsaufruf geschrieben. Mit dem Programm [`ffmpeg`](https://ffmpeg.org/ffmpeg.html#Description) kann zum Beispiel durch den folgenden Befehl das Format einer Videodatei von AVI zu MP4 mit einer Auflösung von 1920x1080 Pixeln konvertiert werden:

```bash
ffmpeg -i input.avi -s 1920x1080 output.mp4
```

In dem Beispiel gibt es 5 Argumente: `-i`, `input.avi`, `-s`, `1920x1080` und `output.mp4`.

Argumente, die auf diese Weise angegeben werden, können vom jeweiligen Befehl/Programm (in dem Fall `ffmpeg` oder `python`) gelesen und interpretiert werden.

## Argumente in eigenen Programmen

Auch selbst geschriebene Programme in Java, C, Python usw. können Argumente auf eigene Weise verarbeiten. Meistens wird direkt in der statischen `main()`-Methode ein Array an Strings überliefert, der die Befehls-Argumente enthält.

```java
// Dateiname: "MainClass.java"
public class MainClass {  
  
    public static void main(String[] arguments) {  
        System.out.println("Es gibt " + arguments.length + " Argumente");  
  
        // Hier werden alle angegebenen Argumente in die Programmausgabe geschrieben.  
        for (String argument : arguments) {  
            System.out.println("Argument: " + argument);  
        }  
    }  
}
```

Dieses Java-Programm kann von der Kommandozeile mit dem folgenden Befehl ausgeführt werden:

```bash
java MainClass.java
```

Hinter diesen Befehl können nun beliebig viele Argumente angehängt werden, zum Beispiel *"mein-erstes-argument"* und *"Nummer2"*.

```powershell
# EINGABE
C:\Users\benutzername\JavaBeispiel> java MainClass.java mein-erstes-argument Nummer2

# AUSFÜHRUNG DES BEFEHLS "java MainClass.java mein-erstes-argument Nummer2"
Es gibt 2 Argumente
Argument: mein-erstes-argument
Argument: Nummer2
```

### Argumente als Zahlen interpretieren
Programm-Argumente werden als eine Anreihung von Zeichenketten übergeben (Typ `String[]`).

Falls man ein Programm gestaltet, das eingegebene Zahlen verarbeiten soll, müssen die Argumente von dem Typ `String` in den Typ `int` oder `float` konvertiert werden.

In Java geht das mithilfe der statischen Methoden `Integer.parseInt()` oder `Float.parseFloat()` (Siehe auch: [[2023 SS/03 Objektorientierung/Datentypen#Hüllenklasse (Java)|Hüllenklasse]])

```java
String geschriebeneZahl = "12";

int zahl = Integer.parseInt(geschriebeneZahl);       // 12
float dezimal = Float.parseFloat(geschriebeneZahl);  // 12.0
```
