#!/bin/sh
function install() {
	mkdir /usr/share/levanditor
	cp ./editor.py /usr/share/levanditor/
	cp ./Le.png /usr/share/pixmaps/
	cp ./levanditor.desktop /usr/share/applications/
	echo "#!/bin/sh" >> /usr/bin/levanditor
	echo "python3 /usr/share/levanditor/editor.py" >> /usr/bin/levanditor
	chmod +x /usr/share/levanditor/editor.py
	chmod +x /usr/bin/levanditor
}

if [[ ${EUID} != 0 ]] ; then
	echo "ERROR: We are not root. Going root..." && su -c "bash $0"
else
	install
fi
