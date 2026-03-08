<template>
  <div class="reg-root">
    <div class="bg-grid"></div>
    <div class="bg-glow bg-glow--blue"></div>

    <div class="reg-split">
      <!-- Left decorative panel -->
      <div class="side-panel">
        <router-link to="/" class="back-link">← Back to Login</router-link>
        <div class="side-content">
          <div class="side-tag">STUDENT PORTAL</div>
          <h2 class="side-heading">Begin your<br>journey<br>today.</h2>
          <div class="step-trail">
            <div class="step-item step-active"><span class="step-dot"></span><span>Create Account</span></div>
            <div class="step-line"></div>
            <div class="step-item"><span class="step-dot"></span><span>Explore Drives</span></div>
            <div class="step-line"></div>
            <div class="step-item"><span class="step-dot"></span><span>Get Placed</span></div>
          </div>
        </div>
        <div class="floating-card card-a">
          <span class="fc-icon">🎓</span>
          <span class="fc-text">Join 2,400+ students</span>
        </div>
        <div class="floating-card card-b">
          <span class="fc-icon">✨</span>
          <span class="fc-text">Top campus portal</span>
        </div>
      </div>

      <!-- Form panel -->
      <div class="form-panel">
        <div class="form-card">
          <div class="form-header">
            <span class="form-tag">🎓 Student</span>
            <h2 class="form-title">Create your account</h2>
            <p class="form-sub">Fill in your details to register as a student</p>
          </div>

          <div class="fields-grid">
            <div class="field-group field-full">
              <label class="field-label">Full Name</label>
              <input v-model="form.name" class="styled-input" placeholder="John Doe" />
            </div>

            <div class="field-group field-full">
              <label class="field-label">University Email</label>
              <input v-model="form.email" class="styled-input" placeholder="you@university.edu" type="email" />
            </div>

            <div class="field-group field-full">
              <label class="field-label">Password</label>
              <input v-model="form.password" class="styled-input" placeholder="Create a strong password" type="password" />
            </div>

            <div class="field-group">
              <label class="field-label">Branch / Department</label>
              <input v-model="form.branch" class="styled-input" placeholder="e.g. Computer Science" />
            </div>

            <div class="field-group">
              <label class="field-label">CGPA</label>
              <input v-model="form.cgpa" class="styled-input" placeholder="e.g. 8.5" type="number" step="0.1" max="10" />
            </div>

            <div class="field-group field-full">
              <label class="field-label">Graduation Year</label>
              <input v-model="form.graduation_year" class="styled-input" placeholder="e.g. 2025" type="number" />
            </div>
          </div>

          <button @click="register" class="cta-btn">
            <span>Register as Student</span>
            <span class="btn-arrow">→</span>
          </button>

          <p class="login-prompt">Already registered? <router-link to="/" class="login-link">Sign in</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api"

