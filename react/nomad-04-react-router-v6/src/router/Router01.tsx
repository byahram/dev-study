import { BrowserRouter, Route, Routes } from "react-router-dom";
import Header from "../components/Header";
import Home from "../screens/Home";
import About from "../screens/About";

export default function Router01() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}
