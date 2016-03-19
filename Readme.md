# RemoteAppHelper

## About

This is a helper application for .rdp files run.

## Dependencies

* python3
* python-keyring: For kwallet support
* PyQt5
* freerdp

## Example Desktop file

``` ini
[Desktop Entry]
Comment[en_US]=
Comment=
Exec=python3 src/remoteapphelper.py example.rdp
GenericName[en_US]=Example desktop file for remoteapp helper
GenericName=Example desktop file for remoteapp helper
Icon=exec
MimeType=
Name[en_US]=Example
Name=Example
Path=/home/example/remoteapphelper # You should set for the installation directory
StartupNotify=true
Terminal=false
TerminalOptions=
Type=Application
X-DBUS-ServiceName=
X-DBUS-StartupType=none
X-KDE-SubstituteUID=false
X-KDE-Username=
```
