Summary:	Atmel AVR Micro In-System Programmer
Summary(pl):	Programator mikrosterowników Atmel AVR
Name:		uisp
Version:	20030618
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://jubal.westnet.com/AVR/%{name}-%{version}.tar.gz
# Source0-md5:	0d5d475a5e5f7bb2bfa45e85c3b94af4
Source1:	http://medo.fov.uni-mb.si/mapp/uTools/uisp-parport-connect.txt
# NoSource1-md5:	4ce613ab777f3608d4b861e2bdc6a16c
Patch0:		%{name}-debian.patch
URL:		http://savannah.nongnu.org/projects/uisp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uisp allows to program contents of Atmel AVR's flash memory in-system.
It supports many types programmers.

%description -l pl
uisp pozwala programowaæ zawarto¶æ pamiêci flash mikrosterowników Atmel
AVR bezpo¶rednio w systemie. Obs³uguje wiele rodzajów programatorów.

%prep
%setup -q %{name}-%{version}
%patch0 -p1

%build
%configure2_13
%{__make}

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
