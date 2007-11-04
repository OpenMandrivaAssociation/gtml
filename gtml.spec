%define	name	gtml
%define	version	3.5.4
%define	release	%mkrel 3

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


