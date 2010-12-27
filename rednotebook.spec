Name:           rednotebook
Version:        1.1.2
Release:        %mkrel 1
Summary:        A desktop diary
Group:          Office
License:        GPLv2+
URL:            http://rednotebook.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf %{buildroot}
python setup.py install \
	--skip-build \
	--root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}*.egg-info
