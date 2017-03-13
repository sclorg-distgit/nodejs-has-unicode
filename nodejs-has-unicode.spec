%{?scl:%scl_package nodejs-has-unicode}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-has-unicode

%global npm_name has-unicode
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-has-unicode
Version:    2.0.1
Release:    1%{?dist}
Summary:	Try to guess if your terminal supports unicode
Url:		https://github.com/iarna/has-unicode
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ISC

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(require-inject)
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
Try to guess if your terminal supports unicode

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/has-unicode

%doc README.md LICENSE

%changelog
* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.1-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-3
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-2
- Rebuilt with updated metapackage

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-1
- Initial build
