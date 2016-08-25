%define oname RedNotebook
%define name %(echo %{oname} | tr [:upper:] [:lower:])

Summary:	A modern desktop journal
Name:		%{name}
Version:	1.13
Release:	0
License:	( GPLv2+ and LGPLv3+ ) or GPLv3+
Group:		Office
URL:		http://%{name}.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
#Source0:	http://sourceforge.net/projects/rednotebook/files/%{name}-%{version}.tar.gz
#Source0:	https://github.com/jendrikseipp/%{name}/archive/v%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	desktop-file-utils

Requires:	pygtk2.0
Requires:	python
Requires:	python-yaml
Requires:	python-webkitgtk
#Suggests:	pygtkspellcheck

%description
RedNotebook is a modern desktop journal. It lets you format, tag and search
your entries. You can also add pictures, links and customizable templates,
spell check your notes, and export to plain text, HTML, Latex or PDF.

%files -f FILELIST
%{_iconsdir}/hicolor/*/apps/%{name}.png
%doc README.md
%doc CHANGELOG
%doc LICENSE

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot} --record=FILELIST

# remove *.pyc files from FILELIST
sed -i '/\\*.pyc$/d' FILELIST

# icons
for d in 14 16 22 32 48 64 128 192 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	cp %{buildroot}%{py2_puresitedir}/%{name}/images/rednotebook-icon/rn-${d}.png \
	   %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done

%check
# .desktop file
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

