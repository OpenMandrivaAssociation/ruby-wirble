%define rname	wirble

%define name	ruby-%{rname}
%define version 0.1.3
%define release %mkrel 1

Summary:	Enhancements for Irb
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pablotron.org/files/gems/%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
Url:		http://pablotron.org/software/wirble/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems
Provides:	rubygem(%{rname})

%description
Wirble is a set of enhancements for Irb. Wirble enables several items
mentioned on the RubyGarden "Irb Tips and Tricks" page, including
tab-completion, history, and a built-in ri command, as well as
colorized results and a couple other goodies. The idea, of course, is
to fill Irb with useful features without turning your ~/.irbrc file
into swiss cheese.

%prep

%build

%install
%__rm -rf %{buildroot}
gem install --ri -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

%__rm -rf %{buildroot}%{ruby_gemdir}/cache

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec
