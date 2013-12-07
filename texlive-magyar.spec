# revision 25806
# category Package
# catalog-ctan /language/hungarian/babel/magyar.ldf
# catalog-date 2012-03-26 14:33:04 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-magyar
Version:	20120326
Release:	4
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


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120326-1
+ Revision: 790675
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110911-2
+ Revision: 753677
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110911-1
+ Revision: 718939
- texlive-magyar
- texlive-magyar
- texlive-magyar
- texlive-magyar

