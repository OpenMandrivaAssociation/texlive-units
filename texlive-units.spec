# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/units
# catalog-date 2009-09-27 11:52:43 +0200
# catalog-license gpl
# catalog-version 0.9b
Name:		texlive-units
Version:	0.9b
Release:	1
Summary:	Typeset units
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/units
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/units.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/units.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/units.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package is provided as a bundle with the nicefrac package
for typing fractions. Units uses nicefrac in typesetting
physical units in a standard-looking sort of way.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
