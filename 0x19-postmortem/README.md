# 🛠️ Web Stack Debugging Project Postmortem

## 📋 Issue Summary

**Duration of Outage**:  
Start: June 20, 2024, 14:00 UTC  
End: June 20, 2024, 15:30 UTC

**Impact**:  
During the outage, 75% of our users experienced slow load times and 50% faced complete service unavailability on our web application. Users reported issues with logging in, loading content, and making transactions.

**Root Cause**:  
The root cause was a misconfiguration in our load balancer which led to an uneven distribution of traffic, overwhelming a subset of our servers while leaving others underutilized.

---

## 🕒 Timeline

- **14:00 UTC** - Issue detected by monitoring alert indicating high response times and error rates.
- **14:05 UTC** - Initial investigation by on-call engineer, confirmed by user reports on social media.
- **14:15 UTC** - Assumption that the database was under heavy load, investigation into database performance.
- **14:30 UTC** - Database ruled out, shifted focus to application servers and network components.
- **14:45 UTC** - Load balancer misconfiguration suspected, but initially dismissed due to recent update.
- **15:00 UTC** - Escalated to senior network engineer for further analysis.
- **15:15 UTC** - Confirmed load balancer misconfiguration, applied correct settings.
- **15:30 UTC** - Service fully restored, monitoring confirms normal operation.

---

## 🔍 Root Cause and Resolution

**Root Cause**:  
The load balancer had an incorrect setting for traffic distribution that caused it to send the majority of traffic to a small subset of servers. This resulted in those servers being overwhelmed while others remained idle, causing significant delays and outages for users.

**Resolution**:  
The load balancer configuration was corrected to ensure even traffic distribution across all servers. Once the correct settings were applied, the traffic normalized, and server loads balanced out, restoring normal service.

---

## 🚀 Corrective and Preventative Measures

**Improvements**:  
1. **Review and update load balancer configuration policies**: Ensure settings are regularly audited and verified, especially after updates.
2. **Enhanced Monitoring**: Implement more granular monitoring and alerting for load balancer traffic patterns.
3. **Disaster Recovery Drills**: Conduct regular drills to simulate load balancer failures and response protocols.

**Tasks**:
- [ ] Patch and update Nginx server configurations.
- [ ] Add specific monitoring for load balancer traffic and server utilization.
- [ ] Schedule monthly configuration audits for all critical infrastructure components.
- [ ] Develop and implement a runbook for load balancer failure scenarios.

---

## 🎨 Making It Engaging

We are constantly stormed by a quantity of information, it’s tough to get people to read you. Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience's attention.

### Humour
Imagine our servers were like a coffee shop:

- **Database**: The barista making coffee (no overload here, just brewing fine).
- **Application Servers**: Tables where customers sit (some were overcrowded, others empty).
- **Load Balancer**: The server assigning tables, but decided everyone should cram into one corner of the cafe!

### Diagram
![Server Load Diagram](https://github.com/your-repo/link-to-diagram)

### Positive Note
Remember, every challenge is an opportunity to learn and improve! 🌟

![Stay Positive](https://github.com/your-repo/link-to-positive-image) 😊

---

Thank you for your attention to this postmortem. We are committed to learning from these incidents to continuously improve our systems and services.
