<template>
  <div class="dashboard-root">
    <div class="bg-grid"></div>

    <Navbar />

    <div class="dashboard-content">
      <div class="page-header">
        <div class="header-left">
          <div class="header-tag">PLACEMENT DRIVES</div>
          <h1 class="page-title">Available Drives</h1>
          <p class="page-sub">{{ drives.length }} {{ drives.length === 1 ? 'opportunity' : 'opportunities' }} available</p>
        </div>
        <div class="header-search">
          <span class="search-icon">⌕</span>
          <input v-model="search" class="search-input" placeholder="Search drives..." />
        </div>
      </div>

      <!-- Empty state -->
      <div v-if="filteredDrives.length === 0" class="empty-state">
        <div class="empty-icon">📭</div>
        <h3>No drives found</h3>
        <p>{{ search ? 'Try a different search term' : 'Check back later for new opportunities' }}</p>
      </div>

      <!-- Drives grid -->
      <div v-else class="drives-grid">
        <div
          v-for="(drive, i) in filteredDrives"
          :key="drive.id"
          class="drive-card"
          :style="`animation-delay: ${i * 0.06}s`"
        >
          <div class="card-top">
            <div class="company-avatar">{{ getInitial(drive.title) }}</div>
            <span
              class="status-badge"
              :class="drive.status === 'open' ? 'badge--open' : 'badge--closed'"
            >
              {{ drive.status || 'Open' }}
            </span>
          </div>

          <h3 class="drive-title">{{ drive.title }}</h3>
          <p class="drive-company" v-if="drive.company">{{ drive.company }}</p>

          <div class="drive-details">
            <div class="detail-pill">
              <span>Min CGPA: <strong>{{ drive.min_cgpa }}</strong></span>
            </div>
            <div class="detail-pill" v-if="drive.package">
              <span>{{ drive.package }} LPA</span>
            </div>
          </div>

          <div class="card-footer">
            <span class="deadline-text" v-if="drive.deadline">⏰ {{ drive.deadline }}</span>
            <button
              @click="apply(drive.id)"
              class="apply-btn"
              :disabled="applied.has(drive.id)"
              :class="{ 'applied': applied.has(drive.id) }"
            >
              <span v-if="!applied.has(drive.id)">Apply Now →</span>
              <span v-else>✓ Applied</span>
            </button>
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
    return {
      drives: [],
      search: '',
      applied: new Set(),
    }
  },
  computed: {
    filteredDrives() {
      if (!this.search) return this.drives
      const q = this.search.toLowerCase()
      return this.drives.filter(d =>
        d.title?.toLowerCase().includes(q) ||
        d.company?.toLowerCase().includes(q)
      )
    }
  },
  async mounted() {
    const res = await api.get("/student/drives")
    this.drives = res.data
  },
  methods: {
    getInitial(title) { return (title || '?')[0].toUpperCase() },
    async apply(id) {
      await api.post(`/student/apply/${id}`)
      this.applied = new Set([...this.applied, id])
    }
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
  position: relative; z-index: 1;
}

.page-header {
  display: flex; align-items: flex-end; justify-content: space-between;
  margin-bottom: 40px; gap: 24px; flex-wrap: wrap;
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

.header-search { position: relative; flex: 0 0 260px; }

.search-icon {
  position: absolute; left: 14px; top: 50%; transform: translateY(-50%);
  color: rgba(255,255,255,0.3); font-size: 18px; pointer-events: none;
}

.search-input {
  width: 100%; padding: 12px 16px 12px 42px;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 10px;
  color: #fff; font-family: 'DM Sans', sans-serif; font-size: 14px;
  outline: none; transition: border-color 0.2s;
}

.search-input::placeholder { color: rgba(255,255,255,0.2); }
.search-input:focus { border-color: rgba(255,184,0,0.4); }

.drives-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.drive-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 16px;
  padding: 24px;
  display: flex; flex-direction: column;
  animation: cardIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
  transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
}

.drive-card:hover {
  transform: translateY(-4px);
  border-color: rgba(255,184,0,0.2);
  box-shadow: 0 12px 40px rgba(0,0,0,0.3);
}

@keyframes cardIn {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

.card-top {
  display: flex; justify-content: space-between; align-items: flex-start;
  margin-bottom: 20px;
}

.company-avatar {
  width: 48px; height: 48px;
  background: linear-gradient(135deg, #ffb800, #ff8c00);
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-family: 'Syne', sans-serif;
  font-size: 22px; font-weight: 800; color: #0a0e1a;
}

.status-badge {
  font-size: 11px; font-weight: 600; letter-spacing: 1px;
  border-radius: 20px; padding: 4px 10px;
  text-transform: uppercase;
}

.badge--open   { background: rgba(74,222,128,0.1);  color: #4ade80; border: 1px solid rgba(74,222,128,0.25); }
.badge--closed { background: rgba(255,255,255,0.06); color: rgba(255,255,255,0.4); border: 1px solid rgba(255,255,255,0.1); }

.drive-title {
  font-family: 'Syne', sans-serif;
  font-size: 18px; font-weight: 700; color: #ffffff;
  margin-bottom: 4px; line-height: 1.3;
}

.drive-company {
  font-size: 13px; color: rgba(255,255,255,0.35);
  margin-bottom: 20px;
}

.drive-details {
  display: flex; flex-wrap: wrap; gap: 8px;
  margin-top: auto; margin-bottom: 20px;
}

.detail-pill {
  display: flex; align-items: center; gap: 6px;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 8px; padding: 6px 10px;
  font-size: 13px; color: rgba(255,255,255,0.6);
}

.detail-pill strong { color: #fff; }

.card-footer {
  display: flex; align-items: center; justify-content: space-between;
  padding-top: 16px;
  border-top: 1px solid rgba(255,255,255,0.06);
}

.deadline-text { font-size: 12px; color: rgba(255,255,255,0.3); }

.apply-btn {
  padding: 9px 18px;
  background: #ffb800;
  border: none; border-radius: 8px;
  color: #0a0e1a;
  font-family: 'Syne', sans-serif;
  font-size: 13px; font-weight: 700;
  cursor: pointer;
  transition: transform 0.15s, box-shadow 0.15s;
  white-space: nowrap;
}

.apply-btn:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 16px rgba(255,184,0,0.35);
}

.apply-btn.applied {
  background: rgba(74,222,128,0.12);
  color: #4ade80;
  border: 1px solid rgba(74,222,128,0.25);
  cursor: default;
}

.empty-state {
  display: flex; flex-direction: column; align-items: center;
  padding: 80px 0; gap: 12px;
  color: rgba(255,255,255,0.3); text-align: center;
}

.empty-icon { font-size: 48px; margin-bottom: 8px; }

.empty-state h3 {
  font-family: 'Syne', sans-serif;
  font-size: 20px; font-weight: 700; color: rgba(255,255,255,0.5);
}

.empty-state p { font-size: 14px; }

@media (max-width: 600px) {
  .drives-grid { grid-template-columns: 1fr; }
  .dashboard-content { padding: 24px 16px; }
  .header-search { flex: 0 0 100%; }
}
</style>