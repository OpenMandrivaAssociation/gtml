%define	name	gtml
%define	version	3.5.4
%define	release	%mkrel 10

Summary:	An html preprocessor 
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
License:	GPLv2+
URL:		http://www.lifl.fr/~beaufils/gtml/
Group:		Text tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch:	noarch

%description
gtml is an HTML pre-processor which adds some extra features specially designed
for maintaining multiple Web pages. Using gtml you can create and use macros
to save typing, create a "project file" with the names of all your Web pages
to update them all with one command, give specific alias to filename to make it
is easy to move files and have links preserved, specify a tree-like hierarchy
of Web pages to have Next, Previous and Up links added automatically, include
files into all your HTML files, include a timestamp, use conditional commands 
to create different versions of the output, and generate output to different
irectories to generate different versions of your site.  
 
%prep
%setup -q 

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README src/NEWS.gtm gtml.html NEWS.html CREDITS.html  
%{_bindir}/*




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.5.4-8mdv2011.0
+ Revision: 664960
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3.5.4-7mdv2011.0
+ Revision: 605514
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.5.4-6mdv2010.1
+ Revision: 522814
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 3.5.4-5mdv2010.0
+ Revision: 425080
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 3.5.4-4mdv2009.0
+ Revision: 221120
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Nov 04 2007 Adam Williamson <awilliamson@mandriva.org> 3.5.4-3mdv2008.1
+ Revision: 105691
- rebuild for 2008.1
- don't package COPYING
- new license policy


* Thu Nov 23 2006 Lenny Cartier <lenny@mandriva.com> 3.5.4-2mdv2007.0
+ Revision: 86612
- Mkrel
- Import gtml

