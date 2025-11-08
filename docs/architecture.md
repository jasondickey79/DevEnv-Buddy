#  DevEnv-Buddy Architecture Diagram

This diagram shows the flow of components in the **DevEnv-Buddy** system — from reading environment configurations to running tests, notifying users, and integrating with CI/CD pipelines.

---

```mermaid
flowchart TD
    A["YAML Config File"] --> B["Config Loader (PyYAML)"]
    B --> C["Environment Manager (Docker Compose)"]
    C --> D["Test Runner (HTTP/Integration Checks)"]
    C --> E["Notifier (Slack/Webhook)"]
    D --> F["CI/CD Pipeline (GitHub Actions)"]
    E --> F
    F --> G["Developer Feedback & Logs"]
