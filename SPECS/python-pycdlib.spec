%global desc Pycdlib is a pure python library for reading, writing, and otherwise\
manipulating ISO9660 files.  It is focused on speed, correctness, and\
conformance to the various standards around ISO9660, including ISO9660 itself,\
the Joliet extensions, the Rock Ridge extensions, the El Torito boot\
extensions, and UDF.

%global srcname pycdlib

Summary:        A pure python ISO9660 read and write library
Name:           python-%{srcname}
Version:        1.11.0
Release:        5%{?dist}
License:        LGPLv2
URL:            https://github.com/clalancette/%{srcname}
Source0:        https://github.com/clalancette/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%package -n %{srcname}-tools
Summary:        Tools that rely on %{srcname}
Requires:       python3-%{srcname} = %{version}-%{release}

%description -n %{srcname}-tools
Some tools that use the %{srcname} library.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYCDLIB_TRACK_WRITES=1 py.test-%{python3_version} -v \
-k "not test_hybrid and not test_parse and not test_pycdlib_genisoimage" tests

%files -n python3-%{srcname}
%license COPYING
%doc README.md examples/
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/

%files -n %{srcname}-tools
%license COPYING
%{_bindir}/pycdlib-explorer
%{_bindir}/pycdlib-extract-files
%{_bindir}/pycdlib-genisoimage
%{_mandir}/man1/*

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.11.0-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 15 2021 Brian C. Lane <bcl@redhat.com> - 1.11.0-4
- Disable tests that use genisoimage
  Resolves: rhbz#1972212

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.11.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Chris Lalancette <clalancette@gmail.com> - 1.11.0-1
- Update to upstream 1.11.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Chris Lalancette <clalancette@gmail.com> - 1.9.0-1
- Update to upstream version 1.9.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.8.0-2
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Chris Lalancette <clalancette@gmail.com> - 1.8.0-1
- Update to upstream version 1.8.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Chris Lalancette <clalancette@gmail.com> - 1.7.0-1
- Update to upstream version 1.7.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-2
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Jul 29 2018 Chris Lalancette <clalancette@gmail.com> - 1.6.0-1
- Update to upstream version 1.6.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-2
- Rebuilt for Python 3.7

* Sat Jun 23 2018 Chris Lalancette <clalancette@gmail.com> - 1.5.0-1
- Update to upstream version 1.5.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.7

* Fri May 04 2018 Chris Lalancette <clalancette@gmail.com> - 1.4.0-1
- Update to upstream version 1.4.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Chris Lalancette <clalancette@gmail.com> - 1.3.2-1
- Update to upstream version 1.3.2

* Mon Nov 20 2017 Chris Lalancette <clalancette@gmail.com> - 1.3.1-1
- Update to upstream version 1.3.1

* Sun Nov 19 2017 Chris Lalancette <clalancette@gmail.com> - 1.3.0-1
- Update to upstream version 1.3.0

* Tue Oct 03 2017 Chris Lalancette <clalancette@gmail.com> - 1.2.0-1
- Update to upstream version 1.2.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jan 31 2017 Chris Lalancette <clalancette@gmail.com> - 1.1.0-1
- Update to upstream version 1.1.0

* Tue Oct 25 2016 Chris Lalancette <clalancette@gmail.com> - 1.0.0-1
- Update to upstream version 1.0.0

* Wed Dec 30 2015 Chris Lalancette <clalancette@gmail.com> - 0.1.0-1
- Initial package.
