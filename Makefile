all: mo

mo: po/zh_CN.mo po/zh_TW.mo

po/zh_CN.mo: po/zh_CN.po
	msgfmt -o ./po/zh_CN.mo ./po/zh_CN.po

po/zh_TW.mo: po/zh_TW.po
	msgfmt -o ./po/zh_TW.mo ./po/zh_TW.po

po/zh_CN.po: po/template.pot
	msgmerge -U po/zh_CN.po po/template.pot

po/zh_TW.po: po/template.pot
	msgmerge -U po/zh_TW.po po/template.pot

po/template.pot: *.py
	xgettext *.py -o po/template.pot --omit-header
