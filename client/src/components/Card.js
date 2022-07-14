import { Card } from "antd";
import React from "react";
const { Meta } = Card;

const Cardant = ({ svg, title }) => (
  <Card
    hoverable
    style={{
      width: 290,
    }}
    cover={<img alt="example" src={svg} />}
  >
    <Meta title={title} />
  </Card>
);

export default Cardant;
