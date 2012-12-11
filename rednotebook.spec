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


%changelog
* Fri Jul 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.5.0-1
+ Revision: 811263
- version update 1.5.0

* Fri May 13 2011 Jani Välimaa <wally@mandriva.org> 1.1.6-1
+ Revision: 674353
- new version 1.1.6

* Wed May 04 2011 Jani Välimaa <wally@mandriva.org> 1.1.5-1
+ Revision: 666146
- new version 1.1.5
- drop buildroot definition

* Mon Mar 28 2011 Jani Välimaa <wally@mandriva.org> 1.1.4-1
+ Revision: 648663
- new version 1.1.4

* Thu Mar 03 2011 Jani Välimaa <wally@mandriva.org> 1.1.3-1
+ Revision: 641429
- update to new version 1.1.3

* Mon Dec 27 2010 Jani Välimaa <wally@mandriva.org> 1.1.2-1mdv2011.0
+ Revision: 625378
- new version 1.1.2

* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 1.1.1-2mdv2011.0
+ Revision: 594336
- rebuild for python 2.7

* Sun Sep 05 2010 Jani Välimaa <wally@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 576153
- import rednotebook

