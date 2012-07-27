Name:           rednotebook
Version:        1.5.0
Release:        1
Summary:        A desktop diary
Group:          Office
License:        GPLv2+
URL:            http://rednotebook.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
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
%{__python} setup.py install --skip-build --root %{buildroot}
desktop-file-install                                    \
    --add-category="Calendar"                           \
    --delete-original                                   \
    --dir=%{buildroot}%{_datadir}/applications          \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS CHANGELOG LICENSE README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
# %{_datadir}/locale/*/
%dir %{python_sitelib}/%{name}/
%{python_sitelib}/%{name}/*.py*
%{python_sitelib}/%{name}/external/
%{python_sitelib}/%{name}/files/
%{python_sitelib}/%{name}/gui/
%{python_sitelib}/%{name}/images/
%{python_sitelib}/%{name}/util/
%{python_sitelib}/%{name}*.egg-info
