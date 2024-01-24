from user.apis import LoginAPI, SendOTPAPI

urls = {
    "otp/": SendOTPAPI,
    "login/": LoginAPI,
}
