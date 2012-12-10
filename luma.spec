%define name	luma
%define version 2.4
%define rel 4
%define release %mkrel %rel

Name:		%{name}
Summary:	LDAP browser, utility and more
Version:	%{version}
Release:	%{release}
Epoch:		1
Source:		http://prdownloads.sourceforge.net/luma/%{name}-%{version}.tar.bz2
URL:		http://luma.sourceforge.net/
License:	GPL
Group:		System/Configuration/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	PyQt >= 3.7 , python-ldap >= 2.0.1
Requires:	python-sip
Requires:       py-smbpasswd
%py_requires
BuildArch:	noarch

%description
Luma is a graphical utility for accessing and managing data
stored on LDAP servers. It is written in Python, using PyQt
and python-ldap. Plugin-support is included and useful
widgets with LDAP-functionality for easy creation of plugins
are delivered.

%prep
%setup -q

#%build
#
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}
./install.py --prefix=$RPM_BUILD_ROOT%{_prefix}

# fix symlink, we need DESTDIR support for install.py
rm -f %{buildroot}%{_bindir}/luma
ln -s %{_prefix}/lib/luma/luma.py %{buildroot}%{_bindir}/luma

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Luma
Comment=LDAP browser, utility and more
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Qt;System;
EOF

mkdir -p %{buildroot}/{%{_iconsdir},%{_liconsdir},%{_miconsdir}}
ln -s %{_datadir}/%{name}/icons/luma-16.png %{buildroot}/%{_miconsdir}/%{name}.png
ln -s %{_datadir}/%{name}/icons/luma-32.png %{buildroot}/%{_iconsdir}/%{name}.png
ln -s %{_datadir}/%{name}/icons/luma-48.png %{buildroot}/%{_liconsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_prefix}/lib/%name
%{_datadir}/luma
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%_mandir/man1/*
%doc README


%changelog
* Tue Nov 23 2010 Funda Wang <fwang@mandriva.org> 1:2.4-4mdv2011.0
+ Revision: 599898
- rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1:2.4-3mdv2011.0
+ Revision: 439662
- rebuild

* Sat Feb 14 2009 Frederik Himpe <fhimpe@mandriva.org> 1:2.4-2mdv2009.1
+ Revision: 340230
- Rebuild for python 2.6

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1:2.4-1mdv2009.0
+ Revision: 218422
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Feb 28 2008 Andreas Hasenack <andreas@mandriva.com> 1:2.4-1mdv2008.1
+ Revision: 176227
- updated to 2.4 final

* Wed Jan 23 2008 Andreas Hasenack <andreas@mandriva.com> 2.4-1.pre2.5mdv2008.1
+ Revision: 157197
- fix "All files" mask

* Tue Jan 22 2008 Andreas Hasenack <andreas@mandriva.com> 2.4-1.pre2.4mdv2008.1
+ Revision: 156699
- fix backtrace in save file dialogs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Funda Wang <fwang@mandriva.org> 2.4-1.pre2.3mdv2008.0
+ Revision: 77810
- fix menu entry category (bug#33058)


* Wed Nov 29 2006 Andreas Hasenack <andreas@mandriva.com> 2.4-1.pre2.2mdv2007.0
+ Revision: 88467
- rebuild with python 2.5
- added py-smbpasswd to requires

* Mon Nov 13 2006 Andreas Hasenack <andreas@mandriva.com> 2.4-1.pre2.1mdv2007.0
+ Revision: 83836
- added proper buildrequires for python
- updated to 2.4pre2
- the /usr/lib thing smells like a hack, but it's like
  this upstream. Proper location of python files will
  need a more intrusive patch

* Tue Sep 05 2006 Buchan Milne <bgmilne@mandriva.org> 2.3-3mdv2007.0
+ Revision: 59761
- fix package summary to match menu entry
  fix package group to match menu location
- fix icons in menus
- xdg menu
  fix long title (Luma is Qt-only, not KDE), using description from homepage

  + Andreas Hasenack <andreas@mandriva.com>
    - added requirement for python-sip

* Tue Jul 18 2006 Andreas Hasenack <andreas@mandriva.com> 2.3-2mdv2007.0
+ Revision: 41491
- bump release
- using mkrel
- added svn warning
- import luma-2.3-1mdk

* Tue Mar 14 2006 Buchan Milne <bgmilne@mandriva.org> 2.3-1mdk
- New release 2.3

* Wed Aug 24 2005 Buchan Milne <bgmilne@linux-mandrake.com> 2.2.1-1mdk
- New release 2.2.1

* Wed Aug 17 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.2-1mdk
- 2.2

* Wed Mar 16 2005 Michael Scherer <misc@mandrake.org> 2.1.2-1mdk
- New release 2.1.2

* Tue Mar 15 2005 Michael Scherer <misc@mandrake.org> 2.1.1-1mdk
- New release 2.1.1

* Thu Mar 03 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.1-1mdk
- 2.1

* Tue Feb 15 2005 Michael Scherer <misc@mandrake.org> 2.0.3-1mdk
- New release 2.0.3

* Fri Jan 21 2005 Michael Scherer <misc@mandrake.org> 2.0-1mdk
- New release 2.0

* Mon Dec 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.6-1mdk
- 1.6

* Wed Nov 10 2004 Buchan Milne <bgmilne@linux-mandrake.com> 1.5-1mdk
- 1.5

* Fri Sep 03 2004 Buchan Milne <bgmilne@linux-mandrake.com> 1.4-1mdk
- 1.4

* Wed May 19 2004 Frederic Lepied <flepied@mandrakesoft.com> 1.3-1mdk
- New release 1.3

* Mon Apr 05 2004 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.2-1mdk
- 1.2

