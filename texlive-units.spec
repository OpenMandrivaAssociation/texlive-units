# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/units
# catalog-date 2009-09-27 11:52:43 +0200
# catalog-license gpl
# catalog-version 0.9b
Name:		texlive-units
Version:	0.9b
Release:	4
Summary:	Typeset units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/units
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/units.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/units.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/units.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9b-2
+ Revision: 757288
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9b-1
+ Revision: 719851
- texlive-units
- texlive-units
- texlive-units

