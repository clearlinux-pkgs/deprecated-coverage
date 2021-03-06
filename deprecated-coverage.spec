#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-coverage
Version  : 4.5.3
Release  : 66
URL      : https://files.pythonhosted.org/packages/82/70/2280b5b29a0352519bb95ab0ef1ea942d40466ca71c53a2085bdeff7b0eb/coverage-4.5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/82/70/2280b5b29a0352519bb95ab0ef1ea942d40466ca71c53a2085bdeff7b0eb/coverage-4.5.3.tar.gz
Summary  : Code coverage measurement for Python
Group    : Development/Tools
License  : Apache-2.0
Requires: deprecated-coverage-bin = %{version}-%{release}
Requires: deprecated-coverage-license = %{version}-%{release}
Requires: deprecated-coverage-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools-legacypython
BuildRequires : tox
BuildRequires : virtualenv

%description
.. Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
.. For details: https://bitbucket.org/ned/coveragepy/src/default/NOTICE.txt

%package bin
Summary: bin components for the deprecated-coverage package.
Group: Binaries
Requires: deprecated-coverage-license = %{version}-%{release}

%description bin
bin components for the deprecated-coverage package.


%package extras
Summary: extras components for the deprecated-coverage package.
Group: Default

%description extras
extras components for the deprecated-coverage package.


%package legacypython
Summary: legacypython components for the deprecated-coverage package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-coverage package.


%package license
Summary: license components for the deprecated-coverage package.
Group: Default

%description license
license components for the deprecated-coverage package.


%package python
Summary: python components for the deprecated-coverage package.
Group: Default

%description python
python components for the deprecated-coverage package.


%prep
%setup -q -n coverage-4.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554311066
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-coverage
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/deprecated-coverage/LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/coverage
%exclude /usr/bin/coverage-2.7
%exclude /usr/bin/coverage2

%files extras
%defattr(-,root,root,-)
/usr/bin/coverage-2.7
/usr/bin/coverage2

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-coverage/LICENSE.txt

%files python
%defattr(-,root,root,-)
