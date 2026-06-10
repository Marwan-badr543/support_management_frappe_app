# Support Management

Manage all stages of customer support issues in one place with a multi-level workflow — from Customer Service to Technician to Maintenance Technician — built on Frappe/ERPNext.

## Features

- **Multi-stage workflow** — Issues move through states: Draft → Customer Service → Technician → Maint Tech → Closed (with Reject/Reopen)
- **Auto-creation of sub-documents** — Tech and Maintenance Tech issue documents are created automatically as the workflow progresses
- **Custom fields on Issue** — Add item code, serial number, report, visit date/time, technician assignment, and address directly on the standard Issue doctype
- **Maintenance Visit integration** — Create ERPNext Maintenance Visits from Tech issues with one click
- **Role-based permissions** — Row-level access control for Technicians and Maintenance Technicians
- **Auto-setup on install** — Role Profiles (Technician, Maintenance Technician) are created automatically
- **Serial number filtering** — Filter serial numbers by item code and "Delivered" status on the Issue form

## Workflow

```
Draft → Customer Service → Technician → Maint Tech → Closed
                                                    ↘ Rejected
```

1. **Customer Service** — Agent receives the issue, fills in a report, and assigns a Technician
2. **Technician** — Visits the customer, inspects the item, fills a report. Can escalate to Maint Tech or Close
3. **Maint Tech** — Handles pickup, repair, and return. Can create a Maintenance Visit in ERPNext

## Doctypes

| Doctype | Purpose |
|---|---|
| **CS Support Issue** | Customer Service issue tracking (subject, customer, status, priority, description, report) |
| **Tech Supprot Issue** | Technician-level issue (visit info, pickup info, item/serial details, maintenance tech assignment) |
| **Maint Tech Supprot Issue** | Maintenance technician issue (pickup info, description, report) |

## Installation

### Prerequisites

- Frappe Bench (v15+)
- ERPNext installed on your site

### Steps

```bash
# Navigate to your bench directory
cd ~/frappe/bench

# Get the app
bench get-app https://github.com/Marwan-badr543/support_management_frappe_app

# Install the app on your site
bench --site your-site.com install-app support_management
```

After installation, the app will:
- Add custom fields to the **Issue** doctype (Item Code, Serial Number, Report, Technician, Visit Date/Time, Address, etc.)
- Add a custom field to **Maintenance Visit** (`custom_tech_issue`)
- Create 3 workflows: `supprot managemtn`, `tech`, and `maint tech`
- Create **Role Profiles**: Technician and Maintenance Technician
- Add the **Workflow State** values: Draft, Closed, Technician, Customer Service, Maint Tech, Rejected

## Usage

### 1. Create an Issue

Create a new **Issue** record. The available fields include:
- **Item Code** — Link to Item
- **Serial Number** — Filtered by selected item (only "Delivered" serials shown)
- **Report** — Customer service agent's report
- **Visit Date / Visit Time** — Scheduled tech visit
- **Technician** — Assigned technician (User)
- **Address** — Customer address for the visit

### 2. Move through the workflow

- **Draft → Customer Service** — Fill in your Report and transition
- **Customer Service → Technician** — Fill in Item Code, Serial Number, Technician, Visit Date/Time, Address
- **Technician → Maint Tech** — Fill in Description, Report, Maintenance Technician, Pickup Date/Time
- **Technician → Closed** — If the issue is resolved on-site
- **Maint Tech → Closed** — Create a Maintenance Visit to record the work done

### 3. Create a Maintenance Visit (Tech)

On the **Tech Supprot Issue** form, click **Create Maintenance Visit** — this generates an ERPNext Maintenance Visit with the item, serial number, report, and customer details pre-filled.

## Permissions

| Role | Access |
|---|---|
| **System Manager** | Full access to all doctypes |
| **Customer Service** | Create/Read/Write/Delete on CS Support Issue |
| **Technician** | Read/Write on Tech Supprot Issue (scoped to assigned technician) |
| **Maintenance Technician User** | Read/Write on Maint Tech Supprot Issue (scoped to assigned maint tech) |

## Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/support_management
pre-commit install
```

Pre-commit is configured to use the following tools:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app uses GitHub Actions for CI:

- **CI** — Installs the app and runs unit tests on every push to `main`
- **Linters** — Runs Frappe Semgrep Rules and pip-audit on every pull request

## License

MIT
