Name:		luma
Summary:	LDAP browser, utility and more
Version:	2.4
Release:	5
Epoch:		1
Source:		http://prdownloads.sourceforge.net/luma/%{name}-%{version}.tar.bz2
URL:		http://luma.sourceforge.net/
License:	GPL
Group:		System/Configuration/Other
Requires:	PyQt >= 3.7
Requires:	python-ldap >= 2.0.1
Requires:	python-sip
Requires:	py-smbpasswd
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

%build
# nothing

%install
mkdir -p %{buildroot}%{_prefix}
./install.py --prefix=%{buildroot}%{_prefix}

# fix symlink, we need DESTDIR support for install.py
rm -f %{buildroot}%{_bindir}/luma
ln -s %{_prefix}/lib/luma/luma.py %{buildroot}%{_bindir}/luma

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

%files
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_prefix}/lib/%name
%{_datadir}/luma
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_mandir}/man1/*
%doc README


