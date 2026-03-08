<template>
  <div class="reg-root">
    <div class="bg-grid"></div>
    <div class="bg-glow bg-glow--purple"></div>

    <div class="reg-split">
      <!-- Side panel -->
      <div class="side-panel">
        <router-link to="/" class="back-link">← Back to Login</router-link>
        <div class="side-content">
          <div class="side-tag">COMPANY PORTAL</div>
          <h2 class="side-heading">Find your<br>next hire<br>here.</h2>
          <div class="step-trail">
            <div class="step-item step-active"><span class="step-dot"></span><span>Register Company</span></div>
            <div class="step-line"></div>
            <div class="step-item"><span class="step-dot"></span><span>Admin Approval</span></div>
            <div class="step-line"></div>
            <div class="step-item"><span class="step-dot"></span><span>Post Drives</span></div>
          </div>
        </div>
        <div class="benefit-list">
          <div class="benefit-item" v-for="b in benefits" :key="b.text">
            <span class="b-icon">{{ b.icon }}</span>
            <span class="b-text">{{ b.text }}</span>
          </div>
        </div>
      </div>

      <!-- Form panel -->
      <div class="form-panel">
        <div class="form-card">
          <div class="form-header">
            <span class="form-tag">🏢 Company</span>
            <h2 class="form-title">Register your company</h2>
            <p class="form-sub">Submit your details — our admin team will verify and approve your account</p>
          </div>

          <div class="fields-grid">
            <div class="field-group field-full">
              <label class="field-label">HR Representative Name</label>
              <input v-model="form.name" class="styled-input" placeholder="e.g. Sarah Johnson" />
            </div>

            <div class="field-group">
              <label class="field-label">HR Email</label>
              <input v-model="form.email" class="styled-input" placeholder="hr@company.com" type="email" />
            </div>

            <div class="field-group">
              <label class="field-label">Password</label>
              <input v-model="form.password" class="styled-input" placeholder="Create password" type="password" />
            </div>

            <div class="field-group field-full">
              <label class="field-label">Company Name</label>
              <input v-model="form.company_name" class="styled-input" placeholder="e.g. Acme Technologies Pvt Ltd" />
            </div>

            <div class="field-group">
              <label class="field-label">HR Contact Number</label>
              <input v-model="form.hr_contact" class="styled-input" placeholder="+91 98765 43210" />
            </div>

            <div class="field-group">
              <label class="field-label">Company Website</label>
              <input v-model="form.website" class="styled-input" placeholder="https://company.com" type="url" />
            </div>
          </div>

          <div class="approval-notice">
            <span class="notice-icon">ℹ</span>
            <span>Your account will be reviewed and activated by an administrator before you can post drives.</span>
          </div>

          <button @click="register" class="cta-btn">
            <span>Submit for Approval</span>
            <span class="btn-arrow">→</span>
          </button>

          <p class="login-prompt">Already have an account? <router-link to="/" class="login-link">Sign in</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import api from "../services/api"

