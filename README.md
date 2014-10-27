# AoikUrlToFile
A command to create Windows **.url** file. And tips on how to use it to save URL in Chrome or Iron's location bar to a **.url** file in one hotkey.

Tested working with:
- Windows  
- Python: 2.7+, 3.2+

[Package on PyPI](https://pypi.python.org/pypi/AoikUrlToFile)

## Contents
- [How to install](#how-to-install)
  - [Install via pip](#install-via-pip)
- [How to use](#how-to-use)
  - [Find the command](#find-the-command)
  - [Run the command](#run-the-command)
- [How to save Chrome URL to file](#how-to-save-chrome-url-to-file)
  - [Define a custom protocol handler](#define-a-custom-protocol-handler)
  - [Edit *Local State* file](#edit-local-state-file)
  - [Open a custom protocol url](#open-a-custom-protocol-url)
  - [Create a hotkey](#create-a-hotkey)
- [How to read the funny source code](#how-to-read-the-funny-source-code)


## How to install

### Install via pip
Run
```
pip install AoikUrlToFile
```
or
```
pip install git+https://github.com/AoiKuiyuyou/AoikUrlToFile
```

## How to use
### Find the command
After the [installation](#how-to-install), a command named **aoikutf** should be available on your console.

### Run the command
Show usage.
```
aoikutf -h
```

Create a **.url** file.  
The file name is synthesized from the url.
```
aoikutf https://pypi.python.org/pypi
```
```
https://pypi.python.org/pypi
to
pypi.python.org--pypi.url
```

Specify an output dir.
```
aoikutf https://pypi.python.org/pypi -d output_dir
```

## How to save Chrome URL to file
The real fun comes when use the command to save URL in Chrome's location bar.

### Define a custom protocol handler
First of all, We need find a way letting Chrome call our command with the URL in the location bar. This can be achieved by custom protocol handler.

If we prefix the url in the location bar with some custom protocl, e.g.
```
aoikutf://https://pypi.python.org/pypi
```
, then Chrome will look into Windows Registry's key
```
HKEY_CLASSES_ROOT\aoikutf\shell\open\command
```
for the comamnd to call.

Command **aoikutf** is able to create a **.reg** file for you to create this key in Registry. Run
```
aoikutf --reg -d D:\urls > aoikutf.reg
```
In case you prefer to use a different protocol handler name, specify it with arg **-s**. But remember to use the same name in the steps below.
```
aoikutf --reg -d D:\urls -s aoikuuttff > aoikutf.reg
```

A **.reg** file with content resembling the follwing will be created.
```
REGEDIT4
[HKEY_CLASSES_ROOT\aoikutf\shell\open\command]
@="\"D:\\Python\\python.exe\" \"D:\\Python\\Lib\\site-packages\\aoikurltofile\\aoikurltofile_.py\" -d \"D:\\urls\" \"%1\""
```

Double-click it to import to Registry. After that done, you've got a custom protocol handler ready.

### Edit *Local State* file
Merely having a custom protocol handler defined in Registry is not enough for Chrome to call it. Because by default, Chrome does not think *aoikutf://* as a custom protocol and it will search the text in Google instead.

To tell Chrome to call custom protocol handler instead, we need edit Chrome's *Local State* file.

Depending on the program you are running, *Local State* file's location varies.

- If your are using Chrome's **chrome.exe**, located at
  ```
C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
  ```
  , then *Local State* file is located at
  ```
C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Local State
  ```
  Note ```%USERNAME%``` is a variable for your Windows username.
  
- If your are using Iron's **IronPortable.exe**, located at for example
  ```
D:\Iron\IronPortable.exe
  ```
  , then *Local State* file is located at
  ```
D:\Iron\Data\IronPortableData\Local State
  ```
  
- If your are using Iron's **chrome.exe**, located at for example  
  ```
D:\Iron\Iron\chrome.exe
  ```  
  , then *Local State* file is located at  
  ```
C:\Users\%USERNAME%\AppData\Local\Chromium\User Data\Local State
  ```  
  Note ```%USERNAME%``` is a variable for your Windows username.

A simple way to verify if you have found the right *Local State* file is have it opened in a text editor that can detect file change. And then open and close your Chrome or Iron program once. The right one should be detected changed on closing of the program.

Before open the *Local State* file for editing, make sure Chrome or Iron's programs are closed. Otherwise your change will be overwritten.

The change you need to make is find the ```protocol_handler``` and ```excluded_schemes``` part, and add your protocol handler to it with a ```false``` value, like this
```
"protocol_handler": {
  "excluded_schemes": {
     "aoikaoik": false,
```
The ```false``` value does the trick of letting Chrome call custom protocol defined in Registry, instead of searching in Google.

Sometimes the ```protocol_handler``` part may not even exist in the *Local State* file. This is because you haven't tried opening a custom protocol in the location bar for once. Just try opening it once. Chrome will search the text in Google. Don't worry. Close Chrome to have it overwritten the *Local State* file. Then the ```protocol_handler``` part should appear.

### Open a custom protocol url
Now that you've got the custom protocol handler ready and the *Local State* file edited, Chrome should be able to call program **aoikutf** when the protocol scheme is *aoikutf*.

For example, open this url in Chrome's location bar.
```
aoikutf://https://pypi.python.org/pypi
```

If everythong goes well, you should be able to find a file named **pypi.python.org--pypi.url**, in the output dir you specified when [defining the custom protocol handler](#define-a-custom-protocol-handler).

### Create a hotkey
It's really tedious having to type in ```aoikutf://``` to the location bar for every url you want to save. What we need is a hotkey.

Here is how to make one in [AutoHotkey](http://www.autohotkey.com/).
```
<^1::
SetKeyDelay, 10
Send ^l{Home}aoikutf://{Enter}
```

The ```^l``` part means **Ctrl+l**, which is Chrome's hotkey for moving cursor focus to the location bar. Then the ```{Home}``` key moves the cursor to the beginning of the url, followed by the typing of ```aoikutf://```, and ended with a ```{Enter}``` key that opens the url. The ```SetKeyDelay, 10``` part makes the typing quick enough but not overspeeding.

## How to read the funny source code
For developers interested in reading the source code,  
Here is a flowchart ([.png](/doc/dev/main.png?raw=true), [.svg](/doc/dev/main.svg?raw=true), or [.graphml](/doc/dev/main.graphml?raw=true)) that has recorded key steps of the program.  
![Image](/doc/dev/main.png?raw=true)

The flowchart is produced using free graph editor [yEd](http://www.yworks.com/en/products_yed_download.html).

If you want to copy the text in the graph, it's recommended to download the [.svg](/doc/dev/main.svg?raw=true) file and open it locally in your browser. (For security reason, Github has disabled rendering of SVG images on the page.)

The meaning of the shapes in the flowchart should be straightforward.  
One thing worth mentioning is isosceles trapezium means sub-steps.

The most useful feature of the flowchart is, for each step in it,
there is a 7-character ID.  
This ID can be used to locate (by text searching) the code that implements a step.  
This mechanism has two merits:

1. It has provided **precise** (locating precision is line-level)
  and **fast** (text searching is fast) mapping from doc to code, which is
  very handy for non-trivial project.

  Without it you have to rely on developers' memory to recall the code locations (*Will you recall them after several months, precise and fast?*).

2. It has provided **precise** (unique ID) and **concise** (7-character long) names
  for each steps of a program, which is very handy for communicating between
  members of a development team.

  Without it describing some steps of a program between team members tends to be unclear.
