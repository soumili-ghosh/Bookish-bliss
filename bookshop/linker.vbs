Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "main1.py" & Chr(34), 0
Set WinScriptHost = Nothing