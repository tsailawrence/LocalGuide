import { createContext, useContext, useState, useEffect } from "react";
import { message } from "antd";

const ADD_MESSAGE_COLOR = "#3d84b8";
const REGULAR_MESSAGE_COLOR = "#2b2e4a";
const ERROR_MESSAGE_COLOR = "#fb3640";

const AppContext = createContext({});

const makeMessage = (message, color) => {
  return { message, color };
};

const AppProvider = (props) => {
  const [me, setMe] = useState("");
  const [signIn, setSignIn] = useState();
  const [status, setStatus] = useState([]);
  const [result, setResult] = useState([]);

  const displayStatus = (s) => {
    if (s.msg) {
      const { type, msg } = s;
      const content = {
        content: msg,
        duration: 1,
      };
      switch (type) {
        case "success":
          message.success(content);
          break;
        case "error":
        default:
          message.error(content);
          break;
      }
    }
  };
  useEffect(() => {
    displayStatus(status);
  }, [status]);

  return (
    <AppContext.Provider
      value={{
        me,
        setMe,
        signIn,
        setSignIn,
        status,
        setStatus,
        setResult,
        result,
      }}
      {...props}
    />
  );
};

const useApp = () => useContext(AppContext);
export { AppProvider, useApp };
