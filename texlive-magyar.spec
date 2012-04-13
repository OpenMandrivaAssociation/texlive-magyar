# revision 25806
# category Package
# catalog-ctan /language/hungarian/babel/magyar.ldf
# catalog-date 2012-03-26 14:33:04 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-magyar
Version:	20120326
Release:	1
Summary:	Hungarian language definition for Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hungarian/babel/magyar.ldf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magyar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/magyar.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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
