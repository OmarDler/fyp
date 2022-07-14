import {
  Button,
  List,
  Skeleton,
  Modal,
  Input,
  message,
  Space,
  Popconfirm,
  Empty,
} from "antd";
import React, { useEffect, useState } from "react";
const { Search } = Input;
const API = `http://127.0.0.1:5000/lecturers`;

const Lecturer = () => {
  const [initLoading, setInitLoading] = useState(true);
  const [loading, setLoading] = useState(false);
  const [data, setData] = useState([]);
  const [list, setList] = useState([]);
  const [visibleEdit, setVisibleEdit] = useState(false);
  const [visibleAdd, setVisibleAdd] = useState(false);
  const [currentLecturerId, setCurrentLecturerId] = useState("");
  const [currentLecturerName, setCurrentLecturerName] = useState("");
  const [yeet, setYeet] = useState("");
  const [newLecturerName, setNewLecturerName] = useState("");

  useEffect(() => {
    fetch(API)
      .then((res) => res.json())
      .then((res) => {
        setInitLoading(false);
        setData(res.data);
        setList(res.data);
      });
  }, [yeet]);

  const info = (txt) => {
    message.info(txt);
  };

  const updateLecturer = (id, name) => {
    const requestOptions = {
      method: "PUT",
      body: JSON.stringify({ name: name }),
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };
    fetch(`${API}/${id}`, requestOptions)
      .then((response) => response.json())
      .then((res) => {
        if (res.success) {
          setYeet("Lecturer updated successfully to " + name);
          info("Lecturer updated successfully to " + name);
        } else {
          setYeet("Lecturer update failed" + res.message);
          info("Lecturer update failed" + res.message);
        }
      });
  };

  const handleDelete = (id) => {
    const requestOptions = {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };
    fetch(`${API}/${id}`, requestOptions)
      .then((response) => response.json())
      .then((res) => {
        if (res.success) {
          setYeet("Lecturer deleted successfully" + id);
          info("Lecturer deleted successfully");
        } else {
          setYeet("Lecturer delete failed" + res.message);
          info("Lecturer delete failed" + res.message);
        }
      });
  };

  const addLecturer = (name) => {
    const requestOptions = {
      method: "POST",
      body: JSON.stringify({ name: name }),
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };
    fetch(API, requestOptions)
      .then((response) => response.json())
      .then((res) => {
        if (res.success) {
          setYeet("Lecturer added successfully to " + name);
          info("Lecturer " + name + " added successfully!");
        } else {
          setYeet("Lecturer add failed" + res.message);
          info("Lecturer add failed" + res.message);
        }
      });
  };
  const handleOk = () => {
    setLoading(true);
    setTimeout(() => {
      updateLecturer(currentLecturerId, currentLecturerName);
      setLoading(false);
      setVisibleEdit(false);
    }, 2000);
  };
  const handleCancel = () => {
    setVisibleEdit(false);
    setVisibleAdd(false);
  };

  return (
    <div style={{ paddingLeft: 50, paddingRight: 50 }}>
      <div style={{ paddingTop: 60, paddingLeft: 60, paddingRight: 60 }}>
        <Space direction="horizontal">
          <Button
            type="primary"
            onClick={() => {
              setNewLecturerName("");
              setVisibleAdd(true);
            }}
          >
            Add Lecturer
          </Button>
          <Search
            placeholder="Search lecturer"
            allowClear={true}
            onSearch={(value) => {
              if (value === "") {
                setYeet(Date.now());
              }
              setList(
                data.filter((item) =>
                  item[1].toLowerCase().includes(value.toLowerCase())
                )
              );
            }}
            style={{ width: 200, marginLeft: 20 }}
          />
        </Space>
      </div>
      <List
        locale={{
          emptyText: (
            <Empty
              image={Empty.PRESENTED_IMAGE_SIMPLE}
              description={"No lecturers were found"}
            >
              <Button type="primary" onClick={() => setYeet(Date.now())}>
                go back
              </Button>
            </Empty>
          ),
        }}
        style={{ minHeight: "350px", padding: 60 }}
        loading={initLoading}
        itemLayout="horizontal"
        dataSource={list}
        renderItem={(item) => (
          <List.Item
            actions={[
              <Button
                key="list-loadmore-edit"
                type="primary"
                onClick={() => {
                  setVisibleEdit(true);
                  setCurrentLecturerId(item[0]);
                  setCurrentLecturerName(item[1]);
                }}
              >
                edit
              </Button>,
              <Popconfirm
                title="Are you sure？"
                okText="Yes"
                cancelText="No"
                onConfirm={() => handleDelete(item[0])}
              >
                <Button type="danger" key="list-loadmore-more">
                  delete
                </Button>
              </Popconfirm>,
            ]}
          >
            <Skeleton avatar title={false} loading={item.loading} active>
              <List.Item.Meta title={item[1]} />
            </Skeleton>
          </List.Item>
        )}
      />

      <Modal
        visible={visibleEdit}
        title="Edit Lecturer"
        onCancel={handleCancel}
        footer={[
          <Button key="back" onClick={handleCancel}>
            Return
          </Button>,
          <Button
            key="submit"
            type="primary"
            loading={loading}
            onClick={handleOk}
            disabled={currentLecturerName === ""}
          >
            Submit
          </Button>,
        ]}
      >
        <Input
          defaultValue={currentLecturerName}
          onChangeCapture={(text) => setCurrentLecturerName(text.target.value)}
        />
      </Modal>
      <Modal
        visible={visibleAdd}
        title="Add Lecturer"
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
              addLecturer(newLecturerName);
              setVisibleAdd(false);
            }}
            disabled={newLecturerName === ""}
          >
            Submit
          </Button>,
        ]}
      >
        <Input
          placeholder="Enter Lecturer Name"
          onChange={(text) => setNewLecturerName(text.target.value)}
        />
      </Modal>
    </div>
  );
};

export default Lecturer;
