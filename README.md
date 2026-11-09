# Cloud Encryption & Cryptographic Posture Auditor

<p align="center">
  <img src="https://img.shields.io/badge/Security-Defensive_Auditor-blue?style=flat" alt="Type">
  <img src="https://img.shields.io/badge/Status-Architectural_Showcase-success?style=flat" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
</p>

> 🔒 **Technical Showcase & Architecture Specification**  
> *This repository provides public architectural documentation, system specifications, and implementation summaries. Full production source code, internal test suites, and proprietary algorithms are maintained in a secure private repository.*

---

## 📌 Executive Summary

**Category**: Cloud Security & Cryptography  
**Tech Stack**: `Python 3.10+ · AWS KMS · Encryption Standards · Compliance Auditing`  

Automated security posture tool auditing at-rest and in-transit encryption standards across cloud storage, databases, and message queues.

---

## 🎯 The Problem It Solves

Modern regulatory frameworks (GDPR, HIPAA, PCI-DSS) mandate pervasive encryption. Cloud services often default to unencrypted or provider-managed keys without rotation, risking data exposure in multi-tenant environments.

---

## ⚙️ How the Engine Works

1. **Resource Inventory Parsing**: Analyzes configuration snapshots of S3 buckets, EBS volumes, RDS instances, and SQS queues.
2. **Cryptographic Algorithm Check**: Verifies that active encryption uses sanctioned ciphers (e.g., AES-256) and flags legacy or deprecated algorithms.
3. **Key Ownership Analysis**: Differentiates between default AWS-owned keys, AWS-managed KMS keys, and Customer-Managed Keys (CMKs) to enforce separation of duties.
4. **In-Transit TLS Enforcement**: Checks bucket policies and API gateway configs for explicit `aws:SecureTransport` deny rules to block non-TLS traffic.
5. **Compliance Scoring**: Outputs non-compliant assets ranked by data sensitivity and regulatory risk.

---

## 🚀 Key Capabilities

- Audits S3 default encryption and bucket policy TLS enforcement
- Verifies EBS volume snapshot encryption and RDS storage configurations
- Flags missing customer-managed KMS key rotations
- Generates gap-analysis reports for compliance frameworks

---

## 🏗️ System Data Flow & Architecture

```
+-----------------------------------+
|  Target Input / Configuration    |
|  (JSON Snapshots / Policies)      |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  1. Schema Normalization Engine   |
|  Validates types & formats        |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  2. Core Analytical Pipeline      |
|  Heuristic rule evaluation,       |
|  invariant checks & drift diffs   |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  3. Risk Classification           |
|  Assigns severity: INFO / HIGH    |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  4. Structured Findings & Report  |
|  Root cause, evidence &           |
|  actionable remediation steps     |
+-----------------------------------+
```

---

## 📄 Findings Output Structure

The engine generates structured, machine-parsable JSON reports adhering to this standard audit schema:

```json
{
  "results": [
    {
      "resource": "resource-identifier",
      "severity": "HIGH",
      "check": "CHECK_IDENTIFIER",
      "detail": "Descriptive analysis of the identified security posture issue.",
      "remediation": "Actionable step-by-step guidance to restore compliant state.",
      "evidence": {
        "observed_field": "value",
        "required_policy": "enforced_policy"
      }
    }
  ],
  "count": 1,
  "scope": "Comprehensive defensive security audit"
}
```

---

## 🔒 Source Code & Enterprise Inquiries

To protect proprietary intellectual property and client operational security:
* **Public Repository**: Contains comprehensive architecture specifications, schemas, and design overviews.
* **Private Repository**: Contains the complete production implementation, continuous integration pipelines, and full regression test suites.

For architectural questions or enterprise inquiries, connect via [LinkedIn](https://www.linkedin.com/in/karthikeyansubramaniam04/) or visit the [Portfolio Site](https://karthikeyansubramaniyam.github.io).
