import bcrypt from "bcrypt";
import signUpHelpers from "../Helpers/signUp";
import UserModel from "../Schemas/User";

describe("insert", () => {
  let mockedUser;
  beforeAll(() => {
    mockedUser = {
      _id: "test",
      mail: "test mail",
      userName: "test name",
      firstName: "test first",
      lastName: "test last",
      password: "test password",
      picture: "test picture",
      __v: 0
    };
  });

  afterAll(async () => {
    await UserModel.deleteOne({ _id: "test" });
  });

  it("should insert user", async () => {
    expect(await signUpHelpers.createUser(mockedUser, false)).toBe(true);
  });

  it("should be the same user", async () => {
    const findUser = await UserModel.findOne({ _id: "test" });
    const res = await bcrypt.compare(mockedUser.password, findUser.password);
    findUser.password = res ? "test password" : findUser.password;
    expect(mockedUser).toEqual(findUser.toJSON());
  });
});
