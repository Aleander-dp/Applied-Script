#!/bin/bash
#
# Detta script samlar in systeminformation - RECON
#
#
# Author: Alexander Dolk Persson
# Last Update: 2026-01-04


echo "Välkommen till RECON script för att kontrollera en Linux-miljö"

echo
echo "=== SYSTEMINFO ==="
uname -a

echo
echo "=== AKTUELL ANVÄNDARE ==="
echo $USER

echo
echo "=== ANVÄNDARE MED SHELL ==="
grep "sh$" /etc/passwd

echo
echo "=== NÄTVERK ==="
ip a | grep inet

echo
echo "=== LÄGG TILL FLERA TESTER  ==="
echo "Detta är ett test"
date
uptime

