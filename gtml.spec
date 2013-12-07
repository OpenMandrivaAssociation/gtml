Summary:	An html preprocessor 
Name:		gtml
Version:	3.5.4
Release:	12
License:	GPLv2+
Group:		Text tools
Url:		http://www.lifl.fr/~beaufils/gtml/
Source0:	%{name}-%{version}.tar.bz2
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
install -m 755 %{name} -D %{buildroot}%{_bindir}/%{name}

%files
%doc README src/NEWS.gtm gtml.html NEWS.html CREDITS.html  
%{_bindir}/*

