# Linux Virtual Machine Configuration

## 1. VM Specifications
- Environment: Kali GNU/Linux Rolling 2026.1 (WSL2 x86_64)
- CPU: Intel Core i5-10400F (8 vCPUs)
- Memory: 15 GiB RAM
- Storage: 1007 GB (/dev/sdd)
- Network: Isolated Private Lab Network (172.25.222.233/20)
- Snapshot: before-project (12/11/2026)

## 2. Named Accounts and Permissions
- halim (Student 1): halim, users, docker (No sudo)
- yazan (Student 2): yazan, sudo, users (Admin sudo enabled)
- moayad (Student 3): moayad, users, docker (No sudo)
- deploy (Deployment Account): deploy, users, docker (No sudo, owns /opt/devops-project)

## 3. Firewall Rules (sudo ufw status numbered)
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] 22/tcp                     ALLOW IN    Anywhere                  
[ 2] 8000/tcp                   ALLOW IN    Anywhere                  
[ 3] 22/tcp (v6)                ALLOW IN    Anywhere (v6)             
[ 4] 8000/tcp (v6)              ALLOW IN    Anywhere (v6)             


## 4. Connectivity Check
=== Connectivity Check to VM (172.25.222.233) ===
PING 172.25.222.233 (172.25.222.233) 56(84) bytes of data.
64 bytes from 172.25.222.233: icmp_seq=1 ttl=64 time=0.080 ms
64 bytes from 172.25.222.233: icmp_seq=2 ttl=64 time=0.029 ms
64 bytes from 172.25.222.233: icmp_seq=3 ttl=64 time=0.035 ms

--- 172.25.222.233 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2032ms
rtt min/avg/max/mdev = 0.029/0.048/0.080/0.022 ms
172.25.222.233: inverse host lookup failed: Unknown host
(UNKNOWN) [172.25.222.233] 22 (ssh) open
