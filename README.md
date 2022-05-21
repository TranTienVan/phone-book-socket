# Socket Python programming

**Phobo** - Phone Book client-server application using: 

- [Socket](https://docs.python.org/3/library/socket.html) is a Python library that supports connecting two nodes on a network to communicate with each other. One socket listens on a particular port on an IP address while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

- [SQLite](https://www.sqlite.org/docs.html) is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day.

- [QT5](https://doc.qt.io/qt-5.15/) is a full development framework with tools designed to streamline the creation of applications and user interfaces for desktop, embedded, and mobile platforms.

![alt text](./assets//design.gif)
## Prerequisite
- Install Python 3

- Install Pip

## Getting Started

**Step 1. Clone the code into a fresh folder**

```
$ git clone https://github.com/TranTienVan/phone-book-socket.git
```

**Step 2. Create a Virtual Environment and install Dependencies.**

Create a new Virtual Environment for the project and activate it. 

```
$ virtualenv venv
$ source venv/bin/activate
```

Next, we need to install the project dependencies, which are listed in `requirements.txt`.

```
(venv) $ pip install -r requirements.txt
```

**Step 3. Run the Client and Server app**

Server
```
(venv) $ cd source/server
(venv) $ python server.py
```

Client
```
(venv) $ cd source/client
(venv) $ python main.py
```

![alt text](./assets/FormHome.png)

## Distributing
In order to create an executable file (e.g. '.exe', ELF file,...), we can use PyInstaller, which can be installed via `pip`:
```
(venv) $ pip install pyinstaller
```

We need to 'client' folder where 'main.py' is exist. Then run:
```
(venv) $ pyinstaller -n Phobo -F -w -i Resources/phobo.ico main.py
```
where:
- `-n Phobo` means naming application Phobo;
- `-F` means creating a one-file bundled executable;
- `-w` means not providing a console window for standard i/o;
- `-i Resources/phobo.ico` means applying the icon to a Windows executable ('Resources/phobo.ico' is needed).

If you've already installed Makefiles, then just simply run:
```
(venv) $ make
```
We need folder 'Resource' and file 'cookies.json' be in the same place of 'Phobo.exe', which was released in 'dist/'.
# Author
[Trần Tiến Văn](https://github.com/TranTienVan)

[Nguyễn Hoàng Khang](https://github.com/khangnh-22)

[Dương Lê Đình Thuận](https://github.com/ThuanDuongHCMUS)

