Name:           rednotebook
Version:        1.8.0
Release:        2
Summary:        A desktop diary
Group:          Office
License:        GPLv2+
URL:            http://rednotebook.sourceforge.net
Source0:        http://sourceforge.net/projects/rednotebook/files/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
Requires:       python-yaml
Requires:       pygtk2.0
Requires:       python-webkitgtk
Requires:       gnome-python-extras
Requires:	python-chardet

%description
RedNotebook is a desktop diary that makes it very easy for you
to keep track of the stuff you do and the thoughts you have. This
journal software helps you to write whole passages or just facts,
and does so in style.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --skip-build --root %{buildroot}
desktop-file-install                                    \
    --add-category="Calendar"                           \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS CHANGELOG LICENSE README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
# % {_datadir}/locale/*/
%dir %{py_puresitedir}/%{name}/
%{py_puresitedir}/%{name}/*.py*
%{py_puresitedir}/%{name}/external/
%{py_puresitedir}/%{name}/files/
%{py_puresitedir}/%{name}/gui/
%{py_puresitedir}/%{name}/images/
%{py_puresitedir}/%{name}/util/
%{py_puresitedir}/%{name}*.egg-info

