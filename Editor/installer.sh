#!/bin/sh
function install() {
        pip3 install PyQt5
	mkdir /usr/share/levanditor
	cp ./levditor.py /usr/share/levanditor/
	cp ./Le.png /usr/share/pixmaps/
	cp ./levanditor.desktop /usr/share/applications/
	echo "#!/bin/sh" >> /usr/bin/levanditor
	echo "python3 /usr/share/levanditor/levditor.py" >> /usr/bin/levanditor
	chmod +x /usr/share/levanditor/levditor.py
	chmod +x /usr/bin/levanditor
}

if [[ ${EUID} != 0 ]] ; then
	echo "ERROR: We are not root. Going root..." && su -c "bash $0"
else
	install
fi
