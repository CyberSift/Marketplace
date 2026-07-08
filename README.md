# Marketplace
This repo contains templates and samples for CyberSift Sentio visuals, Sentio dashboards and Nifi flows.

## Intro: CyberSift Sentio SIEM

CyberSift Sentio is a unified security intelligence platform that combines logs, events, behaviour and anomalies to reveal threats in full context. Designed to cut through alert noise, it delivers real-time detection, correlation and investigation capabilities through an open-stack architecture (OpenSearch, NiFi).

**Key capabilities:**

- **Unified log collection** from Windows, Linux, cloud platforms (AWS, Azure/O365, Google Workspace), firewalls, endpoint protection (ESET, SentinelOne), network devices and more
- **100+ built-in detection rules** covering Windows, Linux, cloud, network and application-layer attacks, plus ML-driven anomaly baselining
- **Threat intelligence integration** with MISP feeds, enriching every event with AS numbers, geolocation, ISP info and known threat indicators (TOR, CnC, scanners)
- **Investigation toolkit** including Discover search, CyberSift Fields, User/IP/Host dashboards and liveliness monitoring
- **Prebuilt dashboards and visuals** *(this repo)* for O365, network security, firewall, endpoint, SWIFT, VPN and more
- **Comprehensive reporting** with canned reports across all major log source categories plus on-demand generation
- **AI-augmented analysis** via Cyberbot, an integrated LLM assistant with MCP tool access and natural language querying
- **Scalable architecture** from single-node all-in-one to fully redundant HA setups, with cold storage offload to cloud providers
- **SOC-driven detection engineering** where analysts can contribute and evolve rules through a formal workflow


## Sentio Visuals

```json
[
    {
        "name": "Visual Title",
        "description": "Brief description of what the visual shows and its purpose.",
        "tags": [
            "tag1",
            "tag2"
        ],
        "export": { ... }
    }
]
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Display name of the visual |
| `description` | string | Human-readable description of what the visual displays |
| `tags` | string[] | Keywords for categorising and filtering the visual |
| `export` | raw json from the sentio "Export" button |

## Sentio Dashboards

> **Note:** A dashboard is an array of [Visuals](#sentio-visuals). The `export` object contains a `panels` array where each panel is a visual embedded in the dashboard.

```json
[
    {
        "name": "Dashboard Title",
        "description": "Brief description of what the dashboard shows and its purpose.",
        "reference": "https://www.cybersift.io",
        "tags": [
            "tag1",
            "tag2"
        ],
        "export": { ... }
    }
]
```

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Display name of the dashboard |
| `description` | string | Human-readable description of what the dashboard displays |
| `reference` | string | Link to related Cybersift documentation or resource |
| `tags` | string[] | Keywords for categorising and filtering the dashboard |
| `export` | raw json from the sentio "Export" button |

## NiFi Template

```json
[
    {
      "name": "Flow Name",
      "description": "Flow Description",
      "reference": "https://www.cybersift.io",
      "tags": [
        "flow_tag_1"
      ],
      "export": {
        // json export
      }
    },
    //...
]
```