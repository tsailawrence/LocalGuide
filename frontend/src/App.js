import React, { useState } from "react";
import "./index.css";
import { Layout, Menu } from "antd";
import Login from "./pages/Login";
import MainPage from "./pages/MainPage";

function App() {
  const [login, setLogin] = useState(false);

  return <>{login ? <MainPage /> : <Login setLogin={setLogin} />}</>;
}

export default App;
