import { React, useState } from "react";
import { Space, Typography, Button } from "antd";
import Cardant from "./components/Card";
import lecturer from "./assets/Lecturer.svg";
import module from "./assets/module.svg";
import { Link } from "react-router-dom";
import { DownloadOutlined } from "@ant-design/icons";

import "./App.css";
import "antd/dist/antd.min.css";

const { Title } = Typography;
function App() {
  const [loading, setLoading] = useState(false);
  return (
    <div className="App">
      <Title style={{ paddingTop: 20 }}>Smart Timetable</Title>
      <Space
        direction="horizontal"
        style={{ width: "100%", justifyContent: "space-evenly", padding: 60 }}
      >
        <Link to="/lecturers">
          <Cardant title="Lecturers" svg={lecturer} />
        </Link>
        <Link to="/modules">
          <Cardant title={"Modules"} svg={module} />
        </Link>
      </Space>
      <Button
        loading={loading}
        type="primary"
        shape="round"
        icon={<DownloadOutlined />}
        size={"large"}
        onClick={() => {
          setLoading(true);
          fetch(`http://127.0.0.1:5000/download/timetable`, {
            method: "GET",
          }).then((response) => {
            response.blob().then((blob) => {
              let url = window.URL.createObjectURL(blob);
              let a = document.createElement("a");
              a.href = url;
              a.download = "timetable.csv";
              a.click();
              setLoading(false);
            });
          });
        }}
      >
        Generate Timetable
      </Button>
    </div>
  );
}

export default App;
