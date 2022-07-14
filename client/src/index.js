import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";
import Lecturer from "./routes/lecturer";
import Module from "./routes/module";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="lecturers" element={<Lecturer />} />
      <Route path="modules" element={<Module />} />
    </Routes>
  </BrowserRouter>
);
