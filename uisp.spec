Summary:	Atmel AVR Micro In-System Programmer
Summary(pl):	Programator mikrosterowników Atmel AVR 
Name:		uisp
Version:	1.0b
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://medo.fov.uni-mb.si/mapp/uTools/%{name}-%{version}.src.tar.gz
Source1:	http://medo.fov.uni-mb.si/mapp/uTools/uisp-parport-connect.txt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uisp allows to program contents of Atmel AVR's flash memory in-system.
It supports many types programmers.

%description -l pl
uisp pozwala programować zawartość pamięci flash mikrosterowników Atmel
AVR bezpośrednio w systemie. Obsługuje wiele rodzajów programatorów.

%prep
%setup -q %{name}-%{version}

%build
cd src
%{__make} CC=%{__cc} CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install src/uisp $RPM_BUILD_ROOT%{_bindir}
cp %{SOURCE1} .

gzip -9nf CHANGES INSTALL uisp-parport-connect.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
