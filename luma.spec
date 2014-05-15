Name:		luma
Summary:	LDAP browser, utility and more

Version:	3.0.7
Release:	1
Epoch:		1
Source0:	%{name}-%{version}.tar.gz
URL:		http://luma.sourceforge.net/
License:	GPL
Group:		System/Configuration/Other
Requires:	python-qt4 >= 4.8
Requires:	python-ldap >= 2.3
Requires:	python-sip
Requires:	py-smbpasswd
BuildRequires:  python-devel
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
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{py_puresitedir}/%{name}
%{py_puresitedir}/%{name}-%{version}-py*.egg-info
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*
