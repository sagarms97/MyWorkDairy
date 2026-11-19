# 📓 Project Work Log: Staff Establishment (HR Module)

---

## 📅 18-11-2026

### 🔹 Task 1: Capture Voter ID and Address Details in Staff Master
- **Table / Schema**: `[dbo].[ESTB_StaffDetails]`
- **Requirement**: Enable staff records to store Voter ID numbers and corresponding registered addresses.
- **Solution / Implementation**: Added two new database columns and integrated front-end textboxes bound across `INSERT`, `UPDATE`, and `SELECT` query procedures:
  ```sql
  ALTER TABLE [dbo].[ESTB_StaffDetails]
  ADD [VoterID] VARCHAR(50) NULL,
      [AddressOnVoterID] VARCHAR(500) NULL;
  ```
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

<br/>

## 📅 03-11-2026

### 🔹 Task 1: Provide Option to Delete Uploaded Document
- **Page**: Document Management / HR Module
- **Requirement**: Allow users to delete specific uploaded documents.
- **Solution / Progress**: Implemented a `LinkButton` action to handle document removal.
- **Blocker / Reason**: Project publish failed due to build configuration issues.
- **Status**: ![](https://img.shields.io/badge/Status-Pending-yellow?style=flat-square)

---

<br/>

## 📅 02-11-2026

### 🔹 Task 1: Increase Document Upload Limit to Minimum 10 MB
- **Page / Config**: `web.config`
- **Requirement**: Enable upload support for larger employee documents (at least 10 MB).
- **Solution**: Updated `maxRequestLength` and `maxAllowedContentLength` parameters in `web.config`.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---
