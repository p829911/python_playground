#! /bin/bash

# Program to output a system information page

TITLE="System Information Report For $HOSTNAME"
CURRENT_TIME=$(date +"%x %r %Z")
TIME_STAMP="Generated $CURRENT_TIME, by $USER"

report_uptime() {
    cat <<-EOF
            <H2>System Uptime</H2>
            <PRE>$(uptime)</PRE>
EOF
    return
}

report_disk_space() {
    cat <<-EOF
            <H2>Disk Space Utilization</H2>
            <PRE>$(df -h)</PRE>
EOF
    return
}

report_home_space() {
    cat <<-EOF
            <H2>Home Space Utilization</H2>
            <PRE>$(du -sh /home/*)</PRE>
EOF
    return
}

cat <<_EOF_
<HTML>
    <HEAD>
        <TITLE>$TITLE</TITLE>
    </HEAD>
    <BODY>
        <H1>$TITLE</H1>
        <P>$TIME_STAMP</P>
        $(report_uptime)
        $(report_disk_space)
        $(report_home_space)
    </BODY>
</HTML>
_EOF_
