<template>
  <div class="login-root">
    <!-- Animated background -->
    <div class="bg-grid"></div>
    <div class="bg-glow"></div>

    <div class="login-split">
      <!-- Left panel -->
      <div class="left-panel">
        <div class="brand-mark">
          <span class="brand-icon">⬡</span>
          <span class="brand-name">NEXUS<span class="brand-accent">HIRE</span></span>
        </div>
        <div class="left-content">
          <h1 class="hero-heading">Your career<br><em>starts here.</em></h1>
          <p class="hero-sub">The placement portal connecting ambitious students with industry leaders.</p>
          <div class="stat-row">
            <div class="stat-item"><span class="stat-num">2,400+</span><span class="stat-label">Students placed</span></div>
            <div class="stat-item"><span class="stat-num">180+</span><span class="stat-label">Companies</span></div>
            <div class="stat-item"><span class="stat-num">94%</span><span class="stat-label">Success rate</span></div>
          </div>
        </div>
        <div class="geometric-dec">
          <div class="geo-ring geo-ring-1"></div>
          <div class="geo-ring geo-ring-2"></div>
          <div class="geo-dot"></div>
        </div>
      </div>

      <!-- Right panel -->
      <div class="right-panel">
        <div class="form-card">
          <div class="form-header">
            <h2 class="form-title">Welcome back</h2>
            <p class="form-sub">Sign in to continue to your portal</p>
          </div>

          <div class="field-group">
            <label class="field-label">Email address</label>
            <div class="input-wrap">
              <span class="input-icon">✉</span>
              <input v-model="email" class="styled-input" placeholder="you@university.edu" type="email" />
            </div>
          </div>

          <div class="field-group">
            <label class="field-label">Password</label>
            <div class="input-wrap">
              <span class="input-icon">⬤</span>
              <input v-model="password" class="styled-input" placeholder="••••••••" type="password" />
            </div>
          </div>

          <button @click="login" class="cta-btn">
            <span>Sign In</span>
            <span class="btn-arrow">→</span>
          </button>

          <div class="divider"><span>New here?</span></div>

          <div class="register-links">
            <router-link to="/register-student" class="reg-link reg-link--student">
              <span class="reg-link-icon">🎓</span>
              <span>Student Registration</span>
            </router-link>
            <router-link to="/register-company" class="reg-link reg-link--company">
              <span class="reg-link-icon">🏢</span>
              <span>Company Registration</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api"

export default {
  data() {
    return { email: "", password: "" }
  },
  methods: {
    async login() {
      try {
        const res = await api.post("/auth/login", { email: this.email, password: this.password })
        localStorage.setItem("token", res.data.access_token)
        localStorage.setItem("role", res.data.role)
        if (res.data.role === "ADMIN") this.$router.push("/admin")
        if (res.data.role === "COMPANY") this.$router.push("/company")
        if (res.data.role === "STUDENT") this.$router.push("/student")
      } catch (e) {
        alert("Invalid login")
      }
    }
  }
}
</script>

<style>
/* Global reset — removes browser default body margin causing white gap */
html, body, #app {
  margin: 0 !important;
  padding: 0 !important;
  background: #0a0e1a;
  min-height: 100vh;
}
</style>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

.login-root {
  font-family: 'DM Sans', sans-serif;
  min-height: 100vh;
  background: #0a0e1a;
  position: relative;
  overflow: hidden;
}

.bg-grid {
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(255,184,0,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,184,0,0.04) 1px, transparent 1px);
  background-size: 48px 48px;
  animation: gridShift 20s linear infinite;
}

@keyframes gridShift {
  0% { transform: translateY(0); }
  100% { transform: translateY(48px); }
}

.bg-glow {
  position: absolute;
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(255,184,0,0.08) 0%, transparent 70%);
  top: -100px; left: -100px;
  animation: glowPulse 6s ease-in-out infinite alternate;
}

@keyframes glowPulse {
  from { transform: scale(1); opacity: 0.5; }
  to { transform: scale(1.3); opacity: 1; }
}

.login-split {
  display: flex;
  min-height: 100vh;
  position: relative;
  z-index: 1;
}

/* LEFT PANEL */
.left-panel {
  flex: 1.1;
  padding: 48px 56px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  border-right: 1px solid rgba(255,184,0,0.1);
}

.brand-mark {
  display: flex;
  align-items: center;
  gap: 10px;
}

