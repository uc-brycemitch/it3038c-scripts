$IP = (Get-NetIPAddress).ipv4address | Select-String "192*"
$USER = $HOST.Name
$HOSTNAME = [System.Net.Dns]::GetHostName()
$VERSION = $HOST.Version.Major
$TODAY = (Get-Date -format 'D')

$BODY = "The Machine's IP address is $IP. The User is $USER. The Hostname is $HOSTNAME. Powershell version is $VERSION. Today's Date is $TODAY."