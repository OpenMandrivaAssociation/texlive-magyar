Name:		texlive-magyar
Version:	20110911
Release:	1
Summary:	Hungarian language definition for Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hungarian/babel/magyar.ldf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magyar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magyar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This is an interim release of a new version of the Magyar
language definition for babel.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/magyar/magyar.ldf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
