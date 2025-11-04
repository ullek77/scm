<!DOCTYPE html>
<html lang='en'>
<head>
<title>hyprpolkitagent.spec - solopasha/hyprland/hyprpolkitagent.git - [no description]</title>
<meta name='generator' content='cgit '/>
<meta name='robots' content='index, nofollow'/>
<link rel='stylesheet' type='text/css' href='/cgit-data/cgit.css'/>
<link rel='shortcut icon' href='/favicon.ico'/>
<link rel='alternate' title='Atom feed' href='http://copr-dist-git.fedorainfracloud.org/packages/solopasha/hyprland/hyprpolkitagent.git/atom/hyprpolkitagent.spec?h=master' type='application/atom+xml'/>
<link rel='vcs-git' href='http://copr-dist-git.fedorainfracloud.org/git/solopasha/hyprland/hyprpolkitagent.git' title='solopasha/hyprland/hyprpolkitagent.git Git repository'/>
</head>
<body>
<div id='cgit'><table id='header'>
<tr>
<td class='logo' rowspan='2'><a href='/packages/'><img src='/cgit-data/cgit.png' alt='cgit logo'/></a></td>
<td class='main'><a href='/packages/'>index</a> : <a title='solopasha/hyprland/hyprpolkitagent.git' href='/packages/solopasha/hyprland/hyprpolkitagent.git/'>solopasha/hyprland/hyprpolkitagent.git</a></td><td class='form'><form method='get'>
<select name='h' onchange='this.form.submit();'>
<option value='f40'>f40</option>
<option value='f41'>f41</option>
<option value='f42'>f42</option>
<option value='master' selected='selected'>master</option>
</select> <input type='submit' value='switch'/></form></td></tr>
<tr><td class='sub'>[no description]</td><td class='sub right'></td></tr></table>
<table class='tabs'><tr><td>
<a href='/packages/solopasha/hyprland/hyprpolkitagent.git/'>summary</a><a href='/packages/solopasha/hyprland/hyprpolkitagent.git/refs/'>refs</a><a href='/packages/solopasha/hyprland/hyprpolkitagent.git/log/hyprpolkitagent.spec'>log</a><a class='active' href='/packages/solopasha/hyprland/hyprpolkitagent.git/tree/hyprpolkitagent.spec'>tree</a><a href='/packages/solopasha/hyprland/hyprpolkitagent.git/commit/hyprpolkitagent.spec'>commit</a><a href='/packages/solopasha/hyprland/hyprpolkitagent.git/diff/hyprpolkitagent.spec'>diff</a><a href='/packages/solopasha/hyprland/hyprpolkitagent.git/stats/hyprpolkitagent.spec'>stats</a></td><td class='form'><form class='right' method='get' action='/packages/solopasha/hyprland/hyprpolkitagent.git/log/hyprpolkitagent.spec'>
<select name='qt'>
<option value='grep'>log msg</option>
<option value='author'>author</option>
<option value='committer'>committer</option>
<option value='range'>range</option>
</select>
<input class='txt' type='search' size='10' name='q' value=''/>
<input type='submit' value='search'/>
</form>
</td></tr></table>
<div class='path'>path: <a href='/packages/solopasha/hyprland/hyprpolkitagent.git/tree/'>root</a>/<a href='/packages/solopasha/hyprland/hyprpolkitagent.git/tree/hyprpolkitagent.spec'>hyprpolkitagent.spec</a></div><div class='content'>blob: 665dfd15243bc14611b2f077e2b9aaa85fbd8e2a (<a href='/packages/solopasha/hyprland/hyprpolkitagent.git/plain/hyprpolkitagent.spec'>plain</a>)
<table summary='blob content' class='blob'>
<tr><td class='linenumbers'><pre><a id='n1' href='#n1'>1</a>
<a id='n2' href='#n2'>2</a>
<a id='n3' href='#n3'>3</a>
<a id='n4' href='#n4'>4</a>
<a id='n5' href='#n5'>5</a>
<a id='n6' href='#n6'>6</a>
<a id='n7' href='#n7'>7</a>
<a id='n8' href='#n8'>8</a>
<a id='n9' href='#n9'>9</a>
<a id='n10' href='#n10'>10</a>
<a id='n11' href='#n11'>11</a>
<a id='n12' href='#n12'>12</a>
<a id='n13' href='#n13'>13</a>
<a id='n14' href='#n14'>14</a>
<a id='n15' href='#n15'>15</a>
<a id='n16' href='#n16'>16</a>
<a id='n17' href='#n17'>17</a>
<a id='n18' href='#n18'>18</a>
<a id='n19' href='#n19'>19</a>
<a id='n20' href='#n20'>20</a>
<a id='n21' href='#n21'>21</a>
<a id='n22' href='#n22'>22</a>
<a id='n23' href='#n23'>23</a>
<a id='n24' href='#n24'>24</a>
<a id='n25' href='#n25'>25</a>
<a id='n26' href='#n26'>26</a>
<a id='n27' href='#n27'>27</a>
<a id='n28' href='#n28'>28</a>
<a id='n29' href='#n29'>29</a>
<a id='n30' href='#n30'>30</a>
<a id='n31' href='#n31'>31</a>
<a id='n32' href='#n32'>32</a>
<a id='n33' href='#n33'>33</a>
<a id='n34' href='#n34'>34</a>
<a id='n35' href='#n35'>35</a>
<a id='n36' href='#n36'>36</a>
<a id='n37' href='#n37'>37</a>
<a id='n38' href='#n38'>38</a>
<a id='n39' href='#n39'>39</a>
<a id='n40' href='#n40'>40</a>
<a id='n41' href='#n41'>41</a>
<a id='n42' href='#n42'>42</a>
<a id='n43' href='#n43'>43</a>
<a id='n44' href='#n44'>44</a>
<a id='n45' href='#n45'>45</a>
<a id='n46' href='#n46'>46</a>
<a id='n47' href='#n47'>47</a>
<a id='n48' href='#n48'>48</a>
<a id='n49' href='#n49'>49</a>
<a id='n50' href='#n50'>50</a>
<a id='n51' href='#n51'>51</a>
<a id='n52' href='#n52'>52</a>
<a id='n53' href='#n53'>53</a>
</pre></td>
<td class='lines'><pre><code><span class="hl kwa">Name</span><span class="hl opt">:</span>           hyprpolkitagent
<span class="hl kwa">Version</span><span class="hl opt">:</span>        <span class="hl num">0.1.3</span>
<span class="hl kwa">Release</span><span class="hl opt">:</span>        <span class="hl kwb">%autorelease</span>
<span class="hl kwa">Summary</span><span class="hl opt">:</span>        A simple polkit authentication agent <span class="hl kwa">for</span> Hyprland
<span class="hl kwa">License</span><span class="hl opt">:</span>        BSD<span class="hl opt">-</span><span class="hl num">3</span><span class="hl opt">-</span>Clause
<span class="hl kwa">URL</span><span class="hl opt">:</span>            https<span class="hl opt">://</span>github.com<span class="hl opt">/</span>hyprwm<span class="hl opt">/</span>hyprpolkitagent
<span class="hl kwa">Source</span><span class="hl opt">:</span>         <span class="hl kwc">%{url}/archive/v%{version}/%{name}-%{version}</span>.tar.gz

