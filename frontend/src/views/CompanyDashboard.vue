<template>
  <div class="dashboard-root">
    <div class="bg-grid"></div>

    <Navbar />

    <div class="dashboard-content">
      <div class="page-header">
        <div class="header-left">
          <div class="header-tag">RECRUITER HQ</div>
          <h1 class="page-title">Company Dashboard</h1>
          <p class="page-sub">Track your placement drives and applications</p>
        </div>
      </div>

      <!-- Summary pills — computed from API data -->
      <div class="summary-row" v-if="drives.length">
        <div class="summary-pill pill--amber">
          <span class="pill-num">{{ drives.length }}</span>
          <span class="pill-label">Total Drives</span>
        </div>
        <div class="summary-pill pill--green">
          <span class="pill-num">{{ openDrives }}</span>
          <span class="pill-label">Active</span>
        </div>
        <div class="summary-pill pill--blue">
          <span class="pill-num">{{ totalApplicants }}</span>
          <span class="pill-label">Total Applicants</span>
        </div>
      </div>

      <!-- Empty state -->
      <div v-if="drives.length === 0" class="empty-state">
        <div class="empty-icon">📋</div>
        <h3>No drives yet</h3>
        <p>Your placement drives will appear here once created</p>
      </div>

      <!-- Drives list -->
      <div v-else>
        <div class="section-label">YOUR DRIVES</div>
        <div class="drives-list">
          <div
            v-for="(d, i) in drives"
            :key="d.drive_id"
            class="drive-row"
            :style="`animation-delay: ${i * 0.06}s`"
          >
            <div class="drive-row-left">
              <div class="drive-avatar">{{ getInitial(d.title) }}</div>
              <div class="drive-info">
                <h3 class="drive-title">{{ d.title }}</h3>
                <span
                  class="drive-status"
                  :class="d.status === 'open' ? 'status--open' : 'status--closed'"
                >
                  {{ d.status }}
                </span>
              </div>
            </div>

            <div class="drive-row-stats">
              <div class="mini-stat">
                <span class="mini-num">{{ d.applicants ?? '—' }}</span>
                <span class="mini-label">Applicants</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api"
import Navbar from "../components/AppNavbar.vue"

export default {
  components: { Navbar },
  data() {
    return { drives: [] }
  },
  computed: {
    openDrives() {
      return this.drives.filter(d => d.status === 'open').length
    },
    totalApplicants() {
      return this.drives.reduce((sum, d) => sum + (d.applicants || 0), 0)
    }
  },
  async mounted() {
    const res = await api.get("/company/dashboard")
    this.drives = res.data
  },
  methods: {
    getInitial(title) { return (title || '?')[0].toUpperCase() }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

.dashboard-root {
  font-family: 'DM Sans', sans-serif;
  min-height: 100vh;
  background: #080c18;
  color: #fff;
  position: relative;
}

.bg-grid {
  position: fixed; inset: 0;
  background-image:
    linear-gradient(rgba(255,184,0,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,184,0,0.025) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
}

.dashboard-content {
  max-width: 1100px;
  margin: 0 auto;
  padding: 40px 32px 64px;
  position: relative; z-index: 1;
}

.page-header { margin-bottom: 32px; }

.header-tag {
  font-size: 11px; font-weight: 700;
  letter-spacing: 3px; color: #ffb800;
  margin-bottom: 10px;
}

.page-title {
  font-family: 'Syne', sans-serif;
  font-size: 36px; font-weight: 800; color: #ffffff;
  margin-bottom: 6px;
}

.page-sub { font-size: 14px; color: rgba(255,255,255,0.4); }

/* Summary */
.summary-row {
  display: flex; gap: 16px; flex-wrap: wrap;
  margin-bottom: 40px;
}

.summary-pill {
  flex: 1; min-width: 140px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 12px; padding: 20px;
  display: flex; flex-direction: column; gap: 4px;
  position: relative; overflow: hidden;
  transition: transform 0.2s;
}

.summary-pill:hover { transform: translateY(-2px); }

.summary-pill::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
}

.pill--amber::before { background: #ffb800; }
.pill--green::before { background: #4ade80; }
.pill--blue::before  { background: #60a5fa; }

.pill-num {
  font-family: 'Syne', sans-serif;
  font-size: 36px; font-weight: 800;
}

.pill--amber .pill-num { color: #ffb800; }
.pill--green .pill-num { color: #4ade80; }
.pill--blue  .pill-num { color: #60a5fa; }

.pill-label {
  font-size: 12px; color: rgba(255,255,255,0.35);
  text-transform: uppercase; letter-spacing: 1px; font-weight: 600;
}

/* Section label */
.section-label {
  font-size: 11px; font-weight: 700; letter-spacing: 2px;
  color: rgba(255,255,255,0.25); margin-bottom: 16px;
}

/* Drives list */
.drives-list { display: flex; flex-direction: column; gap: 12px; }

.drive-row {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 14px;
  padding: 20px 24px;
  display: flex; align-items: center; gap: 20px;
  animation: rowIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) both;
  transition: transform 0.2s, border-color 0.2s;
}

.drive-row:hover {
  transform: translateX(4px);
  border-color: rgba(255,184,0,0.18);
}

@keyframes rowIn {
  from { opacity: 0; transform: translateX(-12px); }
  to { opacity: 1; transform: translateX(0); }
}

.drive-row-left {
  display: flex; align-items: center; gap: 16px; flex: 1; min-width: 0;
}

.drive-avatar {
  width: 44px; height: 44px; flex-shrink: 0;
  background: linear-gradient(135deg, #ffb800, #ff8c00);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Syne', sans-serif;
  font-size: 20px; font-weight: 800; color: #0a0e1a;
}

.drive-info { min-width: 0; display: flex; flex-direction: column; gap: 6px; }

.drive-title {
  font-family: 'Syne', sans-serif;
  font-size: 16px; font-weight: 700; color: #fff;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}

.drive-status {
  font-size: 11px; font-weight: 600; letter-spacing: 0.5px;
  border-radius: 6px; padding: 3px 8px;
  text-transform: uppercase; width: fit-content;
}

.status--open   { background: rgba(74,222,128,0.1);  color: #4ade80; border: 1px solid rgba(74,222,128,0.2); }
.status--closed { background: rgba(255,255,255,0.06); color: rgba(255,255,255,0.3); border: 1px solid rgba(255,255,255,0.08); }

.drive-row-stats { display: flex; gap: 32px; flex-shrink: 0; }

.mini-stat { display: flex; flex-direction: column; align-items: center; gap: 2px; }

.mini-num {
  font-family: 'Syne', sans-serif;
  font-size: 22px; font-weight: 700; color: #ffffff;
}

.mini-label {
  font-size: 11px; color: rgba(255,255,255,0.3);
  text-transform: uppercase; letter-spacing: 0.5px;
}

/* Empty state */
.empty-state {
  display: flex; flex-direction: column; align-items: center;
  padding: 80px 0; gap: 12px; color: rgba(255,255,255,0.3);
  text-align: center;
}

.empty-icon { font-size: 48px; margin-bottom: 8px; }

.empty-state h3 {
  font-family: 'Syne', sans-serif;
  font-size: 20px; font-weight: 700; color: rgba(255,255,255,0.5);
}

.empty-state p { font-size: 14px; }

@media (max-width: 800px) {
  .drive-row { flex-wrap: wrap; }
  .dashboard-content { padding: 24px 16px; }
}
</style>