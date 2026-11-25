# 📓 Project Work Log: Room Booking

---

## 📅 25-11-2026

### 🔹 Task 1: Resolve Amount Discrepancy in Reconciliation Report
- **Page / Report**: Financial / Reconciliation Report
- **Issue**: Reconciliation report was displaying inaccurate totals and discrepancy amounts.
- **Solution / Resolution**: Reviewed the backend aggregation logic and formula calculations; corrected the amount computation scripts to ensure reconciled values match actual transaction amounts accurately.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 2: Correct Print Layout Alignment in Portrait Orientation
- **Scope**: Print View / Document Export
- **Issue**: Print output was overflowing margins or misaligned when printing in portrait orientation.
- **Solution / Resolution**: Adjusted layout scaling percentage under print settings/CSS so that all columns and table elements fit cleanly within the standard portrait print window.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 3: Fix Webcam Capture Functionality
- **Scope**: Guest Photo Capture / Front Desk Module
- **Issue**: Webcam interface failed to initialize or trigger camera feed for guest photo capture.
- **Solution / Resolution**: Deployed the missing `webcam.js` library file directly into the published production web application assets directory.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

### 🔹 Task 4: Fix Rent Calculation / Multiplication Bug for Dormitory Rooms
- **Page / Module**: Room Booking / Tariff Calculation Engine
- **Issue**: Dormitory bookings were incorrectly multiplying or calculating rental charges upon reservation.
- **Solution / Resolution**: Updated the rate calculation code in the Room Booking page to evaluate dormitory per-bed tariff logic properly without compounding multipliers.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

<br/>

## 📅 19-11-2026

### 🔹 Task 1: Cancel Erroneous Checkout Receipt for Guest (Irranna)
- **Scope**: Front Desk / Room Reservation
- **Issue**: BTM user inadvertently checked out guest "Irranna", who is currently still residing at the property.
- **Solution / Resolution**: Authenticated via administrative privileges and deleted the premature checkout receipt, successfully restoring the guest's active check-in record.
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

<br/>

## 📅 18-11-2026

### 🔹 Task 1: Display Children Count and Refundable Amount on Booking Reports
- **Table / Config**: `[ht_ReportFormats]` (Template ID: `10`)
- **Requirement**: Show both adult and children headcounts together, and display refundable portion alongside the deposit amount in generated booking reports.
- **Solution / Implementation**: Updated the HTML report layout template in `[ht_ReportFormats]` using string placeholders to render children count beside adults and refundable amount beside deposit:
  ```sql
  UPDATE [ht_ReportFormats]
  SET ReportContent = REPLACE(
      REPLACE(
          ReportContent,
          '<td><strong>{{NoAdults}}</strong></td>',
          '<td><strong>{{NoAdults}}</strong> &nbsp;(Children: <strong>{{NoChildrens}}</strong>)</td>'
      ),
      '<td><strong> {{DepositAmount}} </strong></td>',
      '<td><strong>{{DepositAmount}}</strong> &nbsp;(Refundable: <strong>{{RefundAmount}}</strong>)</td>'
  )
  WHERE id = 10;
  ```
- **Status**: ![](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---
