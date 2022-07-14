import { React, useState, useEffect } from "react";
import {
  Button,
  List,
  Modal,
  Input,
  message,
  Space,
  Popconfirm,
  Empty,
  Typography,
  Menu,
  Dropdown,
  Divider,
} from "antd";
import { DownOutlined } from "@ant-design/icons";
import "../App.css";

const { Search } = Input;
const API = `http://127.0.0.1:5000/modules`;

const Module = () => {
  const [newModuleCode, setNewModuleCode] = useState("");
  const [data, setData] = useState([]);
  const [list, setList] = useState([]);
  const [lecturerList, setLecturerList] = useState([]);
  const [visibleEdit, setVisibleEdit] = useState(false);
  const [visibleAdd, setVisibleAdd] = useState(false);
  const [currentModuleId, setCurrentModuleId] = useState("");
  const [currentModuleName, setCurrentModuleName] = useState("");
  const [loading, setLoading] = useState(false);
  const [initLoading, setInitLoading] = useState(true);
  const [yeet, setYeet] = useState("");
  const [currentLecturerId, setCurrentLecturerId] = useState("");
  const [currentLecturerName, setCurrentLecturerName] = useState("");

  const { Title } = Typography;

  const handleCancel = () => {
    setVisibleEdit(false);
    setVisibleAdd(false);
    setCurrentLecturerId("");
    setCurrentLecturerName("");
    setCurrentModuleId("");
    setCurrentModuleName("");
    setNewModuleCode("");
  };

  const getLecturer = (id) => {
    return String(
      //eslint-disable-next-line
      lecturerList.map((lecturer) => (lecturer[0] == id ? lecturer[1] : ""))
    );
  };

  useEffect(() => {
    fetch(API)
      .then((res) => res.json())
      .then((res) => {
        setData(res.data);
        setList(res.data);
      });
    fetch(`http://127.0.0.1:5000/lecturers`)
      .then((res) => res.json())
      .then((res) => {
        setLecturerList(res.data);
        setInitLoading(false);
      });
  }, [yeet]);
  return (
    <div style={{ padding: 100 }}>
      <Space direction="horizontal">
        <Button
          type="primary"
          onClick={() => {
            setVisibleAdd(true);
            setCurrentLecturerName("Lecturer");
            setCurrentLecturerId("");
            setCurrentModuleName("");
            // setNewLecturerName("");
            setNewModuleCode("");
            setCurrentModuleId("");
          }}
        >
          Add Module
        </Button>
        <Search
          placeholder="Search Module"
          allowClear={true}
          onSearch={(value) => {
            if (value === "") {
              setYeet(Date.now());
            }
            setList(
              data.filter(
                (item) =>
                  item[0].toLowerCase().includes(value.toLowerCase()) ||
                  item[1].toLowerCase().includes(value.toLowerCase()) ||
                  getLecturer(item[2])
                    .replace(/,/g, "")
                    .toLowerCase()
                    .includes(value.toLowerCase())
              )
            );
          }}
          style={{ width: 200, marginLeft: 20 }}
        />
      </Space>
      <Divider />
      <List
        locale={{
          emptyText: (
            <Empty
              image={Empty.PRESENTED_IMAGE_SIMPLE}
              description={"No modules were found"}
            >
              <Button type="primary" onClick={() => setYeet(Date.now())}>
                go back
              </Button>
            </Empty>
          ),
        }}
        itemLayout="horizontal"
        loading={initLoading}
        dataSource={list}
        renderItem={(item) => (
          <List.Item>
            <List.Item.Meta
              title={item[1]}
              description={
                item[0] + "  " + getLecturer(item[2]).replace(/,/g, "")
              }
            />
            <Space>
              <Button
                type="primary"
                onClick={() => {
                  setVisibleEdit(true);
                  setCurrentModuleId(item[0]);
                  setNewModuleCode(item[0]);
                  setCurrentModuleName(item[1]);
                  setCurrentLecturerId(item[2]);
                  setCurrentLecturerName(
                    getLecturer(item[2]).replace(/,/g, "")
                  );
                }}
              >
                Edit
              </Button>
              <Popconfirm
                title="Do you want to delete this module?"
                onConfirm={() => {
                  fetch(`${API}/${item[0]}`, {
                    method: "DELETE",
                    headers: {
                      "Content-Type": "application/json",
                    },
                  })
                    .then((res) => res.json())
                    .then((res) => {
                      if (res.success) {
                        message.success("Deleted successfully");
                        setYeet(Math.random());
                      } else {
                        message.error("Delete failed");
                      }
                    });
                }}
              >
                <Button type="danger">Delete</Button>
              </Popconfirm>
            </Space>
          </List.Item>
        )}
      />
      <Modal
        title="Edit Module"
        visible={visibleEdit}
        onCancel={handleCancel}
        footer={[
          <Button key="back" onClick={handleCancel}>
            Return
          </Button>,
          <Button
            key="submit"
            type="primary"
            loading={loading}
            onClick={() => {
              setLoading(true);
              fetch(`${API}/${currentModuleId}`, {
                method: "PUT",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  code: newModuleCode,
                  lecturer_id: currentLecturerId,
                  name: currentModuleName,
                }),
              })
                .then((res) => res.json())
                .then((res) => {
                  if (res.success) {
                    message.success("Updated successfuly");
                    setYeet(Date.now());
                    setLoading(false);
                    setVisibleEdit(false);
                  } else {
                    message.error("Update failed");
                    setLoading(false);
                  }
                });
            }}
          >
            Submit
          </Button>,
        ]}
      >
        <Space
          direction="vertical"
          style={{
            width: "100%",
            justifyContent: "space-between",
          }}
        >
          <Space direction="horizontal">
            <Title level={5}>Module Code</Title>
            <Input
              value={newModuleCode}
              onChangeCapture={(text) => {
                setNewModuleCode(text.target.value);
              }}
              style={{ width: 100, marginLeft: 4 }}
            />
          </Space>
          <Space direction="horizontal">
            <Title level={5}>Module Name</Title>
            <Input
              value={currentModuleName}
              onChangeCapture={(text) =>
                setCurrentModuleName(text.target.value)
              }
              style={{ width: 350 }}
            />
          </Space>
          <Space direction="horizontal">
            <Title level={5}>Lecturer</Title>
            <Dropdown
              className="ant-dropdown-menu"
              trigger={["click"]}
              overlay={
                <Menu
                  items={lecturerList.map((lecturer) => {
                    return {
                      key: lecturer[0],
                      label: lecturer[1],
                    };
                  })}
                  onClick={(e) => {
                    // console.log(e);
                    setCurrentLecturerId(e.key);
                    setCurrentLecturerName(
                      getLecturer(e.key).replace(/,/g, "")
                    );
                  }}
                />
              }
            >
              <Button>
                <Space>
                  {currentLecturerName}
                  <DownOutlined />
                </Space>
              </Button>
            </Dropdown>
          </Space>
        </Space>
      </Modal>
      <Modal
        title="Add Module"
        visible={visibleAdd}
        onCancel={handleCancel}
        footer={[
          <Button key="back" onClick={handleCancel}>
            Return
          </Button>,
          <Button
            disabled={
              newModuleCode === "" ||
              currentModuleName === "" ||
              currentLecturerId === ""
            }
            key="submit"
            type="primary"
            loading={loading}
            onClick={() => {
              setLoading(true);
              fetch(API, {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  code: newModuleCode,
                  lecturer_id: currentLecturerId,
                  name: currentModuleName,
                }),
              })
                .then((res) => res.json())
                .then((res) => {
                  console.log(res);
                  if (res.success) {
                    message.success("Added successfully");
                    setYeet(Date.now());
                    setLoading(false);
                  } else {
                    message.error("Add failed");
                    setLoading(false);
                  }
                });

              setVisibleAdd(false);
            }}
          >
            Submit
          </Button>,
        ]}
      >
        <Space
          direction="vertical"
          style={{
            width: "100%",
            justifyContent: "space-between",
          }}
        >
          <Space direction="horizontal">
            <Title level={5}>Module Code</Title>
            <Input
              value={newModuleCode}
              onChangeCapture={(text) => {
                setNewModuleCode(text.target.value);
              }}
              style={{ width: 100, marginLeft: 4 }}
            />
          </Space>
          <Space direction="horizontal">
            <Title level={5}>Module Name</Title>
            <Input
              value={currentModuleName}
              onChangeCapture={(text) =>
                setCurrentModuleName(text.target.value)
              }
              style={{ width: 350 }}
            />
          </Space>
          <Space direction="horizontal">
            <Title level={5}>Lecturer</Title>
            <div style={{ paddingLeft: 40 }}>
              <Dropdown
                // className="ant-dropdown-menu"
                trigger={["click"]}
                overlay={
                  <Menu
                    items={lecturerList.map((lecturer) => {
                      return {
                        key: lecturer[0],
                        label: lecturer[1],
                      };
                    })}
                    onClick={(e) => {
                      // console.log(e);
                      setCurrentLecturerId(e.key);
                      setCurrentLecturerName(
                        getLecturer(e.key).replace(/,/g, "")
                      );
                      // console.log(getLecturer(e.key).replace(/,/g, ""));
                    }}
                  />
                }
              >
                <Button>
                  <Space>
                    {currentLecturerName} <DownOutlined />
                  </Space>
                </Button>
              </Dropdown>
            </div>
          </Space>
        </Space>
      </Modal>
    </div>
  );
};

export default Module;
