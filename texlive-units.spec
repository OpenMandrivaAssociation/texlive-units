Name:		texlive-units
Version:	42428
Release:	2
Summary:	Typeset units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/units
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/units.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/units.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/units.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is provided as a bundle with the nicefrac package
for typing fractions. Units uses nicefrac in typesetting
physical units in a standard-looking sort of way.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/units/nicefrac.sty
%{_texmfdistdir}/tex/latex/units/units.sty
%doc %{_texmfdistdir}/doc/latex/units/COPYING
%doc %{_texmfdistdir}/doc/latex/units/README
%doc %{_texmfdistdir}/doc/latex/units/units.pdf
#- source
%doc %{_texmfdistdir}/source/latex/units/units.dtx
%doc %{_texmfdistdir}/source/latex/units/units.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
