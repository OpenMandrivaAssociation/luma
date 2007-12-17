%define name	luma
%define version 2.4
%define prerelease pre2
%define rel 3
%define release %mkrel 1.pre2.%rel

Name: 	 	%{name}
Summary: 	LDAP browser, utility and more
Version: 	%{version}
Release: 	%{release}
Source:		http://prdownloads.sourceforge.net/luma/%{name}-%{version}%{prerelease}.tar.bz2
URL:		http://luma.sourceforge.net/
License:	GPL
Group:		System/Configuration/Other
Requires:	PyQt >= 3.7 , python-ldap >= 2.0.1
Requires:	python-sip
Requires:   py-smbpasswd
%py_requires
BuildArch:	noarch

%description
Luma is a graphical utility for accessing and managing data
stored on LDAP servers. It is written in Python, using PyQt
and python-ldap. Plugin-support is included and useful
widgets with LDAP-functionality for easy creation of plugins
are delivered.

%prep
%setup -q -n %{name}-%{version}%{prerelease}

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

%post
%update_menus
		
%postun
%clean_menus

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
