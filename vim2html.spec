Summary:	Vim-editable file converter to HTML
Summary(pl):	Konwerter edytowalnych plików Vima do formatu HTML
Name:		vim2html
Version:	1.42
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://norlug.org/~chipster/download_handler/cat5/%{name}-%{version}.tar.gz
# Source0-md5:	da1a1c79b17181fdf3d69f2417f90e0b
URL:		http://norlug.org/~chipster/vim2html
Requires:	tidy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vim2html is a small program that exports any Vim-editable file into
well-formed HTML - simulating a Vim session. Fully supports Vim
colorization (customizable) and Syntax Highlighting. This program
provides an excellent method of presenting your
programs/HTML/scripts/etc. on the web.

%description -l pl
vim2html jest ma³ym programem, który eksportuje ka¿dy edytowalny przez
Vima plik do dobrze sformatowanego HTML-a symuluj±c sesjê Vima. Pe³ne
wsparcie dla koloryzowania Vima i pod¶wietlania sk³adni. Program
dostarcza doskona³ej metody prezentacji programów/HTML-a/skryptów/itp. w
Internecie.

%prep
%setup -q

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
