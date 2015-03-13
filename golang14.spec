Name: golang14
Version: 1.4.2
Release: 1%{?dist}
Summary: go 1.4

License: BSD
URL: http://golang.org           
Source0: https://storage.googleapis.com/golang/go%{version}.linux-amd64.tar.gz

Conflicts: golang

%description
golang 1.4


%prep
%setup -q -n go

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/usr/local/go

cp bin/* $RPM_BUILD_ROOT/%{_bindir}/.

cp -r . $RPM_BUILD_ROOT/usr/local/go/.

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/go{,doc,fmt}
/usr/local/go
/usr/local/go/*