export default {
  data() { return { form: {} } },
  methods: {
    async register() {
      await api.post("/auth/register/student", this.form)
      alert("Registered successfully")
      this.$router.push("/")
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

.reg-root {
  font-family: 'DM Sans', sans-serif;
  min-height: 100vh;
  background: #0a0e1a;
  position: relative;
  overflow-x: hidden;
}

.bg-grid {
  position: fixed; inset: 0;
  background-image:
    linear-gradient(rgba(255,184,0,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,184,0,0.03) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
}

.bg-glow {
  position: fixed;
  width: 500px; height: 500px;
  border-radius: 50%;
  pointer-events: none;
}

.bg-glow--blue {
  background: radial-gradient(circle, rgba(64,120,255,0.1) 0%, transparent 70%);
  bottom: -100px; right: -100px;
}

.reg-split {
  display: flex;
  min-height: 100vh;
  position: relative;
  z-index: 1;
}

/* SIDE PANEL */
.side-panel {
  flex: 0 0 380px;
  background: linear-gradient(160deg, #0f1629 0%, #0a0e1a 100%);
  border-right: 1px solid rgba(255,184,0,0.08);
  padding: 40px 40px;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
}

.side-panel::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, #ffb800, transparent);
}

.back-link {
  color: rgba(255,255,255,0.35);
  text-decoration: none;
  font-size: 13px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: color 0.2s;
}

.back-link:hover { color: #ffb800; }

.side-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.side-tag {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 3px;
  color: #ffb800;
  margin-bottom: 20px;
}

.side-heading {
  font-family: 'Syne', sans-serif;
  font-size: 42px;
  font-weight: 800;
  color: #ffffff;
  line-height: 1.1;
  margin-bottom: 48px;
}

.step-trail { display: flex; flex-direction: column; gap: 0; }

.step-item {
  display: flex;
  align-items: center;
  gap: 14px;
  color: rgba(255,255,255,0.3);
  font-size: 14px;
  font-weight: 500;
}

.step-active { color: #ffb800; }

.step-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
  background: rgba(255,255,255,0.15);
  flex-shrink: 0;
}

.step-active .step-dot {
  background: #ffb800;
  box-shadow: 0 0 12px rgba(255,184,0,0.6);
}

.step-line {
  width: 1px;
  height: 24px;
  background: rgba(255,255,255,0.08);
  margin-left: 5px;
}

.floating-card {
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 10px;
  padding: 10px 14px;
  font-size: 13px;
  color: rgba(255,255,255,0.6);
  width: fit-content;
}

.card-a { margin-bottom: 8px; animation: floatA 4s ease-in-out infinite alternate; }
.card-b { animation: floatB 5s ease-in-out infinite alternate; }

@keyframes floatA {
  from { transform: translateY(0px); }
  to { transform: translateY(-6px); }
}

@keyframes floatB {
  from { transform: translateY(-4px); }
  to { transform: translateY(4px); }
}

/* FORM PANEL */
.form-panel {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 40px;
}

.form-card {
  width: 100%;
  max-width: 500px;
  animation: slideUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.form-header { margin-bottom: 32px; }

.form-tag {
  display: inline-block;
  background: rgba(255,184,0,0.12);
  color: #ffb800;
  border: 1px solid rgba(255,184,0,0.25);
  border-radius: 20px;
  padding: 4px 12px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.5px;
  margin-bottom: 14px;
}

.form-title {
  font-family: 'Syne', sans-serif;
  font-size: 28px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 6px;
}

.form-sub {
  font-size: 14px;
  color: rgba(255,255,255,0.4);
}

.fields-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 24px;
}

.field-group { display: flex; flex-direction: column; gap: 7px; }
.field-full { grid-column: 1 / -1; }

.field-label {
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,0.4);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.styled-input {
  width: 100%;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 9px;
  padding: 13px 15px;
  color: #ffffff;
  font-family: 'DM Sans', sans-serif;
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s, background 0.2s;
}

.styled-input::placeholder { color: rgba(255,255,255,0.18); }

.styled-input:focus {
  border-color: rgba(255,184,0,0.45);
  background: rgba(255,184,0,0.04);
}

.cta-btn {
  width: 100%;
  padding: 15px 24px;
  background: linear-gradient(135deg, #ffb800, #ff8c00);
  border: none;
  border-radius: 10px;
  color: #0a0e1a;
  font-family: 'Syne', sans-serif;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.3px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  transition: transform 0.15s, box-shadow 0.15s;
  margin-bottom: 20px;
}

.cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(255,140,0,0.35);
}

.btn-arrow { transition: transform 0.2s; }
.cta-btn:hover .btn-arrow { transform: translateX(4px); }

.login-prompt {
  text-align: center;
  font-size: 13px;
  color: rgba(255,255,255,0.35);
}

.login-link {
  color: #ffb800;
  text-decoration: none;
  font-weight: 500;
}

.login-link:hover { text-decoration: underline; }

@media (max-width: 900px) {
  .side-panel { display: none; }
}

@media (max-width: 480px) {
  .fields-grid { grid-template-columns: 1fr; }
  .field-full { grid-column: 1; }
  .form-panel { padding: 32px 20px; }
}
</style>