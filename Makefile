all: mo

mo:
	for name in po/*.po; do\
		msgfmt -o $${name/.po/.mo} $${name};\
    done

pot:
	xgettext *.py */*.py */*/*.py -o po/template.pot --omit-header
