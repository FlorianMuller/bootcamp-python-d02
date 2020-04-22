import passport from "passport";
import { OAuth2Strategy as GoogleStrategy } from "passport-google-oauth";
// import UserModel from "./Schemas/User";

// No need for the
// passport.serializeUser((user, done) => {
//   done(null, user);
// });

// passport.deserializeUser((user, done) => {
//   done(null, user);
// });

passport.use(
  new GoogleStrategy(
    {
      clientID: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET,
      callbackURL: "http://localhost:8080/api/user/google/callback"
    },
    (_accessToken, _refreshToken, profile, done) => {
      console.log("profile", profile.id);
      // todo: Create user with profile

      done(null, { user: profile.id, lol: "toto" });
    }
  )
);

export default passport;
