import * as React from "react";
import Adapter from "enzyme-adapter-react-16";
import EnzymeToJson from "enzyme-to-json";
import { mount, configure } from "enzyme";
import App from "../components/App";

configure({ adapter: new Adapter() });

jest.mock("../hooks/useApi", () => (): {
  data: unknown;
  loading: boolean;
  error: void;
  setUrl: () => void;
} => ({
  data: [],
  loading: false,
  error: null,
  setUrl: jest.fn()
}));

jest.mock("../helpers/history", () => {
  // require after code makes the disable required
  // eslint-disable-next-line
  const { createBrowserHistory } = require("history");

  const history = createBrowserHistory({
    keyLength: 0
  });

  return history;
});

describe("App", () => {
  it("renders correctly", () => {
    const domNode = mount(<App />);
    expect(EnzymeToJson(domNode)).toMatchSnapshot();
  });
});
