<template>
  <div class="dashboard-root">
    <div class="bg-grid"></div>

    <Navbar />

    <div class="dashboard-content">
      <div class="page-header">
        <div class="header-left">
          <div class="header-tag">CONTROL CENTER</div>
          <h1 class="page-title">Admin Dashboard</h1>
          <p class="page-sub">Platform overview and key metrics</p>
        </div>
        <div class="live-badge">
          <span class="live-dot"></span>
          <span>Live data</span>
        </div>
      </div>

      <div class="stats-grid">
        <div
          v-for="(card, i) in statCards"
          :key="card.key"
          class="stat-card"
          :class="`stat-card--${card.color}`"
          :style="`animation-delay: ${i * 0.08}s`"
        >
          <div class="stat-top">
            <span class="stat-label">{{ card.label }}</span>
            <span class="stat-icon-wrap">{{ card.icon }}</span>
          </div>
          <div class="stat-number">{{ stats[card.key] ?? '—' }}</div>
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
    return {
      stats: {},
      statCards: [
        { key: 'students',     label: 'Total Students', icon: '🎓', color: 'amber'  },
        { key: 'companies',    label: 'Companies',       icon: '🏢', color: 'blue'   },
        { key: 'drives',       label: 'Active Drives',   icon: '📋', color: 'green'  },
        { key: 'applications', label: 'Applications',    icon: '📨', color: 'purple' },
      ]
    }
  },
  async mounted() {
    const res = await api.get("/admin/dashboard")
    this.stats = res.data
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
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 32px 64px;
  position: relative;
  z-index: 1;
}

.page-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 40px;
  flex-wrap: wrap;
  gap: 16px;
}

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

.live-badge {
  display: flex; align-items: center; gap: 8px;
  background: rgba(34,197,94,0.1);
  border: 1px solid rgba(34,197,94,0.25);
  border-radius: 20px;
  padding: 6px 14px;
  font-size: 13px; color: #4ade80;
  white-space: nowrap;
}

.live-dot {
  width: 7px; height: 7px; border-radius: 50%;
  background: #4ade80;
  animation: livePulse 2s ease-in-out infinite;
}

@keyframes livePulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.5; transform: scale(0.85); }
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.stat-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 16px;
  padding: 28px 24px;
  position: relative;
  overflow: hidden;
  animation: cardIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
  transition: transform 0.2s, border-color 0.2s;
}

.stat-card:hover {
  transform: translateY(-3px);
  border-color: rgba(255,255,255,0.12);
}

@keyframes cardIn {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

.stat-card--amber  { --card-accent: #ffb800; }
.stat-card--blue   { --card-accent: #60a5fa; }
.stat-card--green  { --card-accent: #4ade80; }
.stat-card--purple { --card-accent: #a78bfa; }

.stat-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: var(--card-accent);
  opacity: 0.7;
}

.stat-top {
  display: flex; justify-content: space-between; align-items: flex-start;
  margin-bottom: 20px;
}

.stat-label {
  font-size: 12px; font-weight: 600;
  color: rgba(255,255,255,0.4);
  text-transform: uppercase; letter-spacing: 1px;
}

.stat-icon-wrap {
  font-size: 20px;
  background: rgba(255,255,255,0.06);
  border-radius: 8px;
  width: 38px; height: 38px;
  display: flex; align-items: center; justify-content: center;
}

.stat-number {
  font-family: 'Syne', sans-serif;
  font-size: 48px; font-weight: 800;
  color: var(--card-accent);
  line-height: 1;
}

@media (max-width: 900px) {
  .stats-grid { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 500px) {
  .stats-grid { grid-template-columns: 1fr; }
  .dashboard-content { padding: 24px 16px; }
}
</style>