export default {
  data() {
    return {
      form: {},
      benefits: [
        { icon: '🎯', text: 'Access 5,000+ pre-screened candidates' },
        { icon: '⚡', text: 'Fast-track hiring within 2 weeks' },
        { icon: '📊', text: 'Real-time application analytics' },
      ]
    }
  },
  methods: {
    async register() {
      await api.post("/auth/register/company", this.form)
      alert("Company registered. Await admin approval.")
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

.bg-glow--purple {
  position: fixed;
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(140,80,255,0.09) 0%, transparent 70%);
  bottom: -80px; right: -80px;
  border-radius: 50%;
  pointer-events: none;
}

.reg-split {
  display: flex;
  min-height: 100vh;
  position: relative;
  z-index: 1;
}

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
  position: absolute; top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, #7c3aed, transparent);
}

.back-link {
  color: rgba(255,255,255,0.35);
  text-decoration: none;
  font-size: 13px;
  transition: color 0.2s;
}
.back-link:hover { color: #ffb800; }

.side-content { flex: 1; display: flex; flex-direction: column; justify-content: center; }

.side-tag {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 3px;
  color: #a78bfa;
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

.step-trail { display: flex; flex-direction: column; gap: 0; margin-bottom: 48px; }

.step-item {
  display: flex; align-items: center; gap: 14px;
  color: rgba(255,255,255,0.3);
  font-size: 14px; font-weight: 500;
}

.step-active { color: #a78bfa; }

.step-dot {
  width: 10px; height: 10px; border-radius: 50%;
  background: rgba(255,255,255,0.15); flex-shrink: 0;
}

.step-active .step-dot {
  background: #a78bfa;
  box-shadow: 0 0 12px rgba(167,139,250,0.6);
}

.step-line {
  width: 1px; height: 24px;
  background: rgba(255,255,255,0.08);
  margin-left: 5px;
}

.benefit-list { display: flex; flex-direction: column; gap: 12px; }

.benefit-item {
  display: flex; align-items: center; gap: 12px;
  color: rgba(255,255,255,0.5);
  font-size: 13px;
}

.b-icon { font-size: 18px; }

.form-panel {
  flex: 1;
  display: flex; align-items: center; justify-content: center;
  padding: 48px 40px;
}

.form-card {
  width: 100%; max-width: 500px;
  animation: slideUp 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

.form-header { margin-bottom: 32px; }

.form-tag {
  display: inline-block;
  background: rgba(167,139,250,0.12);
  color: #a78bfa;
  border: 1px solid rgba(167,139,250,0.25);
  border-radius: 20px;
  padding: 4px 12px;
  font-size: 12px; font-weight: 600;
  letter-spacing: 0.5px; margin-bottom: 14px;
}

.form-title {
  font-family: 'Syne', sans-serif;
  font-size: 28px; font-weight: 700; color: #ffffff; margin-bottom: 6px;
}

.form-sub { font-size: 14px; color: rgba(255,255,255,0.4); line-height: 1.5; }

.fields-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px;
}

.field-group { display: flex; flex-direction: column; gap: 7px; }
.field-full { grid-column: 1 / -1; }

.field-label {
  font-size: 11px; font-weight: 600;
  color: rgba(255,255,255,0.4);
  text-transform: uppercase; letter-spacing: 1px;
}

.styled-input {
  width: 100%;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.09);
  border-radius: 9px;
  padding: 13px 15px;
  color: #ffffff;
  font-family: 'DM Sans', sans-serif;
  font-size: 14px; outline: none;
  transition: border-color 0.2s, background 0.2s;
}

.styled-input::placeholder { color: rgba(255,255,255,0.18); }

.styled-input:focus {
  border-color: rgba(167,139,250,0.45);
  background: rgba(167,139,250,0.04);
}

.approval-notice {
  display: flex; align-items: flex-start; gap: 10px;
  background: rgba(167,139,250,0.06);
  border: 1px solid rgba(167,139,250,0.15);
  border-radius: 9px;
  padding: 12px 14px;
  font-size: 13px;
  color: rgba(255,255,255,0.5);
  line-height: 1.5;
  margin-bottom: 20px;
}

.notice-icon { color: #a78bfa; flex-shrink: 0; font-style: normal; }

.cta-btn {
  width: 100%; padding: 15px 24px;
  background: linear-gradient(135deg, #7c3aed, #a78bfa);
  border: none; border-radius: 10px;
  color: #ffffff;
  font-family: 'Syne', sans-serif;
  font-size: 15px; font-weight: 700;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  transition: transform 0.15s, box-shadow 0.15s;
  margin-bottom: 20px;
}

.cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px rgba(124,58,237,0.4);
}

.btn-arrow { transition: transform 0.2s; }
.cta-btn:hover .btn-arrow { transform: translateX(4px); }

.login-prompt {
  text-align: center; font-size: 13px; color: rgba(255,255,255,0.35);
}

.login-link { color: #a78bfa; text-decoration: none; font-weight: 500; }
.login-link:hover { text-decoration: underline; }

@media (max-width: 900px) { .side-panel { display: none; } }
@media (max-width: 480px) {
  .fields-grid { grid-template-columns: 1fr; }
  .field-full { grid-column: 1; }
  .form-panel { padding: 32px 20px; }
}
</style>