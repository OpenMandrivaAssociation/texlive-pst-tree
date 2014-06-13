# revision 24142
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-tree
# catalog-date 2011-09-29 17:52:33 +0200
# catalog-license lppl
# catalog-version 1.12
Name:		texlive-pst-tree
Version:	1.12
Release:	7
Summary:	Trees, using pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-tree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tree.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tree.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pst-tree is a pstricks package that defines a macro \pstree
which offers a structured way of joining nodes created using
pst-node in order to draw trees.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-tree/pst-tree.tex
%{_texmfdistdir}/tex/latex/pst-tree/pst-tree.sty
%doc %{_texmfdistdir}/doc/generic/pst-tree/Changes
%doc %{_texmfdistdir}/doc/generic/pst-tree/README
%doc %{_texmfdistdir}/doc/generic/pst-tree/pst-tree-doc-de.pdf
%doc %{_texmfdistdir}/doc/generic/pst-tree/pst-tree-doc-de.tex
%doc %{_texmfdistdir}/doc/generic/pst-tree/pst-tree-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-tree/pst-tree-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-tree/pst-tree-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-tree/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.12-2
+ Revision: 755485
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.12-1
+ Revision: 719403
- texlive-pst-tree
- texlive-pst-tree
- texlive-pst-tree
- texlive-pst-tree

