Summary:	Atmel AVR Micro In-System Programmer
Summary(pl):	Programator mikrosterowników Atmel AVR
Name:		uisp
Version:	20050207
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/uisp/%{name}-%{version}.tar.gz
# Source0-md5:	b1e499d5a1011489635c1a0e482b1627
URL:		http://savannah.nongnu.org/projects/uisp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uisp allows to program contents of Atmel AVR's flash memory in-system.
It supports many types programmers.

%description -l pl
uisp pozwala programowaæ zawarto¶æ pamiêci flash mikrosterowników
Atmel AVR bezpo¶rednio w systemie. Obs³uguje wiele rodzajów
programatorów.

%prep
%setup -q %{name}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES ChangeLog* NEWS TODO doc/[!H]*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
