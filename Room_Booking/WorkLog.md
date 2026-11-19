# 📓 Project Work Log: Room Booking

---

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
