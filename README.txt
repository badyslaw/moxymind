--- GENERAL ---
EXEC dir: ..\moxymind>
EXEC cmd (with report): >pytest --html=reports/report.html

--- ANDROID (Tested on) ---
Emulator:
    Version: 10
    Name: Android
Physical:
    Version: 9
    Name: Pixel

settings.py -> IS_EMULATOR=True/False to decide what type of device the tester is using