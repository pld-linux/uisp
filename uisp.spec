Summary:	Atmel AVR Micro In-System Programmer
Summary(pl):	Programator mikrosterowników Atmel AVR
Name:		uisp
Version:	1.0b
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://medo.fov.uni-mb.si/mapp/uTools/%{name}-%{version}.src.tar.gz
# Source0-md5:	3945498181030e6c000f705ac53b920f
Source1:	http://medo.fov.uni-mb.si/mapp/uTools/uisp-parport-connect.txt
# NoSource1-md5:	4ce613ab777f3608d4b861e2bdc6a16c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uisp allows to program contents of Atmel AVR's flash memory in-system.
It supports many types programmers.

%description -l pl
uisp pozwala programowaæ zawarto¶æ pamiêci flash mikrosterowników Atmel
AVR bezpo¶rednio w systemie. Obs³uguje wiele rodzajów programatorów.

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


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL uisp-parport-connect.txt
%attr(755,root,root) %{_bindir}/*
