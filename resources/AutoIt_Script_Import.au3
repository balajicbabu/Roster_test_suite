#Region -- Functions which simulate the browser window dialog to save and close the dialog

Func _Au3RecordSetup()
Opt('WinWaitDelay',100)
Opt('WinDetectHiddenText',1)
Opt('MouseCoordMode',0)
Local $aResult = DllCall('User32.dll', 'int', 'GetKeyboardLayoutNameW', 'wstr', '')
If $aResult[1] <> '00020409' Then
  MsgBox(64, 'Warning', 'Recording has been done under a different Keyboard layout' & @CRLF & '(00020409->' & $aResult[1] & ')')
EndIf

EndFunc

Func _WinWaitActivate($title,$text,$timeout=30)
	WinWait($title,$text,$timeout)
	If Not WinActive($title,$text) Then WinActivate($title,$text)
	WinWaitActive($title,$text,$timeout)
EndFunc

_AU3RecordSetup()
#endregion --- Internal functions Au3Recorder End ---
WinWait("File Upload","")
_WinWaitActivate("File Upload","")
MouseClick("left",414,476,1)
ClipPut("")
Send(@UserProfileDir & "\workspace\Roster_test_suite\resources\2013_MensVarsityFootball_Roster.xlsx {TAB}{TAB}{ENTER}")
MouseClick("left",796,505,1)