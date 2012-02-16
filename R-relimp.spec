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
Requires:         R-nnet R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-tcltk 
BuildRequires:    R-nnet R-MASS 
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
