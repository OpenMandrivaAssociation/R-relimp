%global packname  relimp
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0_3
Release:          1
Summary:          Relative Contribution of Effects in a Regression Model
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-tcltk 
Requires:         R-nnet
Requires:         R-MASS 
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex 
BuildRequires:    R-tcltk 
BuildRequires:    R-nnet
BuildRequires:    R-MASS 
BuildRequires:    pkgconfig(lapack)
%rename R-cran-relimp

%description
Functions to facilitate inference on the relative importance of predictors
in a linear or generalized linear model, and a couple of useful Tcl/Tk

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_3-1
+ Revision: 775049
- Update to latest version

* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0_2-1
+ Revision: 774875
- Update and rebuild with R2spec
- Update and rebuild with R2spec

* Tue Dec 29 2009 Jérôme Brenier <incubusss@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 483325
- import R-cran-relimp

