import React, { useState, useEffect, useRef } from "react";
import "../index.css";
import { useApp } from "../UseApp";
import axios from "../api";
import { Button, Checkbox, Form, Input } from "antd";
import map from "../map.png";

function Login({ setLogin }) {
  const { me, setMe, status, setStatus } = useApp();
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    if (id === "") document.getElementById("submit").disabled = true;
    else document.getElementById("submit").disabled = false;
  }, [id]);

  const handleLogin = async () => {
    if (!id) {
      setStatus({
        type: "error",
        msg: "Missing student ID",
      });
    } else {
      const {
        data: { message, content },
      } = await axios.post("/login", {
        userId: id,
      });

      switch (message) {
        default:
          break;
        case "error":
          setStatus({
            type: "error",
            msg: content,
          });
          alert(content);
          break;
        case "success":
          console.log(content);
          setMe(content.name);
          setLogin(true);
          setStatus({
            type: "success",
            msg: "Login successfully!",
          });
          break;
      }
    }
  };

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        height: "100vh",
      }}
    >
      <div className="loginFormContainer">
        <img src={map} alt={"map"} style={{ height: 150, marginBottom: 30 }} />
        <Form
          name="basic"
          className="loginForm"
          //   labelCol={{ span: 8 }}
          wrapperCol={{ span: 30 }}
          initialValues={{ remember: true }}
          autoComplete="off"
        >
          <h1
            style={{
              fontSize: 40,
              paddingBottom: 50,
            }}
          >
            Local Guide Recommendation
          </h1>
          <Form.Item
            label="User ID"
            name="User ID"
            rules={[
              {
                required: true,
                message: "Please input your User ID!",
              },
            ]}
          >
            <Input
              value={id}
              id="userID"
              onChange={(e) => {
                setId(e.target.value);
              }}
            />
          </Form.Item>

          <Form.Item
            name="remember"
            valuePropName="checked"
            wrapperCol={{ offset: 9, span: 16 }}
          >
            <Checkbox>Remember me</Checkbox>
          </Form.Item>
          <Form.Item wrapperCol={{ offset: 10, span: 16 }}>
            <Button
              id="submit"
              type="primary"
              htmlType="submit"
              style={{
                margin: 5,
                width: 80,
              }}
              onClick={handleLogin}
            >
              Submit
            </Button>
          </Form.Item>
        </Form>
      </div>
    </div>
  );
}

export default Login;
