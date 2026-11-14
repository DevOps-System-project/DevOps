# Project Risk Register

| Risk ID | Date Logged | Category | Description | Likelihood | Impact | Mitigation / Action Plan | Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RISK-001** | 14/11/2026 | Network / Security | UFW rules on the Linux VM currently allow `22/tcp` (SSH) and `8000/tcp` (App) from `Anywhere` (`0.0.0.0/0` and `::/0`) rather than restricting ingress strictly to the isolated lab subnet (`172.25.208.0/20`). | Low (VM is behind NATed WSL2 virtual switch) | Medium | Keep VM isolated on local host-only virtual switch during lab exercises; restrict SSH rule via `sudo ufw allow from 172.25.208.0/20 to any port 22 proto tcp` if VM stays in long-term use. | Student 2 (`yazan`) | Monitored / Mitigated by NAT |
