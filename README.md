# Adventure Sample Unity Game Automation

This framework covers the automation demo of Adventure sample game with text, objects and scene validation. Reports are saved under reports folder in framework and screenshots are saved under screenshot folder in framework.

How to run:
To run the framework, there is a Run.bat file which will trigger the execution of complete framework.

1. Download the framework.
2. Connect the device and enable the USB debugging mode from developer options in device.
3. Open command prompt execute 'adb devices'.
4. Execute 'adb forward tcp:13001 tcp:13000' in cmd.
5. Launch the appium server and start the server with 'Host - 0.0.0.0' and 'Port - 4723'.
6. Double click on the 'Run.bat' file from the framework to start execution.
