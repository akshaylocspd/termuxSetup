def extract_substring(input_str):
    extracted_str = ""
    lines = input_str.split("\n")
    for line in lines:
        if "deb" in line and ("main" in line or "root" in line or "x11" in line):
            extracted_str += " ".join(line.split()[1:]) + "\n"
    return extracted_str

# Input the string
input_str = """
Main	deb https://packages.termux.dev/apt/termux-main stable main
Root	deb https://packages.termux.dev/apt/termux-root root stable
X11	deb https://packages.termux.dev/apt/termux-x11 x11 main

Main	deb https://packages-cf.termux.dev/apt/termux-main stable main
Root	deb https://packages-cf.termux.dev/apt/termux-root root stable
X11	deb https://packages-cf.termux.dev/apt/termux-x11 x11 main

Main	deb https://termux.mentality.rip/termux-main stable main
Root	deb https://termux.mentality.rip/termux-root root stable
X11	deb https://termux.mentality.rip/termux-x11 x11 main

Main	deb https://md.mirrors.hacktegic.com/termux/termux-main stable main
Root	deb https://md.mirrors.hacktegic.com/termux/termux-root root stable
X11	deb https://md.mirrors.hacktegic.com/termux/termux-x11 x11 main

Main	deb https://termux.astra.in.ua/apt/termux-main stable main
Root	deb https://termux.astra.in.ua/apt/termux-root root stable
X11	deb https://termux.astra.in.ua/apt/termux-x11 x11 main

Main	deb https://mirror.textcord.xyz/termux/termux-main stable main
Root	deb https://mirror.textcord.xyz/termux/termux-root root stable
X11	deb https://mirror.textcord.xyz/termux/termux-x11 x11 main

Main	deb https://linux.domainesia.com/applications/termux/termux-main stable main
Root	deb https://linux.domainesia.com/applications/termux/root root stable
X11	deb https://linux.domainesia.com/applications/termux/x11 x11 main

Main	deb https://grimler.se/termux/termux-main stable main
Root	deb https://grimler.se/termux/termux-root root stable
X11	deb https://grimler.se/termux/termux-x11 x11 main

Main	deb https://termux.librehat.com/apt/termux-main stable main
Root	deb https://termux.librehat.com/apt/termux-root root stable
X11	deb https://termux.librehat.com/apt/termux-x11 x11 main

Main	deb https://mirror.mwt.me/termux/main stable main
Root	deb https://mirror.mwt.me/termux/root root stable
X11	deb https://mirror.mwt.me/termux/x11 x11 main

Main	deb https://mirror.nevacloud.com/applications/termux/termux-main stable main
Root	deb https://mirror.nevacloud.com/applications/termux/root root stable
X11	deb https://mirror.nevacloud.com/applications/termux/x11 x11 main

Main	deb https://plug-mirror.rcac.purdue.edu/termux/termux-main stable main
Root	deb https://plug-mirror.rcac.purdue.edu/termux/termux-root root stable
X11	deb https://plug-mirror.rcac.purdue.edu/termux/termux-x11 x11 main

Main	deb https://mirror.csclub.uwaterloo.ca/termux/termux-main stable main
Root	deb https://mirror.csclub.uwaterloo.ca/termux/termux-root root stable
X11	deb https://mirror.csclub.uwaterloo.ca/termux/termux-x11 x11 main

Main	deb https://mirrors.sahilister.in/termux/termux-main stable main
Root	deb https://mirrors.sahilister.in/termux/termux-root root stable
X11	deb https://mirrors.sahilister.in/termux/termux-x11 x11 main

Main	deb https://mirrors.utermux.dev/termux/termux-main stable main
Root	deb https://mirrors.utermux.dev/termux/termux-root root stable
X11	deb https://mirrors.utermux.dev/termux/termux-x11 x11 main

Main	deb https://mirror.vern.cc/termux/termux-main stable main
Root	deb https://mirror.vern.cc/termux/termux-root root stable
X11	deb https://mirror.vern.cc/termux/termux-x11 x11 main

Main	deb https://mirror.fcix.net/termux/termux-main stable main
Root	deb https://mirror.fcix.net/termux/termux-root root stable
X11	deb https://mirror.fcix.net/termux/termux-x11 x11 main

Main	deb https://mirrors.cbrx.io/apt/termux/termux-main stable main
Root	deb https://mirrors.cbrx.io/apt/termux/termux-root root stable
X11	deb https://mirrors.cbrx.io/apt/termux/termux-x11 x11 main

Main	deb https://termux.3san.dev/termux/termux-main stable main
Root	deb https://termux.3san.dev/termux/termux-root root stable
X11	deb https://termux.3san.dev/termux/termux-x11 x11 main

Main	deb https://cdn.lumito.net/termux/termux-main stable main
Root	deb https://cdn.lumito.net/termux/termux-root root stable
X11	deb https://cdn.lumito.net/termux/termux-x11 x11 main

Main	deb https://mirrors.wale.id.au/termux/termux-main stable main
Root	deb https://mirrors.wale.id.au/termux/termux-root root stable
X11	deb https://mirrors.wale.id.au/termux/termux-x11 x11 main

Main	deb https://ftp.fau.de/termux/termux-main stable main
Root	deb https://ftp.fau.de/termux/termux-root root stable
X11	deb https://ftp.fau.de/termux/termux-x11 x11 main

Main	deb https://packages.nscdn.top/termux-main stable main
Root	deb https://packages.nscdn.top/termux-root root stable
X11	deb https://packages.nscdn.top/termux-x11 x11 main

Main	deb https://mirror.albony.xyz/termux/termux-main stable main
Root	deb https://mirror.albony.xyz/termux/termux-root root stable
X11	deb https://mirror.albony.xyz/termux/termux-x11 x11 main

Main	deb http://mirror.mephi.ru/termux/termux-main stable main
Root	deb http://mirror.mephi.ru/termux/termux-root root stable
X11	deb http://mirror.mephi.ru/termux/termux-x11 x11 main

Main	deb https://mirror.surf/termux/termux-main stable main
Root	deb https://mirror.surf/termux/termux-root root stable
X11	deb https://mirror.surf/termux/termux-x11 x11 main

Main	deb https://mirror.bardia.tech/termux/termux-packages-24 stable main
Root	deb https://mirror.bardia.tech/termux/termux-root-packages-24 root stable
X11	deb https://mirror.bardia.tech/termux/x11-packages x11 main

Main	deb https://mirrors.bfsu.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirrors.bfsu.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirrors.bfsu.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirrors.cqupt.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirrors.cqupt.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirrors.cqupt.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirrors.dgut.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirrors.dgut.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirrors.dgut.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirrors.hit.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirrors.hit.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirrors.hit.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirrors.njupt.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirrors.njupt.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirrors.njupt.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirror.nyist.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirror.nyist.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirror.nyist.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirror.nju.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirror.nju.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirror.nju.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirrors.sdu.edu.cn/termux/termux-main stable main
Root	deb https://mirrors.sdu.edu.cn/termux/termux-root root stable
X11	deb https://mirrors.sdu.edu.cn/termux/termux-x11 x11 main

Main	deb https://mirrors.sau.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirrors.sau.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirrors.sau.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirrors.scau.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirrors.scau.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirrors.scau.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirrors.sustech.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirrors.sustech.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirrors.sustech.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main
Root	deb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-root root stable
X11	deb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-x11 x11 main

Main	deb https://mirrors.pku.edu.cn/termux/termux-main/ stable main
Root	deb https://mirrors.pku.edu.cn/termux/termux-root/ root stable
X11	deb https://mirrors.pku.edu.cn/termux/termux-x11/ x11 main

Main	deb https://mirrors.ustc.edu.cn/termux/apt/termux-main/ stable main
Root	deb https://mirrors.ustc.edu.cn/termux/apt/termux-root/ root stable
X11	deb https://mirrors.ustc.edu.cn/termux/apt/termux-x11/ x11 main

Main	deb https://mirrors.zju.edu.cn/termux/apt/termux-main/ stable main
Root	deb https://mirrors.zju.edu.cn/termux/apt/termux-root/ root stable
X11	deb https://mirrors.zju.edu.cn/termux/apt/termux-x11/ x11 main

Main	deb https://mirrors.aliyun.com/termux/termux-packages-24 stable main
Root	deb https://mirrors.aliyun.com/termux/termux-root-packages-24 root stable
X11	deb https://mirrors.aliyun.com/termux/x11-packages x11 main

Main	deb https://mirror.iscas.ac.cn/termux/apt/termux-main/ stable main
Root	deb https://mirror.iscas.ac.cn/termux/apt/termux-root/ root stable
X11	deb https://mirror.iscas.ac.cn/termux/apt/termux-x11/ x11 main
"""

# Call the function to extract the substring
output_str = extract_substring(input_str)

print("Extracted substring:")
print(output_str)
