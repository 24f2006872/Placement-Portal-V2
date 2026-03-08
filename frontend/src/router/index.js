import {createRouter,createWebHistory} from "vue-router"

import Login from "../views/LoginPage.vue"
import AdminDashboard from "../views/AdminDashboard.vue"
import StudentDashboard from "../views/StudentDashboard.vue"
import CompanyDashboard from "../views/CompanyDashboard.vue"
import RegisterStudent from "../views/RegisterStudent.vue"
import RegisterCompany from "../views/RegisterCompany.vue"

const routes=[

{path:"/",component:Login},

{path:"/admin",component:AdminDashboard},

{path:"/student",component:StudentDashboard},

{path:"/company",component:CompanyDashboard},

{path:"/register-student",component:RegisterStudent},

{path:"/register-company",component:RegisterCompany}

]

const router=createRouter({
history:createWebHistory(),
routes
})

export default router