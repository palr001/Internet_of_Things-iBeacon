hciconfig hci0 up
hciconfig hci0 leadv 3
hciconfig hci0 noscan

sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 DA 7A BA 5E 33 33 33 33 33 33 33 33 69 42 03 60 00 05 00 A4 C8 00