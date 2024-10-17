Name:		texlive-unicode-bidi
Version:	42482
Release:	2
Summary:	Experimental unicode bidi package for XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unicode-bidi
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-bidi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-bidi.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The experimental unicode-bidi package allows to mix non-RTL
script with RTL script without any markup.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/unicode-bidi
%doc %{_texmfdistdir}/doc/xelatex/unicode-bidi

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
