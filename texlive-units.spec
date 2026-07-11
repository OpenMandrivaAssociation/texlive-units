%global tl_name units
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9b
Release:	%{tl_revision}.1
Summary:	Typeset units
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/units
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/units.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/units.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/units.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is provided as a bundle with the nicefrac package for typing
fractions. Units uses nicefrac in typesetting physical units in a
standard-looking sort of way.

