Name:		texlive-pst-tree
Version:	1.13
Release:	1
Summary:	Trees, using pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-tree
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tree.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tree.doc.tar.xz
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
%{_texmfdistdir}/tex/generic/pst-tree
%{_texmfdistdir}/tex/latex/pst-tree
%doc %{_texmfdistdir}/doc/generic/pst-tree

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
