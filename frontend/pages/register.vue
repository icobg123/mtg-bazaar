<template>
  <v-main class="register-page">
    <v-container>
      <v-layout flex align-center justify-center>
        <v-flex xs6 sm6 elevation-6>
          <v-card>
            <v-card-title flex align-center justify-center>
              <h1>Register</h1>
            </v-card-title>
            <v-card-text class="pt-4">
              <div>
                <v-form ref="form"
                        v-model="valid"
                        lazy-validation>
                  <v-text-field
                    v-model="userData.email"
                    label="Enter your e-mail address"
                    :rules="emailRules"
                    counter
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="userData.password"
                    label="Enter your password"
                    required
                    :append-icon="
                      userData.showPassword ? 'mdi-eye' : 'mdi-eye-off'
                    "
                    :type="userData.showPassword ? 'text' : 'password'"
                    @click:append="
                      userData.showPassword = !userData.showPassword
                    "
                  ></v-text-field>
                  <v-text-field
                    v-model="userData.password2"
                    label="Confirm password"
                    :append-icon="
                      userData.showPassword2 ? 'mdi-eye' : 'mdi-eye-off'
                    "
                    :type="userData.showPassword2 ? 'text' : 'password'"
                    required
                    @click:append="
                      userData.showPassword2 = !userData.showPassword2
                    "
                  ></v-text-field>
                  <v-layout justify-space-between>
                    <v-btn @click="signUp(userData)">
                      Register
                    </v-btn>
                    <a href="">Forgot Password</a>
                  </v-layout>
                  <!--                  <Notification :message="error" v-if="error"/>-->
                  <v-snackbar
                    v-model="error"
                  >
                    {{ error_text }}

                    <template v-slot:action="{ attrs }">
                      <v-btn
                        color="pink"
                        text
                        v-bind="attrs"
                        @click="snackbar = false"
                      >
                        Close
                      </v-btn>
                    </template>
                  </v-snackbar>
                </v-form>
              </div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
export default {
  middleware: 'guest',
  data: () => ({
    valid: true,
    name: '',
    nameRules: [
      v => !!v || 'Name is required',
      v => (v && v.length <= 10) || 'Name must be less than 10 characters',
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
    ],
    userData: {
      email: '',
      password: '',
      password2: '',
      showPassword: false,
      showPassword2: false,
    },
    error: false,
    error_text: '',
  }),
  methods: {
    validate() {
      this.$refs.form.validate()
    },
    reset() {
      this.$refs.form.reset()
    },
    resetValidation() {
      this.$refs.form.resetValidation()
    },
    signUp(registrationInfo) {
      this.$axios
        .$post('accounts/users/', registrationInfo)
        .then((response) => {
          console.log('Scuccessful')
        })
        .catch((error) => {
          this.error = true
          this.error_text = error.response.data
          console.log('error:', error.response)
        })
      this.$auth.loginWith('local', {
        data: registrationInfo,
      })
    },
  },
}
</script>