.brand-icon {
  font-size: 28px;
  color: #ffb800;
  animation: spin 12s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.brand-name {
  font-family: 'Syne', sans-serif;
  font-size: 22px;
  font-weight: 800;
  color: #ffffff;
  letter-spacing: 2px;
}

.brand-accent { color: #ffb800; }

.left-content { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 40px 0; }

.hero-heading {
  font-family: 'Syne', sans-serif;
  font-size: clamp(40px, 4.5vw, 64px);
  font-weight: 800;
  color: #ffffff;
  line-height: 1.1;
  margin-bottom: 20px;
}

.hero-heading em {
  font-style: italic;
  font-weight: 600;
  color: #ffb800;
}

.hero-sub {
  font-size: 16px;
  color: rgba(255,255,255,0.5);
  line-height: 1.6;
  max-width: 380px;
  margin-bottom: 48px;
}

.stat-row {
  display: flex;
  gap: 40px;
}

.stat-item { display: flex; flex-direction: column; gap: 4px; }

.stat-num {
  font-family: 'Syne', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: #ffb800;
}

.stat-label {
  font-size: 12px;
  color: rgba(255,255,255,0.4);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.geometric-dec {
  position: absolute;
  bottom: 60px; right: -60px;
  pointer-events: none;
}

.geo-ring {
  border-radius: 50%;
  border: 1px solid rgba(255,184,0,0.15);
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
}

.geo-ring-1 { width: 160px; height: 160px; animation: ringPulse 4s ease-in-out infinite; }
.geo-ring-2 { width: 100px; height: 100px; animation: ringPulse 4s ease-in-out infinite 1s; }

@keyframes ringPulse {
  0%, 100% { opacity: 0.2; transform: translate(-50%, -50%) scale(1); }
  50% { opacity: 0.6; transform: translate(-50%, -50%) scale(1.05); }
}

.geo-dot {
  width: 8px; height: 8px;
  background: #ffb800;
  border-radius: 50%;
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 0 16px rgba(255,184,0,0.8);
}

/* RIGHT PANEL */
.right-panel {
  flex: 0.9;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 40px;
}

.form-card {
  width: 100%;
  max-width: 400px;
  animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(24px); }
  to { opacity: 1; transform: translateY(0); }
}

.form-header { margin-bottom: 36px; }

.form-title {
  font-family: 'Syne', sans-serif;
  font-size: 32px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 8px;
}

.form-sub {
  font-size: 14px;
  color: rgba(255,255,255,0.4);
}

.field-group { margin-bottom: 20px; }

.field-label {
  display: block;
  font-size: 12px;
  font-weight: 500;
  color: rgba(255,255,255,0.5);
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 8px;
}

.input-wrap {
  position: relative;
}

.input-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 14px;
  color: rgba(255,184,0,0.5);
  pointer-events: none;
}

.styled-input {
  width: 100%;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 10px;
  padding: 14px 16px 14px 44px;
  color: #ffffff;
  font-family: 'DM Sans', sans-serif;
  font-size: 15px;
  transition: border-color 0.2s, background 0.2s;
  outline: none;
}

.styled-input::placeholder { color: rgba(255,255,255,0.2); }

.styled-input:focus {
  border-color: rgba(255,184,0,0.5);
  background: rgba(255,184,0,0.04);
}

.cta-btn {
  width: 100%;
  padding: 15px 24px;
  background: #ffb800;
  border: none;
  border-radius: 10px;
  color: #0a0e1a;
  font-family: 'Syne', sans-serif;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: 0.5px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-top: 8px;
  transition: transform 0.15s, box-shadow 0.15s;
}

.cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(255,184,0,0.35);
}

.btn-arrow {
  transition: transform 0.2s;
}

.cta-btn:hover .btn-arrow { transform: translateX(4px); }

.divider {
  display: flex;
  align-items: center;
  gap: 12px;
  margin: 28px 0 20px;
  color: rgba(255,255,255,0.2);
  font-size: 13px;
}

.divider::before, .divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: rgba(255,255,255,0.08);
}

.register-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.reg-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 13px 16px;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,0.08);
  color: rgba(255,255,255,0.7);
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: border-color 0.2s, background 0.2s, color 0.2s;
}

.reg-link:hover {
  border-color: rgba(255,184,0,0.4);
  background: rgba(255,184,0,0.06);
  color: #ffb800;
}

.reg-link-icon { font-size: 18px; }

@media (max-width: 768px) {
  .login-split { flex-direction: column; }
  .left-panel { padding: 32px 24px; border-right: none; border-bottom: 1px solid rgba(255,184,0,0.1); }
  .stat-row { gap: 24px; }
  .geometric-dec { display: none; }
}
</style>