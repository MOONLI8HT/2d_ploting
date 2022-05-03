Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "A:\VSC\inter\2d_plot.bat" & Chr(34), 0
Set WshShell = Nothing