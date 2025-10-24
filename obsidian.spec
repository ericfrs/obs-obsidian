Name:           obsidian
Version:        1.9.14
Release:        0
Summary:        A powerful knowledge base that works on top of Markdown files
ExclusiveArch:  x86_64
License:        NonFree
URL:            https://obsidian.md
Source0:        https://github.com/obsidianmd/obsidian-releases/releases/download/v%{version}/obsidian-%{version}.tar.gz
Source1:        obsidian.sh
Source2:        obsidian.desktop

BuildRequires:  fdupes
BuildRequires:  update-desktop-files
Requires:       electron
Requires:       bash

%description
%{summary}.

%prep
%autosetup

%build

%install
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/obsidian
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/obsidian.desktop
install -Dm644 resources/icon.png %{buildroot}%{_datadir}/pixmaps/obsidian.png
install -dm0755 %{buildroot}%{_libdir}/obsidian
cp -a resources/* %{buildroot}%{_libdir}/obsidian/

find %{buildroot}%{_libdir}/obsidian -type f -name "*.js" -exec chmod 644 {} \;
find %{buildroot}%{_libdir}/obsidian -type f -name "*.json" -exec chmod 644 {} \;
find %{buildroot}%{_libdir}/obsidian -type f -name "*.mm" -exec chmod 644 {} \;

%fdupes %{buildroot}%{_libdir}/obsidian

%files
%{_bindir}/obsidian
%{_datadir}/applications/obsidian.desktop
%{_datadir}/pixmaps/obsidian.png
%{_libdir}/obsidian/

%changelog
* Fri Oct 24 2025 - 1.9.14
- Initial package