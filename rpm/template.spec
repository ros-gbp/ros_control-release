Name:           ros-jade-joint-limits-interface
Version:        0.10.2
Release:        0%{?dist}
Summary:        ROS joint_limits_interface package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ros-controls/ros_control/wiki
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-hardware-interface
Requires:       ros-jade-roscpp
Requires:       urdfdom-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-hardware-interface
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostest
BuildRequires:  urdfdom-devel

%description
Interface for enforcing joint limits.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Nov 28 2016 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.10.2-0
- Autogenerated by Bloom

* Fri Nov 20 2015 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.10.0-1
- Autogenerated by Bloom

* Fri Nov 20 2015 Adolfo Rodriguez Tsouroukdissian <adolfo.rodriguez@pal-robotics.com> - 0.10.0-0
- Autogenerated by Bloom

