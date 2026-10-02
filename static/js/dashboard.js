// NIDS Dashboard — polls Flask API and renders live updates

const POLL_MS = 1500;
const MAX_PULSE_BARS = 60;

const el = {
  statusDot: document.getElementById('status-dot'),
  statusText: document.getElementById('status-text'),
  btnStart: document.getElementById('btn-start'),
  btnStop: document.getElementById('btn-stop'),
  btnClear: document.getElementById('btn-clear'),
  pulseStrip: document.getElementById('pulse-strip'),
  statTotal: document.getElementById('stat-total'),
  statAlerts: document.getElementById('stat-alerts'),
  statNormal: document.getElementById('stat-normal'),
  statRate: document.getElementById('stat-rate'),
  alertList: document.getElementById('alert-list'),
  alertCount: document.getElementById('alert-count'),
  activityBody: document.getElementById('activity-body'),
  activityCount: document.getElementById('activity-count'),
};

let isRunning = false;
let pollTimer = null;
let lastSeenActivityId = null;

function setStatus(running) {
  isRunning = running;
  el.statusDot.classList.toggle('live', running);
  el.statusText.textContent = running ? 'MONITORING LIVE' : 'STOPPED';
}

async function postJSON(url) {
  const res = await fetch(url, { method: 'POST' });
  return res.json();
}

async function getJSON(url) {
  const res = await fetch(url);
  return res.json();
}

function fmtTime(iso) {
  const d = new Date(iso);
  return d.toLocaleTimeString('en-US', { hour12: false });
}

function addPulseBar(severity) {
  const bar = document.createElement('div');
  const heights = { info: 8, low: 16, high: 26, critical: 34 };
  bar.className = `pulse-bar ${severity}`;
  bar.style.height = `${heights[severity] || 4}px`;
  el.pulseStrip.appendChild(bar);
  while (el.pulseStrip.children.length > MAX_PULSE_BARS) {
    el.pulseStrip.removeChild(el.pulseStrip.firstChild);
  }
}

function renderStats(stats) {
  el.statTotal.textContent = stats.total_analyzed;
  el.statAlerts.textContent = stats.total_alerts;
  el.statNormal.textContent = stats.normal_count;
  const rate = stats.total_analyzed > 0
    ? Math.round((stats.total_alerts / stats.total_analyzed) * 100)
    : 0;
  el.statRate.textContent = `${rate}%`;
}

function renderAlerts(alerts) {
  el.alertCount.textContent = `${alerts.length} alerts`;
  if (alerts.length === 0) {
    el.alertList.innerHTML = '<div class="empty-state">No alerts yet — start monitoring to begin analysis.</div>';
    return;
  }
  el.alertList.innerHTML = alerts.map(a => `
    <div class="alert-row">
      <span class="sev-tag ${a.severity}">${a.severity}</span>
      <span class="alert-cat">${a.predicted_category}</span>
      <span class="alert-ip">${a.src_ip} &rarr; ${a.dst_ip}</span>
      <span class="alert-time">${fmtTime(a.timestamp)}</span>
    </div>
  `).join('');
}

function renderActivity(activity) {
  el.activityCount.textContent = `${activity.length} records`;
  if (activity.length === 0) {
    el.activityBody.innerHTML = '<tr><td colspan="8" class="empty-state">No activity recorded yet.</td></tr>';
    return;
  }
  el.activityBody.innerHTML = activity.map(r => `
    <tr class="${r.is_attack ? 'is-attack' : ''}">
      <td>${fmtTime(r.timestamp)}</td>
      <td>${r.src_ip}</td>
      <td>${r.dst_ip}</td>
      <td>${r.protocol_type}</td>
      <td>${r.service}</td>
      <td>${r.predicted_category}</td>
      <td>${(r.confidence * 100).toFixed(0)}%</td>
      <td><span class="badge ${r.is_attack ? 'attack' : 'normal'}">${r.is_attack ? 'ATTACK' : 'NORMAL'}</span></td>
    </tr>
  `).join('');

  // Pulse bar for the newest record only, to avoid replaying history every poll
  const newest = activity[0];
  if (newest && newest.id !== lastSeenActivityId) {
    lastSeenActivityId = newest.id;
    addPulseBar(newest.severity);
  }
}

async function refresh() {
  try {
    const [stats, alerts, activity] = await Promise.all([
      getJSON('/api/stats'),
      getJSON('/api/alerts?limit=30'),
      getJSON('/api/activity?limit=40'),
    ]);
    renderStats(stats);
    renderAlerts(alerts);
    renderActivity(activity);
  } catch (err) {
    console.error('Refresh failed:', err);
  }
}

function startPolling() {
  if (pollTimer) return;
  refresh();
  pollTimer = setInterval(refresh, POLL_MS);
}

function stopPolling() {
  clearInterval(pollTimer);
  pollTimer = null;
}

el.btnStart.addEventListener('click', async () => {
  await postJSON('/api/simulator/start');
  setStatus(true);
  startPolling();
});

el.btnStop.addEventListener('click', async () => {
  await postJSON('/api/simulator/stop');
  setStatus(false);
  stopPolling();
});

el.btnClear.addEventListener('click', async () => {
  await postJSON('/api/clear');
  el.pulseStrip.innerHTML = '';
  lastSeenActivityId = null;
  refresh();
});

// Initial load (in case simulator was already running / logs already exist)
refresh();
