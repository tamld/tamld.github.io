#!/usr/bin/env python3
"""
Reproducible Vector Generator for TamLD Homelab Dual-Plane Topology.
Compiles physical infrastructure invariants into a crisp, zero-gradient,
responsive dark-industrial SVG asset.

SSoT Reference:
  - 1-Knowledge/K-Proxmox-Home-Server-Lab.md
  - .agents/plugins/homelab-sre/rules/AGENTS.md
"""

from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parent.parent / "assets" / "diagrams" / "arch-dualplane-topology.svg"

SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1060 620" width="100%" height="100%" class="w-full h-auto font-mono text-xs">
  <defs>
    <style>
      .bg-canvas { fill: #09090b; }
      .bg-panel { fill: #111114; stroke: #1e1e23; stroke-width: 1; }
      .bg-card { fill: #16161b; stroke: #27272a; stroke-width: 1; }
      .bg-card-highlight { fill: #181820; stroke: #38bdf8; stroke-width: 1.5; }
      .bg-boundary { fill: #0d0d10; stroke: #27272a; stroke-width: 1; stroke-dasharray: 4 4; }
      
      .text-title { fill: #fafafa; font-family: 'JetBrains Mono', monospace; font-size: 13px; font-weight: 600; letter-spacing: -0.01em; }
      .text-header { fill: #e4e4e7; font-family: 'JetBrains Mono', monospace; font-size: 11px; font-weight: 600; }
      .text-body { fill: #a1a1aa; font-family: 'Inter', system-ui, sans-serif; font-size: 10px; }
      .text-code { fill: #38bdf8; font-family: 'JetBrains Mono', monospace; font-size: 9.5px; }
      .text-green { fill: #10b981; font-family: 'JetBrains Mono', monospace; font-size: 9.5px; }
      .text-amber { fill: #f59e0b; font-family: 'JetBrains Mono', monospace; font-size: 9.5px; }
      .text-muted { fill: #71717a; font-family: 'Inter', system-ui, sans-serif; font-size: 9px; }

      .flow-wan { stroke: #38bdf8; stroke-width: 1.5; fill: none; }
      .flow-lan { stroke: #10b981; stroke-width: 1.5; fill: none; stroke-dasharray: 3 3; }
      .flow-auth { stroke: #f59e0b; stroke-width: 1.5; fill: none; stroke-dasharray: 4 3; }
      .flow-telemetry { stroke: #818cf8; stroke-width: 1.2; fill: none; stroke-dasharray: 2 3; }
      .flow-marker { fill: #38bdf8; }
    </style>
    <marker id="arrow-wan" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrow-lan" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#10b981"/>
    </marker>
    <marker id="arrow-auth" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#f59e0b"/>
    </marker>
    <marker id="arrow-telemetry" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#818cf8"/>
    </marker>
  </defs>

  <!-- Canvas Surface -->
  <rect width="1060" height="620" class="bg-canvas" rx="8"/>
  <rect x="8" y="8" width="1044" height="604" fill="none" stroke="#1e1e23" stroke-width="1" rx="6"/>

  <!-- TOP HEADER / METRIC BAR -->
  <rect x="16" y="16" width="1028" height="48" class="bg-panel" rx="4"/>
  <circle cx="36" cy="40" r="4" fill="#10b981"/>
  <text x="48" y="44" class="text-title">HOMELAB DUAL-PLANE INGRESS &amp; OBSERVABILITY TOPOLOGY</text>
  <text x="490" y="44" class="text-muted">Node 1: PVE i5-8500 (16GB RAM) · Single Authority RouterOS DHCP (10.0.0.1) · Zero-WAN Mgmt</text>
  
  <!-- LEGEND -->
  <g transform="translate(820, 28)">
    <line x1="0" y1="12" x2="16" y2="12" stroke="#38bdf8" stroke-width="2"/>
    <text x="22" y="15" class="text-code" font-size="8.5">WAN Ingress</text>
    <line x1="95" y1="12" x2="111" y2="12" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 2"/>
    <text x="117" y="15" class="text-green" font-size="8.5">[LAN] Probe</text>
  </g>

  <!-- ==================== ZONE 1: PUBLIC INTERNET & EDGE (x: 20 -> 180) ==================== -->
  <rect x="20" y="76" width="165" height="524" class="bg-boundary" rx="4"/>
  <text x="32" y="98" class="text-header">PUBLIC EDGE</text>
  <text x="32" y="112" class="text-muted">Untrusted Internet</text>

  <!-- Public Clients Node -->
  <rect x="32" y="130" width="141" height="84" class="bg-card" rx="4"/>
  <text x="44" y="152" class="text-header">External Users</text>
  <text x="44" y="168" class="text-code">*.edge.internal</text>
  <text x="44" y="184" class="text-body">Public Clients</text>
  <text x="44" y="198" class="text-muted">HTTPS / Port 443</text>

  <!-- Cloudflare Edge WAF Node -->
  <rect x="32" y="270" width="141" height="154" class="bg-card" rx="4"/>
  <text x="44" y="292" class="text-header">Cloudflare Edge</text>
  <text x="44" y="308" class="text-code">WAF + GeoFilter</text>
  <text x="44" y="326" class="text-body">• Strict SSL/TLS</text>
  <text x="44" y="342" class="text-body">• DDoS Protection</text>
  <text x="44" y="358" class="text-body">• IP Filtering</text>
  <text x="44" y="380" class="text-green">cloudflare_ips</text>
  <text x="44" y="400" class="text-muted">Origin Ingress Port 443</text>

  <!-- Tailscale Zero-WAN Entry -->
  <rect x="32" y="480" width="141" height="96" class="bg-card" rx="4"/>
  <text x="44" y="502" class="text-header">Tailscale VPN</text>
  <text x="44" y="518" class="text-code">Overlay Mesh</text>
  <text x="44" y="536" class="text-body">Admin Direct Mesh</text>
  <text x="44" y="552" class="text-muted">Zero-WAN Exposure</text>

  <!-- ==================== ZONE 2: PERIMETER GATEWAY & AUTH (x: 215 -> 465) ==================== -->
  <rect x="210" y="76" width="250" height="524" class="bg-boundary" rx="4"/>
  <text x="224" y="98" class="text-header">PERIMETER &amp; IDENTITY GATEWAY</text>
  <text x="224" y="112" class="text-muted">Ingress / Auth Boundary</text>

  <!-- EDGE-PROXY Traefik Ingress Node -->
  <rect x="224" y="130" width="222" height="130" class="bg-card-highlight" rx="4"/>
  <rect x="232" y="138" width="56" height="16" fill="#0284c7" rx="2"/>
  <text x="237" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">EDGE-PROXY</text>
  <text x="296" y="151" class="text-header">Traefik Ingress</text>
  <text x="236" y="176" class="text-code">10.0.0.10:80/443</text>
  <text x="236" y="196" class="text-body">• Cloudflare Ingress Proxy</text>
  <text x="236" y="212" class="text-body">• Dynamic Provider (Docker/File)</text>
  <text x="236" y="228" class="text-body">• ForwardAuth Middleware</text>
  <text x="236" y="244" class="text-green">Status: LAN=UP · Edge Verified</text>

  <!-- IAM-AUTH Authelia IAM Node -->
  <rect x="224" y="290" width="222" height="114" class="bg-card" rx="4"/>
  <rect x="232" y="298" width="56" height="16" fill="#d97706" rx="2"/>
  <text x="237" y="310" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">IAM-AUTH</text>
  <text x="296" y="311" class="text-header">Authelia Gateway</text>
  <text x="236" y="336" class="text-amber">10.0.0.20:9091</text>
  <text x="236" y="354" class="text-body">• 2FA / WebAuthn / TOTP</text>
  <text x="236" y="370" class="text-body">• OIDC Client Broker</text>
  <text x="236" y="386" class="text-muted">LDAP / LLDAP Identity SSoT</text>

  <!-- MikroTik RouterOS Gateway (Bottom of Zone 2) -->
  <rect x="224" y="430" width="222" height="146" class="bg-card" rx="4"/>
  <rect x="232" y="438" width="80" height="16" fill="#3f3f46" rx="2"/>
  <text x="237" y="450" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">RouterOS</text>
  <text x="320" y="451" class="text-header">MikroTik Router</text>
  <text x="236" y="476" class="text-green">10.0.0.1 (Single Authority)</text>
  <text x="236" y="496" class="text-body">• Authoritative DHCP Server</text>
  <text x="236" y="512" class="text-body">• Static MAC-to-IP Binding SSoT</text>
  <text x="236" y="528" class="text-body">• Ephemeral Flash Invariant (&lt;2MB)</text>
  <text x="236" y="546" class="text-code">Dual Backup: .rsc + .backup</text>
  <text x="236" y="562" class="text-muted">Port Forwarding: 80/443 strictly</text>

  <!-- ==================== ZONE 3: COMPUTE CLUSTER & CONTAINERS (x: 485 -> 745) ==================== -->
  <rect x="480" y="76" width="260" height="524" class="bg-boundary" rx="4"/>
  <text x="494" y="98" class="text-header">PROXMOX COMPUTE FABRIC</text>
  <text x="494" y="112" class="text-muted">PVE Host: 10.0.0.2 (16GB RAM budget)</text>

  <!-- SECRETS Vaultwarden -->
  <rect x="494" y="130" width="232" height="66" class="bg-card" rx="4"/>
  <text x="506" y="148" class="text-header">SECRETS · Vaultwarden</text>
  <text x="506" y="164" class="text-code">10.0.0.30:80</text>
  <text x="506" y="180" class="text-body">Secrets / IAM Vault · Encrypted</text>

  <!-- COMPUTE Coolify -->
  <rect x="494" y="210" width="232" height="66" class="bg-card" rx="4"/>
  <text x="506" y="228" class="text-header">COMPUTE · Coolify Runner</text>
  <text x="506" y="244" class="text-code">10.0.0.40:8000</text>
  <text x="506" y="260" class="text-body">App Deployment &amp; Workload Node</text>

  <!-- DNS-RESOLV AdGuard Home -->
  <rect x="494" y="290" width="232" height="66" class="bg-card" rx="4"/>
  <text x="506" y="308" class="text-header">DNS-RESOLV · AdGuard Home</text>
  <text x="506" y="324" class="text-code">10.0.0.50:53</text>
  <text x="506" y="340" class="text-body">Client/IoT DNS · Anti-Circular Law</text>

  <!-- SRE-OBSERVER Butler SRE Agent -->
  <rect x="494" y="370" width="232" height="66" class="bg-card" rx="4"/>
  <text x="506" y="388" class="text-header">SRE-OBSERVER · Butler SRE Observer</text>
  <text x="506" y="404" class="text-code">10.0.0.80 (Least-Priv PVE REST)</text>
  <text x="506" y="420" class="text-body">Autonomous Fleet Health Prober</text>

  <!-- Host Invariants Footer inside Zone 3 -->
  <rect x="494" y="454" width="232" height="122" class="bg-card" rx="4"/>
  <text x="506" y="474" class="text-header">Host Invariants (ZFS)</text>
  <text x="506" y="492" class="text-body">• net0: ip=dhcp (Enforced)</text>
  <text x="506" y="508" class="text-body">• Zero Root SSH Injection</text>
  <text x="506" y="524" class="text-body">• RAM Headroom &gt; 15% Safe</text>
  <text x="506" y="540" class="text-body">• Podman NET_RAW Preserved</text>
  <text x="506" y="558" class="text-green">Sub-2s Batch Telemetry (pct list)</text>

  <!-- ==================== ZONE 4: OBSERVABILITY & TELEMETRY (x: 765 -> 1040) ==================== -->
  <rect x="760" y="76" width="280" height="524" class="bg-boundary" rx="4"/>
  <text x="774" y="98" class="text-header">DUAL-PLANE OBSERVABILITY</text>
  <text x="774" y="112" class="text-muted">Probes &amp; Telemetry Aggregation</text>

  <!-- DUAL-PROBE Uptime Kuma Dual-Plane Node -->
  <rect x="774" y="130" width="252" height="194" class="bg-card-highlight" rx="4"/>
  <rect x="782" y="138" width="56" height="16" fill="#10b981" rx="2"/>
  <text x="787" y="150" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">DUAL-PROBE</text>
  <text x="846" y="151" class="text-header">Uptime Kuma Dual-Plane</text>
  <text x="786" y="176" class="text-green">10.0.0.60:3001</text>

  <!-- Probe 1: LAN Probe -->
  <rect x="786" y="190" width="228" height="48" fill="#111114" stroke="#1e1e23" rx="3"/>
  <circle cx="798" cy="206" r="3.5" fill="#10b981"/>
  <text x="808" y="209" class="text-green" font-weight="bold">[LAN] Compute Health</text>
  <text x="808" y="224" class="text-muted">http://10.0.0.x:port (Zero Latency)</text>

  <!-- Probe 2: WAN Probe -->
  <rect x="786" y="246" width="228" height="48" fill="#111114" stroke="#1e1e23" rx="3"/>
  <circle cx="798" cy="262" r="3.5" fill="#38bdf8"/>
  <text x="808" y="265" class="text-code" font-weight="bold">[WAN] Edge Reachability</text>
  <text x="808" y="280" class="text-muted">https://*.edge.internal (TLS + Routing)</text>

  <text x="786" y="312" class="text-amber">Correlation: LAN=UP &amp; WAN=DOWN</text>

  <!-- LOG-SINK VictoriaLogs Centralized Telemetry -->
  <rect x="774" y="344" width="252" height="140" class="bg-card" rx="4"/>
  <rect x="782" y="352" width="56" height="16" fill="#6366f1" rx="2"/>
  <text x="787" y="364" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">LOG-SINK</text>
  <text x="846" y="365" class="text-header">VictoriaLogs SSoT</text>
  <text x="786" y="390" class="text-code">10.0.0.70:9428</text>
  <text x="786" y="410" class="text-body">• Centralized Syslog / Container LogSQL</text>
  <text x="786" y="426" class="text-body">• Fast Incident Triage (Tier-1 First)</text>
  <text x="786" y="442" class="text-body">• Anti-Terminal Hunting Invariant</text>
  <text x="786" y="462" class="text-green">Sub-Second Filter: _time:1h AND error</text>

  <!-- Live Telemetry Sync Badge -->
  <rect x="774" y="504" width="252" height="72" class="bg-card" rx="4"/>
  <text x="786" y="524" class="text-header">Telemetry Integration</text>
  <text x="786" y="542" class="text-body">Dynamic JSON Sync to GitHub Pages</text>
  <text x="786" y="558" class="text-code">/data/telemetry.json (Offline Cached)</text>

  <!-- ==================== FLOW CONNECTORS & ARROWS ==================== -->
  <!-- 1. External -> Cloudflare -->
  <path d="M 102 214 L 102 270" class="flow-wan" marker-end="url(#arrow-wan)"/>

  <!-- 2. Cloudflare -> Traefik EDGE-PROXY -->
  <path d="M 173 347 L 198 347 L 198 195 L 224 195" class="flow-wan" marker-end="url(#arrow-wan)"/>

  <!-- 3. Traefik -> Authelia ForwardAuth Verification Loop -->
  <path d="M 290 260 L 290 290" class="flow-auth" marker-end="url(#arrow-auth)"/>
  <path d="M 370 290 L 370 260" class="flow-auth" marker-end="url(#arrow-auth)"/>

  <!-- 4. Traefik -> Workloads (Coolify & Vaultwarden) -->
  <path d="M 446 163 L 494 163" class="flow-wan" marker-end="url(#arrow-wan)"/>
  <path d="M 446 210 L 470 210 L 470 243 L 494 243" class="flow-wan" marker-end="url(#arrow-wan)"/>

  <!-- 5. MikroTik RouterOS DHCP Authority Leases -->
  <path d="M 446 503 L 470 503 L 470 470 L 494 470" class="flow-lan" marker-end="url(#arrow-lan)"/>

  <!-- 6. Uptime Kuma LAN Probes to EDGE-PROXY & COMPUTE -->
  <path d="M 774 214 L 746 214 L 746 175 L 726 175" class="flow-lan" marker-end="url(#arrow-lan)"/>
  <path d="M 774 214 L 746 214 L 746 230 L 726 230" class="flow-lan" marker-end="url(#arrow-lan)"/>

  <!-- 7. Container Logs Stream to VictoriaLogs LOG-SINK -->
  <path d="M 726 395 L 774 395" class="flow-telemetry" marker-end="url(#arrow-telemetry)"/>

</svg>
"""

def generate():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Strip any extra trailing whitespace
    clean_svg = SVG_CONTENT.strip() + "\n"
    OUTPUT_PATH.write_text(clean_svg, encoding="utf-8")
    size_bytes = OUTPUT_PATH.stat().st_size
    print(f"Generated {OUTPUT_PATH} ({size_bytes} bytes).")
    assert size_bytes < 25000, f"Size {size_bytes} exceeds 25KB budget!"
    assert "linear-gradient" not in clean_svg and "linearGradient" not in clean_svg
    assert "radial-gradient" not in clean_svg and "radialGradient" not in clean_svg
    print("✅ Verified Zero Gradient Law & 25KB budget successfully.")

if __name__ == "__main__":
    generate()
