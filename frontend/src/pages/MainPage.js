import React, { useEffect, useState } from "react";
import { LikeOutlined, MessageOutlined, StarOutlined } from "@ant-design/icons";
import { Layout, Menu, Avatar, List, Space, Input } from "antd";
import RestaurantItem from "./RestaurantItem";
import axios from "../api";
import { useApp } from "../UseApp";

import {} from "@ant-design/icons";
import { withSuccess } from "antd/es/modal/confirm";

const { Header, Sider, Content } = Layout;
const { TextArea } = Input;

function MainPage() {
  const { setStatus, result, setResult } = useApp();
  const [review, setReview] = useState("");

  const onGetVector = async () => {
    console.log(review);
    const {
      data: { content, message },
    } = await axios.get("/compute_user_embedding", {
      params: { review: review },
    });

    switch (message) {
      case "success":
        setStatus({ type: "success", msg: content });
        break;
      case "error":
        setStatus({ type: "error", msg: content });
        break;
    }
  };

  const onPredict = async () => {
    const {
      data: { content, message, res },
      // result might be string, need to be converted to array
    } = await axios.get("/predict");

    console.log(res)
    let restaurants = []
    res.forEach(r_id => 
      restaurants.push(r_id[0])
    )

    switch (message) {
      case "success":
        setStatus({ type: "success", msg: content });
        setResult([...restaurants]);
        break;
      case "error":
        setStatus({ type: "error", msg: content });
        break;
    }

    console.log(result)
  };

  return (
    <div className="main_page_container">
      <h1>Main</h1>
      <div className="restaurant__list">
        {result.map((restaurant, index) => (
          <RestaurantItem restaurant={restaurant} key={index} value={index} />
        ))}
        <TextArea
          showCount
          maxLength={100}
          onChange={(e) => setReview(e.target.value)}
          value={review}
        />
        <button onClick={onGetVector}>Compute user vector</button>
        <button onClick={onPredict}>Predict</button>
      </div>
    </div>
  );
}

export default MainPage;