<span class="hl slc"># https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval</span>
<span class="hl kwa">ExcludeArch</span><span class="hl opt">:</span>    <span class="hl kwc">%{ix86}</span>

BuildRequires<span class="hl opt">:</span>  cmake
BuildRequires<span class="hl opt">:</span>  desktop<span class="hl opt">-</span>file<span class="hl opt">-</span>utils
BuildRequires<span class="hl opt">:</span>  gcc<span class="hl opt">-</span>c<span class="hl opt">++</span>
BuildRequires<span class="hl opt">:</span>  systemd<span class="hl opt">-</span>rpm<span class="hl opt">-</span>macros

BuildRequires<span class="hl opt">:</span>  cmake<span class="hl opt">(</span>Qt6Quick<span class="hl opt">)</span>
BuildRequires<span class="hl opt">:</span>  cmake<span class="hl opt">(</span>Qt6QuickControls2<span class="hl opt">)</span>
BuildRequires<span class="hl opt">:</span>  cmake<span class="hl opt">(</span>Qt6Widgets<span class="hl opt">)</span>
BuildRequires<span class="hl opt">:</span>  pkgconfig<span class="hl opt">(</span>hyprutils<span class="hl opt">)</span>
BuildRequires<span class="hl opt">:</span>  pkgconfig<span class="hl opt">(</span>polkit<span class="hl opt">-</span>agent<span class="hl opt">-</span><span class="hl num">1</span><span class="hl opt">)</span>
BuildRequires<span class="hl opt">:</span>  pkgconfig<span class="hl opt">(</span>polkit<span class="hl opt">-</span>qt6<span class="hl opt">-</span><span class="hl num">1</span><span class="hl opt">)</span>

<span class="hl kwa">Requires</span><span class="hl opt">:</span>       hyprland<span class="hl opt">-</span>qt<span class="hl opt">-</span>support<span class="hl kwc">%{?_isa}</span>

<span class="hl kwb">%description</span>
A simple polkit authentication agent <span class="hl kwa">for</span> Hyprland<span class="hl opt">,</span> written <span class="hl kwa">in</span> QT<span class="hl opt">/</span>QML.

<span class="hl kwb">%prep</span>
<span class="hl kwb">%autosetup</span> <span class="hl opt">-</span>p1

<span class="hl kwb">%build</span>
<span class="hl kwb">%cmake</span>
<span class="hl kwb">%cmake_build</span>

<span class="hl kwb">%install</span>
<span class="hl kwb">%cmake_install</span>

<span class="hl kwb">%post</span>
<span class="hl kwb">%systemd_user_post</span> <span class="hl kwc">%{name}</span>.service

<span class="hl kwb">%preun</span>
<span class="hl kwb">%systemd_user_preun</span> <span class="hl kwc">%{name}</span>.service

<span class="hl kwb">%files</span>
<span class="hl kwb">%license</span> LICENSE
<span class="hl kwb">%doc</span> README.md
<span class="hl kwc">%{_datadir}/dbus-1/services/org.hyprland.%{name}</span>.service
<span class="hl kwc">%{_libexecdir}/%{name}</span>
<span class="hl kwc">%{_userunitdir}/%{name}</span>.service

<span class="hl kwb">%changelog</span>
<span class="hl kwb">%autochangelog</span>
</code></pre></td></tr></table>
</div> <!-- class=content -->
<div class='footer'>generated by <a href='https://git.zx2c4.com/cgit/about/'>cgit </a> (<a href='https://git-scm.com/'>git 2.34.1</a>) at 2025-11-04 19:05:41 +0000</div>
</div> <!-- id=cgit -->
</body>
</html>
