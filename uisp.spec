Summary:	Atmel AVR Micro In-System Programmer
Summary(pl):	Programator mikrosterowników Atmel AVR
Name:		uisp
Version:	20040311
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/uisp/%{name}-%{version}.tar.bz2
# Source0-md5:	ddb3b742d96f85440dfe627d54797f6e
Source1:	http://medo.fov.uni-mb.si/mapp/uTools/uisp-parport-connect.txt
# NoSource1-md5:	4ce613ab777f3608d4b861e2bdc6a16c
#Patch0:		%{name}-debian.patch
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
#%%patch0 -p1

%build
%configure
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
%doc AUTHORS CHANGES ChangeLog* NEWS TODO uisp-parport-connect.txt
%attr(755,root,root) %{_bindir}/*
