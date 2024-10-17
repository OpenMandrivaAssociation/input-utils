
%define name	input-utils
%define version	0
%define cvsrev	20061008
%define rel	4

%define release	%mkrel 0.%cvsrev.%rel

Summary:	Linux input utilities
Name:		%name
Version:	%version
Release:	%release
Group:		System/Kernel and hardware
URL:		https://linuxconsole.sourceforge.net/
# From cvs ruby/utils
Source:		%name-%cvsrev.tar.bz2
Source1:	jscal.1
Source2:	jstest.1
Patch0:		joystick-1.2.15-dont-exit-when-wrong-version.patch
License:	GPL
BuildRequires:	SDL-devel
Obsoletes:	joystick
Provides:	joystick
BuildRoot:	%{_tmppath}/%{name}-root

%description
Userspace utilities for input devices:
- evtest: test event device
- ffcfstress: stress test constant force
- ffmvforce: test constant force with SDL window
- ffset: set force feedback options
- fftest: test force feedback
- inputattach: attach a serial line to an input device
- jscal: calibrate joystick
- jstest: test joystick device

%prep
%setup -q -n utils
%patch0 -p0 -b .version

cp %SOURCE1 %SOURCE2 .

%build
%make CFLAGS="%optflags"

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_bindir}
install -m755 evtest inputattach jstest jscal fftest ffmvforce ffset \
	ffcfstress %{buildroot}%{_bindir}

install -d -m755 %{buildroot}%{_mandir}/man1
install -m644 jscal.1 jstest.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/jscal.1*
%{_mandir}/man1/jstest.1*




%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0-0.20061008.4mdv2011.0
+ Revision: 612398
- the mass rebuild of 2010.1 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0-0.20061008.3mdv2010.1
+ Revision: 437961
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0-0.20061008.2mdv2009.1
+ Revision: 350285
- 2009.1 rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0-0.20061008.1mdv2009.0
+ Revision: 140776
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0-0.20061008.1mdv2008.1
+ Revision: 127072
- kill re-definition of %%buildroot on Pixel's request


* Fri Nov 03 2006 Anssi Hannula <anssi@mandriva.org> 0-0.20061008.1mdv2007.0
+ Revision: 76370
- Import input-utils

