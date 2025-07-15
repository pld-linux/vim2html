Summary:	Vim-editable file converter to HTML
Summary(pl.UTF-8):	Konwerter edytowalnych plików Vima do formatu HTML
Name:		vim2html
Version:	1.46
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://norlug.org/~chipster/resources/vim2html/%{name}-%{version}.tar.gz
# Source0-md5:	4fcccd28b2a28519bdc65e90120c7204
URL:		http://norlug.org/~chipster/vim2html/
Patch0:		%{name}-VIM_HOME.patch
Requires:	tidy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vim2html is a small program that exports any Vim-editable file into
well-formed HTML - simulating a Vim session. Fully supports Vim
colorization (customizable) and Syntax Highlighting. This program
provides an excellent method of presenting your
programs/HTML/scripts/etc. on the web.

%description -l pl.UTF-8
vim2html jest małym programem, który eksportuje każdy edytowalny przez
Vima plik do dobrze sformatowanego HTML-a symulując sesję Vima. Pełne
wsparcie dla koloryzowania Vima i podświetlania składni. Program
dostarcza doskonałej metody prezentacji programów/HTML-a/skryptów/itp. w
Internecie.

%prep
%setup -q
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install vim2html $RPM_BUILD_ROOT%{_bindir}
install man/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
