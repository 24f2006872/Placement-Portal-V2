<template>
  <nav class="navbar" :class="{ 'navbar--scrolled': scrolled }">
    <div class="navbar-inner">
      <!-- Brand -->
      <div class="brand">
        <span class="brand-icon">⬡</span>
        <span class="brand-name">NEXUS<span class="brand-accent">HIRE</span></span>
      </div>

      <!-- Center: role indicator -->
      <div class="role-pill" v-if="role">
        <span class="role-dot" :class="`role-dot--${role.toLowerCase()}`"></span>
        <span class="role-label">{{ roleLabel }}</span>
      </div>

      <!-- Right side -->
      <div class="nav-right">
        <div class="user-info" v-if="userEmail">
          <span class="user-avatar">{{ userInitial }}</span>
          <span class="user-email">{{ userEmail }}</span>
        </div>

        <button class="logout-btn" @click="logout">
          <span class="logout-icon">↩</span>
          <span>Sign Out</span>
        </button>
      </div>
    </div>

    <!-- Bottom accent line -->
    <div class="navbar-line"></div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      scrolled: false,
      role: localStorage.getItem('role') || '',
      userEmail: localStorage.getItem('email') || '',
    }
  },
  computed: {
    roleLabel() {
      const map = { ADMIN: 'Admin Panel', COMPANY: 'Company Portal', STUDENT: 'Student Portal' }
      return map[this.role] || this.role
    },
    userInitial() {
      return (this.userEmail || 'U')[0].toUpperCase()
    }
  },
  mounted() {
    window.addEventListener('scroll', this.onScroll, { passive: true })
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.onScroll)
  },
  methods: {
    onScroll() {
      this.scrolled = window.scrollY > 12
    },
    logout() {
      localStorage.removeItem('token')
      localStorage.removeItem('role')
      localStorage.removeItem('email')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&display=swap');

.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(8, 12, 24, 0.8);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  transition: background 0.3s, box-shadow 0.3s;
  font-family: 'DM Sans', sans-serif;
}

.navbar--scrolled {
  background: rgba(8, 12, 24, 0.96);
  box-shadow: 0 4px 32px rgba(0, 0, 0, 0.4);
}

.navbar-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 32px;
  height: 60px;
  display: flex;
  align-items: center;
  gap: 24px;
}

/* Brand */
.brand {
  display: flex;
  align-items: center;
  gap: 9px;
  flex-shrink: 0;
}

.brand-icon {
  font-size: 22px;
  color: #ffb800;
  display: inline-block;
  animation: spin 14s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.brand-name {
  font-family: 'Syne', sans-serif;
  font-size: 17px;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: 2px;
}

.brand-accent { color: #ffb800; }

/* Role pill */
.role-pill {
  display: flex;
  align-items: center;
  gap: 7px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.09);
  border-radius: 20px;
  padding: 5px 12px;
  font-size: 12px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.5);
  letter-spacing: 0.3px;
  margin-right: auto;
}

.role-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
}

.role-dot--admin   { background: #ffb800; box-shadow: 0 0 6px rgba(255,184,0,0.7); }
.role-dot--company { background: #a78bfa; box-shadow: 0 0 6px rgba(167,139,250,0.7); }
.role-dot--student { background: #4ade80; box-shadow: 0 0 6px rgba(74,222,128,0.7); }

/* Right side */
.nav-right {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-left: auto;
}

.role-pill + .nav-right {
  margin-left: 0;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 10px;
}

.user-avatar {
  width: 30px;
  height: 30px;
  background: linear-gradient(135deg, #ffb800, #ff8c00);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Syne', sans-serif;
  font-size: 13px;
  font-weight: 800;
  color: #0a0e1a;
  flex-shrink: 0;
}

.user-email {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.4);
  max-width: 160px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.logout-btn {
  display: flex;
  align-items: center;
  gap: 7px;
  padding: 7px 16px;
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: rgba(255, 255, 255, 0.5);
  font-family: 'DM Sans', sans-serif;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background 0.2s;
  white-space: nowrap;
}

.logout-btn:hover {
  border-color: rgba(255, 80, 80, 0.4);
  color: #ff6b6b;
  background: rgba(255, 80, 80, 0.06);
}

.logout-icon {
  font-size: 15px;
  transition: transform 0.2s;
}

.logout-btn:hover .logout-icon {
  transform: translateX(-2px);
}

/* Bottom accent line */
.navbar-line {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 120px;
  height: 1px;
  background: linear-gradient(90deg, #ffb800, transparent);
  opacity: 0.6;
}

@media (max-width: 600px) {
  .navbar-inner { padding: 0 16px; gap: 12px; }
  .user-email { display: none; }
  .role-pill { display: none; }
}
</style>